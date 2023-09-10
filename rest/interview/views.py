import json
import os
import traceback

import requests
from accounts.authentication import (
    JWTAuthentication,
    ResourceAccessAuthentication,
)
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from drf_yasg import openapi
from environment.models import Environment
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from utils.logger import log_debug, log_error, log_info
from utils.response import get_api_response

from .forms import InterForm
from .models import Interview, default_config
from .serializers import InterviewSerializer

# Create your views here.


class InterviewView(APIView):
    serializer_class = InterviewSerializer
    authentication_classes = [JWTAuthentication]

    def post(self, request: Request, *args, **kwargs) -> Response:
        try:
            config_data = request.data.get("config", "")

            if not config_data.startswith("{") and not config_data.endswith("}"):
                config_data = "{" + config_data + "}"

            try:
                config_dict = json.loads(config_data)
            except json.JSONDecodeError as e:
                return get_api_response(
                    "Invalid config format", status=400, success=False
                )

            if config_data:
                request.data["config"] = config_dict
            else:
                request.data["config"] = default_config()
            request.data["creator"] = request.user.id

            serializer = InterviewSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return get_api_response("Interview created", status=200, success=True)
            else:
                return get_api_response(serializer.errors, status=400, success=False)

        except Exception as e:
            return get_api_response(str(e), status=500, success=False)

    def get(self, request: Request, interview_id=None, *args, **kwargs) -> Response:
        if interview_id:
            try:
                inter = Interview.objects.get(interview_id=interview_id)
                serializer = InterviewSerializer(inter, many=False)
                return get_api_response(serializer.data, status=200, success=True)
            except Exception as e:
                return get_api_response(str(e), status=500, success=False)
        else:
            try:
                inters = Interview.objects.all()
                serializer = InterviewSerializer(inters, many=True)
            except Exception as e:
                return get_api_response(str(e), status=400, success=False)
            return get_api_response(serializer.data, status=200, success=True)

    def delete(self, request: Request, interview_id=None, *args, **kwargs) -> Response:
        if interview_id:
            try:
                inter = get_object_or_404(Interview, interview_id=interview_id)
                inter.delete()
                return get_api_response("Interview deleted", status=200, success=True)
            except Exception as e:
                return get_api_response(str(e), status=500, success=False)
        else:
            return get_api_response(
                "interview_id parameter is required", status=400, success=False
            )


class FormView(APIView):
    # serializer_class = InterviewSerializer
    authentication_classes = [JWTAuthentication]

    def get(self, request: Request, interview_id=None, *args, **kwargs) -> Response:
        user = request.user
        user_envs = Environment.objects.filter(creator=user)
        args_list = {
            "environment": {str(env.env_id): env.env_name for env in user_envs}
        }
        form = InterForm()
        json_schema = form.generate_json_schema(args_list=args_list)
        if interview_id:
            try:
                interview = Interview.objects.get(
                    interview_id=interview_id, creator=user
                )
                properties_to_add_default = [
                    "environment",
                    "name",
                    "problem",
                    "config",
                    "time_limit",
                ]
                log_debug(interview.config)
                for prop in properties_to_add_default:
                    if (
                        prop == "environment"
                    ):  # getattr cant do interview.environment.env_name so separate
                        json_schema["properties"]["environment"][
                            "default"
                        ] = interview.environment.env_name
                        # cant find a better way :)
                    else:
                        json_schema["properties"][prop]["default"] = str(
                            getattr(interview, prop)
                        )
            except Exception as e:
                return get_api_response(str(e), status=500, success=False)
        return get_api_response(json_schema, status=200, success=True)
