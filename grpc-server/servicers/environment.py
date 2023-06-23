import traceback

import definitions.environment_pb2 as env_pb2
import definitions.environment_pb2_grpc as env_pb2_grpc
import grpc
from dockerclient import environment
from utils.formatter import read_until_newline


class Environment(env_pb2_grpc.environmentServicer):
    async def createEnvironment(self, request, context: grpc.aio.ServicerContext):
        try:
            logs, container_names = environment.create_environment(
                name=request.name,
                config=request.config,
                files=request.files,
                env_type=request.type,
                project_name=request.project_name,
                tag=request.tag,
            )
            line = b""
            for char in logs:
                if char == b"\n":
                    yield env_pb2.EnvCreationResponse(message=line)
                    line = b""
                else:
                    line += char
        except Exception as e:
            traceback.print_exc()
            print(str(e))
