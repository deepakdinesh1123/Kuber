import socket
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


def find_unused_port():
    # Create a socket object
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("localhost", 0))  # Bind to an available port on localhost
    _, port = sock.getsockname()  # Get the allocated port
    sock.close()  # Close the socket

    return port
