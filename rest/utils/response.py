from typing import Any

from rest_framework.response import Response


def get_api_response(data: Any, status: int, success: bool) -> Response:
    response = {"success": success, "data": data}
    return Response(response, status)
