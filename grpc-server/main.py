import asyncio

import grpc
from definitions.container_pb2_grpc import add_ContainersServicer_to_server
from definitions.environment_pb2_grpc import add_environmentServicer_to_server
from definitions.files_pb2_grpc import add_FilesServicer_to_server
from definitions.image_pb2_grpc import add_ImagesServicer_to_server
from servicers.container import Container
from servicers.environment import Environment
from servicers.files import File
from servicers.image import Image


async def serve() -> None:
    server = grpc.aio.server()
    add_ContainersServicer_to_server(Container(), server)
    add_ImagesServicer_to_server(Image(), server)
    add_FilesServicer_to_server(File(), server)
    add_environmentServicer_to_server(Environment(), server)
    listener_addr = "[::]:9000"
    server.add_insecure_port(listener_addr)
    await server.start()
    try:
        await server.wait_for_termination()
    except KeyboardInterrupt:
        await server.stop(0)


if __name__ == "__main__":
    asyncio.run(serve())
