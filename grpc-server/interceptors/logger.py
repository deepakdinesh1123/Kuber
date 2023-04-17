import logging

import grpc

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class LoggerInterceptor(grpc.ServerInterceptor):
    def __init__(self):
        def abort(ignored_request, context):
            context.abort(grpc.StatusCode.UNAUTHENTICATED, "Invalid signature")

        self._abortion = grpc.unary_unary_rpc_method_handler(abort)

    def intercept_service(self, continuation, handler_call_details):
        logger.info(f"Request: {handler_call_details.invocation_metadata}")
        try:
            response = continuation(handler_call_details)
            logger.info(f"Response: {response}")
            return response
        except Exception as e:
            logger.info(f"Error: {e}")
