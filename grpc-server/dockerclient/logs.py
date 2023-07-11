from docker.types.daemon import CancellableStream
from dockerclient.client import cli


def get_container_logs(container_name: str) -> CancellableStream:
    cont = cli.containers.get(container_name)
    logs = cont.logs(stream=True)
    return logs
