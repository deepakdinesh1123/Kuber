from typing import Generator

from docker import errors
from docker.models.containers import Container
from dockerclient.client import cli


def create_container(name: str, image: str) -> bool:
    try:
        cli.containers.run(name=name, image=image, detach=True, tty=True)
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
