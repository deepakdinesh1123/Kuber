import traceback

import definitions.sandbox_pb2 as sbx_pb2
import definitions.sandbox_pb2_grpc as sbx_pb2_grpc
import grpc
from dockerclient import sandbox


class Sandbox(sbx_pb2_grpc.SandboxServicer):
    def create_sandbox(self, request, context: grpc.aio.ServicerContext):
        try:
            created, containers = sandbox.create_sandbox(
                name=request.name,
                config=request.config,
                files=request.files,
                env_type=request.env_type,
                project_name=request.project_name,
                tag=request.tag,
                images=request.images,
            )
            if not created:
                return sbx_pb2.SbxCreationResponse(
                    message="Container could not be created", success=False
                )
            return sbx_pb2.SbxCreationResponse(
                message="Container created", success=True, containers=containers
            )
        except Exception as e:
            traceback.print_exc()
            print(str(e))
