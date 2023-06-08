import io
from typing import Generator

from dockerclient.client import cli


def build_image(name: str, dockerfile: bytes, tag: str) -> Generator[str, None, None]:
    docker_file = io.BytesIO(
        dockerfile
    )  # converts the contents of the dockefile string into a File like object
    image_name = f"{name}:{tag}"
    image, logs = cli.images.build(fileobj=docker_file, tag=image_name)
    return logs


def push_image():
    pass
