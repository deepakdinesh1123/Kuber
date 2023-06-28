import traceback

import definitions.files_pb2 as fil
import definitions.files_pb2_grpc as fil_grpc
from docker.errors import NotFound
from dockerclient import container, files
from utils.logger import log_error


class File(fil_grpc.FilesServicer):
    def copyFileToContainer(self, request, context):
        try:
            res = files.upsert_file(
                container_name=request.container_name,
                path=request.path,
                file_name=request.file_name,
                file_content=request.file_content,
            )
            return fil.CopyResponse(success=res)
        except Exception:
            log_error(traceback.format_exc())
            return fil.CopyResponse(success=False)

    def getFile(self, request, context):
        try:
            res = files.get_file(
                container_name=request.container_name,
                file_name=request.file_name,
                path=request.path,
            )
        except NotFound:
            yield fil.FilesResponse(line="Container not found")
            return
        for line in res.output:
            yield fil.FilesResponse(line=line)
