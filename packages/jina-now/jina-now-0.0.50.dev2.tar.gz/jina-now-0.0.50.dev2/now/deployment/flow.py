import os.path
import pathlib
import tempfile
from multiprocessing import Process
from time import sleep
from typing import Dict

from jina import Flow
from jina.clients import Client
from kubernetes import client as k8s_client
from kubernetes import config
from yaspin.spinners import Spinners

from now.cloud_manager import is_local_cluster
from now.constants import DEFAULT_FLOW_NAME
from now.deployment.deployment import apply_replace, cmd, deploy_wolf
from now.log import time_profiler, yaspin_extended
from now.utils import sigmap, write_env_file, write_flow_file

cur_dir = pathlib.Path(__file__).parent.resolve()
MAX_WAIT_TIME = 1800


def batch(data_list, n=1):
    l = len(data_list)
    for ndx in range(0, l, n):
        yield data_list[ndx : min(ndx + n, l)]


def wait_for_lb(lb_name, ns):
    config.load_kube_config()
    v1 = k8s_client.CoreV1Api()
    while True:
        try:
            services = v1.list_namespaced_service(namespace=ns)
            ip = [
                s.status.load_balancer.ingress[0].ip
                for s in services.items
                if s.metadata.name == lb_name
            ][0]
            if ip:
                break
        except Exception:
            pass
        sleep(1)
    return ip


def check_pods_health(ns):
    config.load_kube_config()
    v1 = k8s_client.CoreV1Api()
    pods = v1.list_namespaced_pod(ns).items

    for pod in pods:
        try:
            message = pod.status.container_statuses[0].state.waiting.message
        except:
            message = None

        if message and 'Error' in message:
            raise Exception(pod.metadata.name + " " + message)


def wait_for_flow(client, ns):
    wait_time = 0
    while not client.is_flow_ready() and wait_time <= MAX_WAIT_TIME:
        if 'NOW_TESTING' not in os.environ:
            check_pods_health(ns)
        wait_time += 1
        sleep(1)
    if not client.is_flow_ready():
        raise Exception('Flow execution timed out.')


def deploy_k8s(f, ns, tmpdir, kubectl_path):
    k8_path = os.path.join(tmpdir, f'k8s/{ns}')
    with yaspin_extended(
        sigmap=sigmap, text="Convert Flow to Kubernetes YAML", color="green"
    ) as spinner:
        f.to_k8s_yaml(k8_path)
        spinner.ok('🔄')

    # create namespace
    cmd(f'{kubectl_path} create namespace {ns}')

    # deploy flow
    with yaspin_extended(
        Spinners.earth,
        sigmap=sigmap,
        text="Deploy Jina Flow (might take a bit)",
    ) as spinner:
        gateway_host_internal = f'gateway.{ns}.svc.cluster.local'
        gateway_port_internal = 8080
        if is_local_cluster(kubectl_path):
            apply_replace(
                f'{cur_dir}/k8s_backend-svc-node.yml',
                {'ns': ns},
                kubectl_path,
            )
            gateway_host = 'localhost'
            gateway_port = 31080
        else:
            apply_replace(f'{cur_dir}/k8s_backend-svc-lb.yml', {'ns': ns}, kubectl_path)
            gateway_host = wait_for_lb('gateway-lb', ns)
            gateway_port = 8080
        cmd(f'{kubectl_path} apply -R -f {k8_path}')

        client = Client(host=gateway_host, port=gateway_port)
        wait_for_flow(client, ns)
        spinner.ok("🚀")

    return gateway_host, gateway_port, gateway_host_internal, gateway_port_internal


def start_flow_in_process(f):
    def start_flow():
        with f:
            print('flow started in process')
            f.block()

    p1 = Process(target=start_flow, args=())
    p1.daemon = False
    p1.start()


@time_profiler
def deploy_flow(
    deployment_type: str,
    flow_yaml: str,
    env_dict: Dict,
    kubectl_path: str,
):
    """Deploy a Flow on JCloud, Kubernetes, or using Jina Orchestration"""
    # TODO create tmpdir top level and pass it down
    with tempfile.TemporaryDirectory() as tmpdir:
        env_file = os.path.join(tmpdir, 'dot.env')
        write_env_file(env_file, env_dict)

        # hack we don't know if the flow yaml is a path or a string
        if type(flow_yaml) == dict:
            flow_file = os.path.join(tmpdir, 'flow.yml')
            write_flow_file(flow_yaml, flow_file)
            flow_yaml = flow_file

        if os.environ.get('NOW_TESTING', False):
            from dotenv import load_dotenv

            load_dotenv(env_file, override=True)

            f = Flow.load_config(flow_yaml)
            f.gateway_args.timeout_send = -1
            start_flow_in_process(f)

            host = 'localhost'
            client = Client(host=host, port=8080)
            wait_for_flow(client, DEFAULT_FLOW_NAME)
            # host & port
            gateway_host = 'remote'
            gateway_port = 8080
            gateway_host_internal = host
            gateway_port_internal = None  # Since host contains protocol

        elif deployment_type == 'remote':
            flow = deploy_wolf(path=flow_yaml)
            host = flow.endpoints['gateway']
            client = Client(host=host)

            # host & port
            gateway_host = 'remote'
            gateway_port = None
            gateway_host_internal = host
            gateway_port_internal = None  # Since host contains protocol
        else:
            from dotenv import load_dotenv

            load_dotenv(env_file, override=True)
            f = Flow.load_config(flow_yaml)
            (
                gateway_host,
                gateway_port,
                gateway_host_internal,
                gateway_port_internal,
            ) = deploy_k8s(
                f,
                DEFAULT_FLOW_NAME,
                tmpdir,
                kubectl_path=kubectl_path,
            )
            client = Client(host=gateway_host, port=gateway_port)

        if os.path.exists(env_file):
            os.remove(env_file)

    return (
        client,
        gateway_host,
        gateway_port,
        gateway_host_internal,
        gateway_port_internal,
    )
