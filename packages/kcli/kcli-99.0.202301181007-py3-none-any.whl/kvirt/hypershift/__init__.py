#!/usr/bin/env python

from glob import glob
from kvirt.common import success, error, pprint, info2, container_mode, warning
from kvirt.common import get_oc, pwd_path, get_installer_rhcos, get_ssh_pub_key, boot_baremetal_hosts
from kvirt.defaults import OPENSHIFT_TAG
from kvirt.openshift import process_apps, update_etc_hosts
from kvirt.openshift import get_ci_installer, get_downstream_installer, get_installer_version, same_release_images
from ipaddress import ip_network
import json
import os
import re
import socket
import sys
from shutil import which, copy2
from subprocess import call
from time import sleep
from urllib.parse import urlparse
import yaml

virtplatforms = ['kvm', 'kubevirt', 'ovirt', 'openstack', 'vsphere']
cloudplatforms = ['aws', 'gcp', 'ibm']


def handle_baremetal_iso(config, plandir, cluster, data, baremetal_hosts=[]):
    baremetal_iso_overrides = data.copy()
    baremetal_iso_overrides['noname'] = True
    baremetal_iso_overrides['workers'] = 1
    result = config.plan(cluster, inputfile=f'{plandir}/kcli_plan.yml', overrides=baremetal_iso_overrides,
                         onlyassets=True)
    iso_data = result['assets'][0]
    with open('iso.ign', 'w') as f:
        f.write(iso_data)
    iso_pool = data.get('pool') or config.pool
    config.create_openshift_iso(cluster, ignitionfile='iso.ign', installer=True, uefi=True)
    if baremetal_hosts:
        iso_pool_path = config.k.get_pool_path(iso_pool)
        chmodcmd = f"chmod 666 {iso_pool_path}/{cluster}-worker.iso"
        call(chmodcmd, shell=True)
        pprint("Creating httpd deployment to host iso for baremetal workers")
        httpdcmd = f"oc create -f {plandir}/httpd.yaml"
        call(httpdcmd, shell=True)
        svcip_cmd = 'oc get node -o yaml'
        svcip = yaml.safe_load(os.popen(svcip_cmd).read())['items'][0]['status']['addresses'][0]['address']
        svcport_cmd = 'oc get svc -n default httpd-kcli-svc -o yaml'
        svcport = yaml.safe_load(os.popen(svcport_cmd).read())['spec']['ports'][0]['nodePort']
        podname = os.popen('oc -n default get pod -l app=httpd-kcli -o name').read().split('/')[1].strip()
        try:
            call(f"oc wait -n default --for=condition=Ready pod/{podname}", shell=True)
        except Exception as e:
            error(f"Hit {e}")
            sys.exit(1)
        copycmd = f"oc -n default cp {iso_pool_path}/{cluster}-worker.iso {podname}:/var/www/html"
        call(copycmd, shell=True)
        return f'http://{svcip}:{svcport}/{cluster}-worker.iso'


def scale(config, plandir, cluster, overrides):
    plan = cluster
    data = {'cluster': cluster, 'kube': cluster, 'kubetype': 'hypershift'}
    data['basedir'] = '/workdir' if container_mode() else '.'
    cluster = data.get('cluster')
    clusterdir = os.path.expanduser(f"~/.kcli/clusters/{cluster}")
    if os.path.exists(f"{clusterdir}/kcli_parameters.yml"):
        with open(f"{clusterdir}/kcli_parameters.yml", 'r') as install:
            installparam = yaml.safe_load(install)
            data.update(installparam)
            plan = installparam.get('plan', plan)
    data.update(overrides)
    with open(f"{clusterdir}/kcli_parameters.yml", 'w') as paramfile:
        yaml.safe_dump(data, paramfile)
    pprint(f"Scaling on client {config.client}")
    worker_overrides = data.copy()
    os.chdir(os.path.expanduser("~/.kcli"))
    old_baremetal_hosts = installparam.get('baremetal_hosts', [])
    new_baremetal_hosts = overrides.get('baremetal_hosts', [])
    baremetal_hosts = [entry for entry in new_baremetal_hosts if entry not in old_baremetal_hosts]
    if baremetal_hosts:
        if not old_baremetal_hosts:
            iso_url = handle_baremetal_iso(config, plandir, cluster, data, baremetal_hosts)
        else:
            svcip_cmd = 'oc get node -o yaml'
            svcip = yaml.safe_load(os.popen(svcip_cmd).read())['items'][0]['status']['addresses'][0]['address']
            svcport_cmd = 'oc get svc -n default httpd-kcli-svc -o yaml'
            svcport = yaml.safe_load(os.popen(svcport_cmd).read())['spec']['ports'][0]['nodePort']
            iso_url = f'http://{svcip}:{svcport}/{cluster}-worker.iso'
        boot_baremetal_hosts(baremetal_hosts, iso_url, overrides=overrides, debug=config.debug)
        worker_overrides['workers'] = worker_overrides.get('workers', 2) - len(new_baremetal_hosts)
    if worker_overrides.get('workers', 2) <= 0:
        return
    threaded = data.get('threaded', False) or data.get('workers_threaded', False)
    config.plan(plan, inputfile=f'{plandir}/kcli_plan.yml', overrides=worker_overrides, threaded=threaded)


