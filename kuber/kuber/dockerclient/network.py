from typing import List

from dockerclient.client import cli


def create_network(name: str) -> str:
    network = cli.networks.create(name=name, driver="bridge")
    return network.name


def list_networks() -> List[str]:
    return cli.networks.list()


def check_network_exists(name: str) -> bool:
    networks = list_networks()
    for network in networks:
        if name == network.name:
            return True
    return False
