# middleware.py
import json

from django.utils.deprecation import MiddlewareMixin
from utils.logger import log_error, log_info


class RequestResponseLoggingMiddleware(MiddlewareMixin):
    def process_request(self, request):
        log_info(f"Request: {request.method} {request.path}")

    # def process_response(self, request, response):
    #     response_body = response.content.decode("utf-8")
    #     log_error(f"Response: {response.status_code} {response_body}")
    #     return response
