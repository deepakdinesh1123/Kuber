import asyncio

import grpc
from definitions.container_pb2_grpc import add_ContainersServicer_to_server
from definitions.environment_pb2_grpc import add_environmentServicer_to_server
from definitions.execute_pb2_grpc import add_ExecuteServicer_to_server
from definitions.files_pb2_grpc import add_FilesServicer_to_server
from definitions.image_pb2_grpc import add_ImagesServicer_to_server
from definitions.logs_pb2_grpc import add_LogsServicer_to_server
from definitions.retrieve_pb2_grpc import add_DataServiceServicer_to_server
from servicers.container import Container
from servicers.environment import Environment
from servicers.execute import Execute
from servicers.files import File
from servicers.image import Image
from servicers.logs import Logs
from servicers.retrieve import DataServiceServicer

async def serve() -> None:
    server = grpc.aio.server()
    add_ContainersServicer_to_server(Container(), server)
    add_ImagesServicer_to_server(Image(), server)
    add_FilesServicer_to_server(File(), server)
    add_environmentServicer_to_server(Environment(), server)
    add_DataServiceServicer_to_server(DataServiceServicer(), server)
    add_ExecuteServicer_to_server(Execute(), server)
    add_LogsServicer_to_server(Logs(), server)
    listener_addr = "[::]:9000"
    server.add_insecure_port(listener_addr)
    try:
        await server.start()
        print("Server started on port 9000")
    except Exception as e:
        print(str(e))
    try:
        await server.wait_for_termination()
    except KeyboardInterrupt:
        await server.stop(0)


if __name__ == "__main__":
    asyncio.run(serve())
