import definitions.container_pb2 as container_pb2
import definitions.container_pb2_grpc as container_pb2_grpc
import grpc
from dockerclient import container, network
from dockerclient.client import cli


class Container(container_pb2_grpc.ContainersServicer):
    async def createContainer(self, request, context: grpc.aio.ServicerContext):
        if not network.check_network_exists(name=request.name):
            new_network = network.create_network(name=request.network)  # noqa
            logs = container.create_container(
                name=request.name, image=request.image, network=request.network
            )
            for line in logs:
                yield container_pb2.ContainerCreationResponse(
                    container_created=container_pb2.ContainerCreated(
                        name=request.name, logs=line.decode().strip()
                    )
                )
        else:
            yield container_pb2.ContainerCreationResponse(
                container_error=container_pb2.ContainerCreationError(
                    error="Network with the given name already exists"
                )
            )
