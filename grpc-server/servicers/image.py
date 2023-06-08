import traceback

import definitions.image_pb2 as img
import definitions.image_pb2_grpc as img_grpc
import grpc
from dockerclient import container, image, network


class Image(img_grpc.ImagesServicer):
    async def buildImage(
        self, request, context: grpc.aio.ServicerContext
    ) -> img.ImageBuildResponse:
        try:
            logs = image.build_image(
                name=request.name, dockerfile=request.dockerfile, tag=request.tag
            )
            for line in logs:
                yield img.ImageBuildResponse(
                    success=img.ImageBuildSuccess(
                        name=request.name, logs=line.get("stream") or ""
                    )
                )
        except Exception as e:
            print(e)
            traceback.print_exc()

    async def pushImage(self, request, context):
        return super().pushImage(request, context)
