# middleware.py
import json

from django.utils.deprecation import MiddlewareMixin
from utils.logger import log_info


class RequestResponseLoggingMiddleware(MiddlewareMixin):
    def process_request(self, request):
        log_info(f"Request: {request.method} {request.path} {request.body}")

    def process_response(self, request, response):
        response_body = response.content.decode("utf-8")
        try:
            response_body = json.loads(response_body)
        except ValueError:
            pass

        log_info(f"Response: {response.status_code} ")
        return response
