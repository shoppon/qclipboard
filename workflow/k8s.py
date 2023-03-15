import sys


class Application:
    namespace = 'openstack'
    components = []


class Component:
    app_name = None
    containers = []
    label = None


class Deployment(Component):
    deployment = None


class DaemonSet(Component):
    pass


class Job(Component):
    pass


class StatefulSet(Component):
    pass


class Fluentd(Deployment):
    name = 'internal'
    containers = ['httpd']


class Fluent(Application):
    name = 'fluentd'
    components = [Fluentd]


class CinderApi(Deployment):
    name = 'api'
    deployment = 'cinder-api'
    containers = ['cinder-api']


class CinderVolume(Deployment):
    name = 'volume'
    deployment = 'cinder-volume'
    containers = ['cinder-volume']


class CinderScheuler(Deployment):
    name = 'scheduler'
    deployment = 'cinder-scheduler'
    containers = ['cinder-scheduler']


class CinderDashboard(Deployment):
    name = 'dashboard'
    deployment = 'cinder-dashboard'
    containers = ['cinder-dashboard']


class CinderDashboardAPI(Deployment):
    name = 'cinder-dashboard-api'
    deployment = 'cinder-dashboard-api'
    containers = ['cinder-dashboard-api']


class Cinder(Application):
    name = 'cinder'
    components = [CinderApi, CinderVolume, CinderScheuler, CinderDashboardAPI]


class CinderDashboard(Application):
    name = 'cinder-dashboard'
    components = [CinderDashboard]


class NovaApi(Deployment):
    name = 'os-api'
    deployment = 'nova-api'
    containers = ['nova-osapi']


class NovaCompute(DaemonSet):
    name = 'compute'
    containers = ['nova-compute']


class NovaScheduler(Deployment):
    name = 'scheduler'
    containers = ['nova-scheduler']


class Nova(Application):
    name = 'nova'
    components = [NovaApi, NovaCompute, NovaScheduler]


class Libvirt(DaemonSet):
    name = 'libvirt'
    containers = ['libvirt']


class LibvirtApp(Application):
    name = 'libvirt'
    components = [Libvirt]


class CephMgr(Deployment):
    name = 'mgr'
    deployment = 'ceph-mgr'
    containers = ['ceph-mgr']


class CephMonitor(DaemonSet):
    name = 'mon'
    containers = ['ceph-mon']


class CephOSD(DaemonSet):
    name = 'osd'
    containers = ['osd-create-pod']


class Ceph(Application):
    name = 'ceph'
    namespace = 'ceph'
    components = [CephMgr, CephMonitor, CephOSD]


class Busybox(Deployment):
    name = 'busybox'
    containers = ['busybox-openstack']


class BusyboxApp(Application):
    name = 'busybox'
    components = [Busybox]


class MariaDB(Deployment):
    name = 'server'
    containers = ['mariadb']


class MariaDBApp(Application):
    name = 'mariadb'
    components = [MariaDB]


class RabbitMQ(StatefulSet):
    name = 'server'
    containers = ['rabbitmq']


class RabbitMQApp(Application):
    name = 'rabbitmq'
    components = [RabbitMQ]


class NodeSmartMonCollector(DaemonSet):
    name = 'metrics'
    containers = ['smartmon-collector']


class NodeScriptCollector(DaemonSet):
    name = 'metrics'
    containers = ['node-script-collector']


class NodeExporter(Application):
    name = 'node_exporter'
    components = [NodeSmartMonCollector, NodeScriptCollector]


class BenchmarkJob(Job):
    name = 'benchmark'
    containers = ['benchmark']


class BenchmarkCleanJob(Job):
    name = 'benchmark-clean'
    containers = ['benchmark-clean']


class BenchmarkWarmupJob(Job):
    name = 'benchmark-warmup'
    containers = ['benchmark-warmup']


class BenchmarkWorker(StatefulSet):
    name = 'benchmark-worker'
    containers = ['benchmark-worker']


class Hulk(Application):
    name = 'hulk'
    components = [BenchmarkJob, BenchmarkCleanJob, BenchmarkWarmupJob,
                  BenchmarkWorker]


class CoasterAll(StatefulSet):
    name = 'all'
    containers = ['coaster-other', 'coaster-api', 'coaster-conductor']


class Coaster(Application):
    name = 'coaster'
    components = [CoasterAll]


class Golem(Deployment):
    name = 'golem'
    containers = ['golem']


class Alpaca(Deployment):
    name = 'alpaca'


class Backup(Deployment):
    name = 'rbd-backup'
    app_name = 'cinder'
    containers = ['cinder-backup-rbd']


class Thor(Application):
    name = 'thor'
    namespace = 'thor'
    components = [Alpaca, Golem, Backup]


class Manul(Deployment):
    name = 'manul'
    containers = ['manul']


class ManagerNode(DaemonSet):
    name = 'manager'
    containers = ['alcubierre-manager']


class TargetNode(DaemonSet):
    name = 'target'
    containers = ['alcubierre-target']


class ExporterNode(DaemonSet):
    name = 'exporter'
    containers = ['alcubierre-exporter']


class Alcubierre(Application):
    name = 'alcubierre'
    namespace = 'alcubierre'
    components = [Manul, ManagerNode, TargetNode, ExporterNode]


class MinIO(Deployment):
    name = 'minio'
    deployment = 'minio'
    containers = ['minio']


class Openvswitchd(DaemonSet):
    name = 'openvswitch-vswitchd'
    containers = ['openvswitch-vswitchd']


class Openvswitch(Application):
    name = 'openvswitch'
    namespace = 'openstack'
    components = [Openvswitchd]


