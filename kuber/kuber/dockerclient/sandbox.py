import subprocess
from typing import BinaryIO, Generator, List

import namegenerator
from docker import errors
from docker.models.containers import Container
from dockerclient.container import create_container
from dockerclient.image import build_image, check_image_exists
from dockerclient.preprocess.compose import preprocess_compose
from dockerclient.preprocess.dockerfile import preprocess_dockerfile
from utils.formatter import string_to_generator


def check_compose_file_exists(name: str) -> bool:
    # TODO
    pass


def create_sandbox(
    name: str,
    config: dict,
    files: List[BinaryIO],
    env_type: str,
    project_name: str,
    tag: str,
    images: List[str],
) -> Generator[str, None, None]:
    if env_type == "compose":
        file = preprocess_compose(files[0])
        with open(f"/tmp/{name}.yml") as f:
            f.writelines(file)
        process = subprocess.Popen(
            f"docker-compose up -f /tmp/{name}.yml up -p {project_name} -d",
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True,
        )
        stdout, stderr = process.communicate()

        return string_to_generator(stderr)

    if env_type == "docker":
        file = preprocess_dockerfile(files[0])
        container_name = namegenerator.gen()
        if not check_image_exists(images[0], tag):
            build_image(name=images[0], dockerfile=file, tag=tag)
        sandbox_name = f"{name}_{container_name}"
        created = create_container(
            image=f"{images[0]}:{tag}", name=sandbox_name, ports=config.get("ports")
        )
        # upsert_containers(container_name, "admin")
        return created, [sandbox_name]
