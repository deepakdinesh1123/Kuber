import definitions.execute_pb2_grpc as exe_grpc


class Execute(exe_grpc.ExecuteServicer):
    def executeCommand(self, request, context):
        return super().executeCommand(request, context)