def create(config, plandir, cluster, overrides):
    log_level = 'debug' if config.debug else 'info'
    os.environ["PATH"] += f":{os.getcwd()}"
    k = config.k
    platform = config.type
    arch = k.get_capabilities()['arch'] if config.type == 'kvm' else 'x86_64'
    arch_tag = 'arm64' if arch in ['aarch64', 'arm64'] else 'latest'
    overrides['arch_tag'] = arch_tag
    if 'KUBECONFIG' not in os.environ:
        warning("KUBECONFIG not set...Using .kube/config instead")
    elif not os.path.isabs(os.environ['KUBECONFIG']):
        os.environ['KUBECONFIG'] = f"{os.getcwd()}/{os.environ['KUBECONFIG']}"
    data = {'kubetype': 'hypershift',
            'domain': 'karmalabs.corp',
            'baremetal_iso': False,
            'coredns': True,
            'mdns': False,
            'network': 'default',
            'etcd_size': 4,
            'workers': 2,
            'async': False,
            'tag': OPENSHIFT_TAG,
            'version': 'stable',
            'network_type': 'OVNKubernetes',
            'fips': False,
            'hypershift_image': 'quay.io/hypershift/hypershift-operator:latest',
            'namespace': 'clusters',
            'disconnected_url': None,
            'pull_secret': 'openshift_pull.json',
            'sslip': False,
            'kubevirt_ingress_service': False,
            'cluster_network_ipv4': '10.129.0.0/14',
            'service_network_ipv4': '172.31.0.0/16',
            'retries': 3}
    data.update(overrides)
    retries = data.get('retries')
    if 'cluster' in overrides:
        clustervalue = overrides.get('cluster')
    elif cluster is not None:
        clustervalue = cluster
    else:
        clustervalue = 'testk'
    data['cluster'] = clustervalue
    data['kube'] = data['cluster']
    ignore_hosts = data.get('ignore_hosts', False)
    pprint(f"Deploying cluster {clustervalue}")
    plan = cluster if cluster is not None else clustervalue
    baremetal_iso = data.get('baremetal_iso', False)
    baremetal_hosts = data.get('baremetal_hosts', [])
    sslip = data.get('sslip')
    domain = data.get('domain')
    data['original_domain'] = domain
    version = data.get('version')
    tag = data.get('tag')
    if str(tag) == '4.1':
        tag = '4.10'
        data['tag'] = tag
    default_sc = False
    if which('oc') is None:
        get_oc()
    for sc in yaml.safe_load(os.popen('oc get sc -o yaml').read())['items']:
        if 'annotations' in sc['metadata']\
           and 'storageclass.kubernetes.io/is-default-class' in sc['metadata']['annotations']\
           and sc['metadata']['annotations']['storageclass.kubernetes.io/is-default-class'] == 'true':
            pprint(f"Using default class {sc['metadata']['name']}")
            default_sc = True
    if not default_sc:
        error("Default Storage class not found. Leaving...")
        sys.exit(1)
    kubeconfig = os.environ.get('KUBECONFIG')
    kubeconfigdir = os.path.dirname(kubeconfig) if kubeconfig is not None else os.path.expanduser("~/.kube")
    kubeconfig = os.path.basename(kubeconfig) if kubeconfig is not None else 'config'
    if yaml.safe_load(os.popen('oc get crd hostedclusters.hypershift.openshift.io -o yaml 2>/dev/null').read()) is None:
        warning("Hypershift not installed. Installing it for you")
        if which('podman') is None:
            error("Please install podman first in order to install hypershift")
            sys.exit(1)
        hypercmd = f"podman pull {data['hypershift_image']}"
        call(hypercmd, shell=True)
        hypercmd = f"podman run -it --rm --entrypoint=/usr/bin/hypershift -e KUBECONFIG=/k/{kubeconfig}"
        hypercmd += f" -v {kubeconfigdir}:/k {data['hypershift_image']} install"
        call(hypercmd, shell=True)
        sleep(120)
    data['basedir'] = '/workdir' if container_mode() else '.'
    cluster = data.get('cluster')
    namespace = data.get('namespace')
    clusterdir = os.path.expanduser(f"~/.kcli/clusters/{cluster}")
    if os.path.exists(clusterdir):
        error(f"Please remove existing directory {clusterdir} first...")
        sys.exit(1)
    supported_data = yaml.safe_load(os.popen("oc get cm/supported-versions -o yaml -n hypershift").read())['data']
    supported_versions = supported_versions = supported_data['supported-versions']
    versions = yaml.safe_load(supported_versions)['versions']
    if str(tag) not in versions:
        error(f"Invalid tag {tag}. Choose between {','.join(versions)}")
        sys.exit(1)
    api_ip = data.get('api_ip')
    if api_ip is None:
        api_url = os.popen("oc whoami --show-server").read()
        api_domain = urlparse(api_url).hostname
        api_ip = socket.getaddrinfo(api_domain, 6443, proto=socket.IPPROTO_TCP)[0][4][0]
        data['api_ip'] = api_ip
    pprint(f"Using {api_ip} as ip to join management cluster api")
    pub_key = data.get('pub_key')
    pull_secret = pwd_path(data.get('pull_secret'))
    pull_secret = os.path.expanduser(pull_secret)
    if not os.path.exists(pull_secret):
        error(f"Missing pull secret file {pull_secret}")
        sys.exit(1)
    data['pull_secret'] = re.sub(r"\s", "", open(pull_secret).read())
    pub_key = data.get('pub_key') or get_ssh_pub_key()
    keys = data.get('keys', [])
    if pub_key is None:
        if keys:
            warning("Using first key from your keys array")
            pub_key = keys[0]
        else:
            error("No usable public key found, which is required for the deployment. Create one using ssh-keygen")
            sys.exit(1)
    pub_key = os.path.expanduser(pub_key)
    if pub_key.startswith('ssh-'):
        data['pub_key'] = pub_key
    elif os.path.exists(pub_key):
        data['pub_key'] = open(pub_key).read().strip()
    else:
        error(f"Publickey file {pub_key} not found")
        sys.exit(1)
    ingress_ip = data.get('ingress_ip')
    cidr = '192.168.122.0/24'
    if config.type in virtplatforms:
        if ingress_ip is None:
            network = data.get('network')
            networkinfo = k.info_network(network)
            if config.type == 'kvm' and networkinfo['type'] == 'routed':
                cidr = networkinfo['cidr']
                ingress_index = 3 if ':' in cidr else -4
                ingress_ip = str(ip_network(cidr)[ingress_index])
                warning(f"Using {ingress_ip} as ingress_ip")
                data['ingress_ip'] = ingress_ip
            elif config.type == 'kubevirt':
                selector = {'kcli/plan': plan, 'kcli/role': 'worker'}
                service_type = "LoadBalancer" if k.access_mode == 'LoadBalancer' else 'NodePort'
                ingress_ip = k.create_service(f"{cluster}-ingress", k.namespace, selector, _type=service_type,
                                              ports=[80, 443], openshift_hack=True)
                if ingress_ip is None:
                    error("Couldnt gather an ingress_ip from your specified network")
                    sys.exit(1)
                else:
                    pprint(f"Using kubernetes service ingress_ip {ingress_ip}")
                    data['ingress_ip'] = ingress_ip
                    data['kubevirt_ingress_service'] = True
            else:
                error("You need to define ingress_ip in your parameters file")
                sys.exit(1)
        virtual_router_id = None
        if data.get('virtual_router_id') is None:
            virtual_router_id = hash(cluster) % 254 + 1
            data['virtual_router_id'] = virtual_router_id
            pprint(f"Using keepalived virtual_router_id {virtual_router_id}")
        ipv6 = True if ':' in cidr else False
        data['ipv6'] = ipv6
    if sslip and config.type in virtplatforms:
        data['domain'] = '%s.sslip.io' % ingress_ip.replace('.', '-').replace(':', '-')
        pprint(f"Setting domain to {domain}")
        ignore_hosts = False
    assetsdata = data.copy()
    if version == 'cluster':
        release_image = os.popen("oc get clusterversion version -o jsonpath={'.status.history[-1].image'}").read()
        version = os.popen("oc get clusterversion version -o jsonpath={'.status.history[-1].version'}").read()
        minor = version[:3].replace('.', '')
        image = f'rhcos{minor}'
        data['image'] = image
    else:
        if os.path.exists('openshift-install'):
            if same_release_images(version=version, tag=tag, pull_secret=pull_secret):
                pprint("Reusing matching openshift-install")
            else:
                pprint("Removing old openshift-install")
                os.remove('openshift-install')
        if which('openshift-install') is None:
            if version in ['ci', 'nightly']:
                nightly = version == 'nigthly'
                run = get_ci_installer(pull_secret, tag=tag, nightly=nightly)
            elif version == 'dev-preview':
                run = get_downstream_installer(devpreview=True, tag=tag, pull_secret=pull_secret)
            else:
                run = get_downstream_installer(tag=tag, pull_secret=pull_secret)
            if run != 0:
                error("Couldn't download openshift-install")
                sys.exit(run)
            pprint("Move downloaded openshift-install somewhere in your PATH if you want to reuse it")
        elif not os.path.exists('openshift-install'):
            warning("Using existing openshift-install found in your PATH")
        INSTALLER_VERSION = get_installer_version()
        pprint(f"Using installer version {INSTALLER_VERSION}")
        release_image = os.popen("openshift-install version | grep 'release image' | cut -f3 -d' '").read().strip()
        image = data.get('image')
        if image is None:
            image_type = 'openstack' if data.get('kvm_openstack', True) and config.type == 'kvm' else config.type
            region = config.k.region if config.type == 'aws' else None
            image_url = get_installer_rhcos(_type=image_type, region=region, arch=arch)
            if platform in ['aws', 'gcp']:
                image = image_url
            else:
                image = os.path.basename(os.path.splitext(image_url)[0])
                if platform == 'ibm':
                    image = image.replace('.', '-').replace('_', '-').lower()
                images = [v for v in k.volumes() if image in v]
                if not images:
                    result = config.handle_host(pool=config.pool, image=image, download=True, update_profile=False,
                                                url=image_url, size=data.get('kubevirt_disk_size'))
                    if result['result'] != 'success':
                        sys.exit(1)
            pprint(f"Using image {image}")
            data['image'] = image
        else:
            pprint(f"Checking if image {image} is available")
            images = [v for v in k.volumes() if image in v]
            if not images:
                error(f"Missing {image}. Indicate correct image in your parameters file...")
                sys.exit(1)
    assetsdata['release_image'] = release_image
    if not os.path.exists(clusterdir):
        os.makedirs(clusterdir)
        os.mkdir(f"{clusterdir}/auth")
        with open(f"{clusterdir}/kcli_parameters.yml", 'w') as p:
            installparam = overrides.copy()
            installparam['plan'] = plan
            installparam['cluster'] = cluster
            installparam['kubetype'] = 'hypershift'
            installparam['api_ip'] = api_ip
            if ingress_ip is not None:
                installparam['ingress_ip'] = ingress_ip
            if virtual_router_id is not None:
                installparam['virtual_router_id'] = virtual_router_id
            installparam['image'] = image
            installparam['ipv6'] = ipv6
            installparam['original_domain'] = data['original_domain']
            yaml.safe_dump(installparam, p, default_flow_style=False, encoding='utf-8', allow_unicode=True)
    copy2(f'{kubeconfigdir}/{kubeconfig}', f"{clusterdir}/kubeconfig.base")
    assetsdata['cidr'] = cidr
    pprint("Creating control plane assets")
    cmcmd = f"oc create ns {namespace} -o yaml --dry-run=client | oc apply -f -"
    call(cmcmd, shell=True)
    icsps = yaml.safe_load(os.popen('oc get imagecontentsourcepolicies -o yaml').read())['items']
    if icsps:
        imagecontentsources = []
        for icsp in icsps:
            for mirror_spec in icsp['spec']['repositoryDigestMirrors']:
                source, mirror = mirror_spec['source'], mirror_spec['mirrors'][0]
                imagecontentsources.append({'source': source, 'mirror': mirror})
        assetsdata['imagecontentsources'] = imagecontentsources
    manifestsdir = pwd_path("manifests")
    if os.path.exists(manifestsdir) and os.path.isdir(manifestsdir):
        manifests = []
        for f in glob(f"{manifestsdir}/*.y*ml"):
            mc_name = os.path.basename(f).replace('.yaml', '').replace('.yml', '')
            mc_data = yaml.safe_load(open(f))
            if mc_data.get('kind', 'xx') == 'MachineConfig':
                pprint(f"Injecting manifest {f}")
                mc_data = json.dumps(mc_data)
                manifests.append({'name': mc_name, 'data': mc_data})
        assetsdata['manifests'] = manifests
    assetsfile = config.process_inputfile(cluster, f"{plandir}/assets.yaml", overrides=assetsdata)
    with open(f"{clusterdir}/assets.yaml", 'w') as f:
        f.write(assetsfile)
    cmcmd = f"oc create -f {clusterdir}/assets.yaml"
    call(cmcmd, shell=True)
    assetsdata['clusterdir'] = clusterdir
    console_url = os.popen("oc get route -n openshift-console console -o jsonpath='{.status.ingress[0].host}'").read()
    assetsdata['base_domain'] = console_url.replace('console-openshift-console.apps.', '')
    ignitionscript = config.process_inputfile(cluster, f"{plandir}/ignition.sh", overrides=assetsdata)
    with open(f"{clusterdir}/ignition.sh", 'w') as f:
        f.write(ignitionscript)
    pprint("Waiting before ignition server is usable")
    call(f"until oc -n {namespace}-{cluster} get secret | grep user-data-{cluster} >/dev/null 2>&1 ; do sleep 1 ; done",
         shell=True)
    ignition_worker = f"{clusterdir}/worker.ign"
    open(ignition_worker, 'a').close()
    timeout = 0
    while True:
        if os.path.getsize(ignition_worker) != 0 and 'Token not found' not in open(ignition_worker).read():
            break
        sleep(30)
        timeout += 30
        if timeout > 300:
            error("Timeout trying to retrieve worker ignition")
            sys.exit(1)
        call(f'bash {clusterdir}/ignition.sh', shell=True)
    pprint("Deploying workers")
    if 'name' in data:
        del data['name']
    if baremetal_iso or baremetal_hosts:
        iso_url = handle_baremetal_iso(config, plandir, cluster, data, baremetal_hosts)
        boot_baremetal_hosts(baremetal_hosts, iso_url, overrides=overrides, debug=config.debug)
        data['workers'] = data['workers'] - len(baremetal_hosts)
    if data['workers'] > 0:
        worker_threaded = data.get('threaded', False) or data.get('workers_threaded', False)
        config.plan(plan, inputfile=f'{plandir}/kcli_plan.yml', overrides=data, threaded=worker_threaded)
    if ignore_hosts:
        warning("Not updating /etc/hosts as per your request")
    else:
        update_etc_hosts(cluster, domain, api_ip, ingress_ip)
    kubeconfigpath = f'{clusterdir}/auth/kubeconfig'
    kubeconfig = os.popen(f"oc extract -n {namespace} secret/{cluster}-admin-kubeconfig --to=-").read()
    with open(kubeconfigpath, 'w') as f:
        f.write(kubeconfig)
    kubeadminpath = f'{clusterdir}/auth/kubeadmin-password'
    kubeadmin = os.popen(f"oc extract -n {namespace} secret/{cluster}-kubeadmin-password --to=-").read()
    with open(kubeadminpath, 'w') as f:
        f.write(kubeadmin)
    autoapproverpath = f'{clusterdir}/autoapprovercron.yml'
    autoapprover = config.process_inputfile(cluster, f"{plandir}/autoapprovercron.yml", overrides=data)
    with open(autoapproverpath, 'w') as f:
        f.write(autoapprover)
    call(f"oc apply -f {autoapproverpath}", shell=True)
    if platform in cloudplatforms:
        result = config.plan(plan, inputfile=f'{plandir}/cloud_lb_apps.yml', overrides=overrides)
        if result['result'] != 'success':
            sys.exit(1)
    async_install = data.get('async')
    if async_install or which('openshift-install') is None:
        success(f"Kubernetes cluster {cluster} deployed!!!")
        info2(f"export KUBECONFIG=$HOME/.kcli/clusters/{cluster}/auth/kubeconfig")
        info2("export PATH=$PWD:$PATH")
    else:
        installcommand = f'openshift-install --dir={clusterdir} --log-level={log_level} wait-for install-complete'
        installcommand = ' || '.join([installcommand for x in range(retries)])
        pprint("Launching install-complete step. It will be retried extra times to handle timeouts")
        run = call(installcommand, shell=True)
        if run != 0:
            error("Leaving environment for debugging purposes")
            error(f"You can delete it with kcli delete kube --yes {cluster}")
            sys.exit(run)
    os.environ['KUBECONFIG'] = f"{clusterdir}/auth/kubeconfig"
    apps = overrides.get('apps', [])
    overrides['hypershift'] = True
    overrides['cluster'] = cluster
    process_apps(config, clusterdir, apps, overrides)
