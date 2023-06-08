import os

import docker

client = docker.from_env()

client.login(
    username=os.environ.get("DOCKER_HUB_USERNAME"),
    password=os.environ.get("DOCKER_HUB_PASSWORD"),
)