class NeutronServer(Deployment):
    name = 'server'
    deployment = 'neutron-server'
    containers = ['neutron-server']


class NeutronMetadataAgent(DaemonSet):
    name = 'metadata-agent'
    containers = ['neutron-metadata-agent']


class Neutron(Application):
    name = 'neutron'
    namespace = 'openstack'
    components = [NeutronServer, NeutronMetadataAgent]


class PyChatGPT(Deployment):
    name = 'pychatgpt'
    containers = ['pychatgpt']


class PyChatGPTApp(Application):
    name = 'pychatgpt'
    namespace = 'pychatgpt'
    components = [PyChatGPT]


class ECPDashboardAPI(Deployment):
    name = 'api'
    containers = ['ecp-dashboard-api']


class ECP(Application):
    name = 'ecp-dashboard-api'
    namespace = 'ems'
    components = [ECPDashboardAPI]


def inheritors(klass):
    subclasses = set()
    work = [klass]
    while work:
        parent = work.pop()
        for child in parent.__subclasses__():
            if child not in subclasses:
                subclasses.add(child)
                work.append(child)
    return subclasses


def build_get_cmd(namespace, label, resource='po'):
    return (f'kubectl -n {namespace} get {resource} -l "{label}" -owide')


def build_delete_cmd(namespace, label, resource='po'):
    return (f'kubectl -n {namespace} delete {resource} -l "{label}"')


def build_describe_cmd(namespace, label, index,
                       resource='po'):
    return (f'kubectl describe po -n {namespace} '
            f'$(kubectl -n {namespace} get {resource} -l "{label}" '
            f'--no-headers -o jsonpath="{{.items[{index}].metadata.name}}")')


def build_logs_cmd(namespace, label, container=None, host=False):
    cmd = (f'for p in $(kubectl -n {namespace} get po -owide -l "{label}"'
           f' --no-headers -o custom-columns=":metadata.name" ')
    if host:
        cmd += "--field-selector spec.nodeName=$host "
    cmd += f");do kubectl -n {namespace} logs "
    if container:
        cmd += f"-c {container} "
    cmd += "$p;done"
    return cmd


def build_tail_cmd(namespace, label, container=None, index=None, host=False):
    cmd = (f'kubectl -n {namespace} logs '
           f'$(kubectl -n {namespace} get po -owide -l "{label}" '
           f'--no-headers -o jsonpath="{{.items[{index}].metadata.name}}" ')
    if host:
        cmd += "--field-selector spec.nodeName=$host "
    cmd += ") -f --tail 20 "
    if container:
        cmd += f"-c {container} "
    return cmd


def build_exec_cmd(namespace, label, index=None, container=None, host=False):
    cmd = (f'kubectl exec -it -n {namespace} '
           f'$(kubectl -n {namespace} get po -owide -l "{label}" ')
    if index is not None:
        cmd += f'--no-headers -o jsonpath="{{.items[{index}].metadata.name}}" '
    if host:
        cmd += "--field-selector spec.nodeName=$host "
    cmd += ") "
    if container:
        cmd += f"-c {container} "
    cmd += "-- bash"
    return cmd


def build_scale_cmd(namespace, deployment):
    return (f"kubectl -n {namespace} scale deployment "
            f"{deployment} --replicas=")


def generate_cmds():
    cmds = {}
    applications = inheritors(Application)
    for app in applications:
        for component in app.components:
            app_name = component.app_name or app.name
            label = component.label or f"application={app_name},component={component.name}"
            get_cmd = build_get_cmd(app.namespace, label)
            cmds['get_' + component.__name__] = get_cmd

            delete_cmd = build_delete_cmd(app.namespace, label)
            cmds['delete_' + component.__name__] = delete_cmd

            host = issubclass(component, DaemonSet)
            index = "$A"
            for c in component.containers:
                exec_cmd = build_exec_cmd(
                    app.namespace, label, index, c, host)
                cmds['exec_' + component.__name__ +
                     '_' + c + '_' + str(index)] = exec_cmd

                logs_cmd = build_logs_cmd(app.namespace, label, c, host)
                cmds['logs_' + component.__name__ +
                     '_' + c + '_' + str(index)] = logs_cmd

                tail_cmd = build_tail_cmd(app.namespace, label, c, index, host)
                cmds['tail_' + component.__name__ +
                     '_' + c + '_' + str(index)] = tail_cmd

            describe_cmd = build_describe_cmd(app.namespace, label, index)
            cmds['describe_' + component.__name__ +
                 '_' + str(index)] = describe_cmd

            if issubclass(component, Deployment):
                scale = build_scale_cmd(app.namespace, component.name)
                cmds['scale_' + component.__name__] = scale

            if issubclass(component, Job):
                rerun = (f"kubectl -n {app.namespace} get job {component.name} -o json | "
                         "jq 'del(.spec.selector)' | jq 'del(.spec.template.metadata.labels)' | "
                         "kubectl replace --force -f -")
                cmds['rerun_' + component.__name__] = rerun

                delete = f"kubectl -n {app.namespace} delete job {component.name}"
                cmds['delete_job' + component.__name__] = delete

                describe = (f"kubectl -n {app.namespace} describe job "
                            f"{component.name}")
                cmds['describe_job' + component.__name__] = describe

                job = f"kubectl -n {app.namespace} get job {component.name}"
                cmds['get_job_' + component.__name__] = job
    return cmds


__cmds = generate_cmds()
for cmd in __cmds:
    setattr(sys.modules[__name__], cmd, __cmds[cmd])
