from typing import Generator

from docker import errors
from docker.models.containers import Container
from dockerclient.client import cli


def create_container(name: str, image: str) -> Generator[str, None, None]:
    container = cli.containers.run(name=name, image=image, detach=True, tty=True)
    return container.logs(stream=True)


def get_container(name: str) -> Container:
    try:
        container = cli.containers.get(name)
        return container
    except errors.NotFound:
        return None


def copy_file_to_container(name: str, path: str, file: bytes) -> bool:
    container = get_container(name)
    container.put_archive(path, file)
    return True
