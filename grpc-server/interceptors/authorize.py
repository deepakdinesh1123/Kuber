import asyncio
import traceback
from typing import Awaitable, Callable

import grpc
from auth.authorize import authorize


class JWTInterceptor(grpc.aio.ServerInterceptor):
    async def intercept_service(
        self,
        continuation: Callable[
            [grpc.HandlerCallDetails], Awaitable[grpc.RpcMethodHandler]
        ],
        handler_call_details: grpc.HandlerCallDetails,
    ) -> grpc.RpcMethodHandler:
        _metadata = dict(handler_call_details.invocation_metadata)
        if _metadata.get("authorization"):
            jwt_token = _metadata["authorization"]
            try:
                authorize(jwt_token)
            except Exception:
                traceback.print_exc()
        return await continuation(handler_call_details)
