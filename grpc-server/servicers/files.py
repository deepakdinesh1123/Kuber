import definitions.files_pb2 as fil
import definitions.files_pb2_grpc as fil_grpc
from dockerclient import container


class File(fil_grpc.FilesServicer):
    def copyFilesToContainer(self, request_iterator, context):
        for request in request_iterator:
            container.copy_file_to_container(
                name=request.container, path=request.File.name, file=request.File.path
            )
        return fil.CopyResponse(success=True)
