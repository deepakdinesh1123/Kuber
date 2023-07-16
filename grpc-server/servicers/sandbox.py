import traceback

import definitions.sandbox_pb2 as sbx_pb2
import definitions.sandbox_pb2_grpc as sbx_pb2_grpc
import grpc
from dockerclient import environment


class Sandbox(sbx_pb2_grpc.SandboxServicer):
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
                return sbx_pb2.SbxCreationResponse(
                    message="Container could not be created", success=False
                )
            return sbx_pb2.sbxCreationResponse(
                message="Container created", success=True
            )
        except Exception as e:
            traceback.print_exc()
            print(str(e))
