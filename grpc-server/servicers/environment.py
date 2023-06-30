import traceback

import definitions.environment_pb2 as env_pb2
import definitions.environment_pb2_grpc as env_pb2_grpc
import grpc
from dockerclient import environment


class Environment(env_pb2_grpc.environmentServicer):
    def createEnvironment(self, request, context: grpc.aio.ServicerContext):
        try:
            created = environment.create_environment(
                name=request.name,
                config=request.config,
                files=request.files,
                env_type=request.type,
                project_name=request.project_name,
                tag=request.tag,
                images=request.images,
            )
            if not created:
                return env_pb2.EnvCreationResponse(
                    message="Container could not be created", success=False
                )
            return env_pb2.EnvCreationResponse(
                message="Container created", success=True
            )
        except Exception as e:
            traceback.print_exc()
            print(str(e))
