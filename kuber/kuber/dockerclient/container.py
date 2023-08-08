from typing import Generator, List

from docker import errors
from docker.models.containers import Container
from dockerclient.client import cli
from dockerclient.network import find_unused_port


def create_container(name: str, image: str, ports: List[int] = None) -> bool:
    try:
        if ports is None:
            cli.containers.run(name=name, image=image, detach=True, tty=True)
        else:
            port_mapping = {f"{cport}/tcp": find_unused_port() for cport in ports}
            print(port_mapping)
            # TODO update port mapping to db
            cli.containers.run(
                name=name, image=image, detach=True, tty=True, ports=port_mapping
            )
    except Exception:
        return False
    return True


def get_container(name: str) -> Container:
    try:
        container = cli.containers.get(name)
        return container
    except errors.NotFound:
        return None


def is_container_running(name: str) -> bool:
    try:
        container = cli.containers.get(name)
        if container.status == "running":
            return True
        else:
            return False
    except errors.NotFound:
        return False
    except errors.APIError:
        return False
