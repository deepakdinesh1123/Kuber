import json
import os
import traceback

import requests
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from user.authentication import JWTAuthentication, ResourceAccessAuthentication
from utils.logger import log_debug, log_error, log_info
from utils.response import get_api_response

from .models import DockerImage, Environment, Sandbox
from .serializers import (
    DockerEnvironmentSerializer,
    DockerFileSerializer,
    DockerImageSerializer,
)


# Create your views here.
class DockerRegistry(APIView):
    parser_classes = [IsAuthenticated]

    # Choose a Registry serivce that provides
    # option to create repos using REST API
    def post(self, request):
        pass

    def get(self, request):
        pass


# class DockerImage(APIView):
#     permission_classes = [IsAuthenticated]

#     def post(self, request):
#         pass


class EnvironmentView(APIView):
    def get(self, request: Request, env_id=None, *args, **kwargs) -> Response:
        if env_id:
            try:
                env = Environment.objects.get(env_id=env_id)
                serializer = DockerEnvironmentSerializer(env, many=False)
                return get_api_response(serializer.data, status=200, success=True)
            except Exception as e:
                return get_api_response(str(e), status=500, success=False)
        else:
            try:
                envs = Environment.objects.all()
                serializer = DockerEnvironmentSerializer(envs, many=True)
            except Exception as e:
                return get_api_response(str(e), status=400, success=False)
            return get_api_response(serializer.data, status=200, success=True)

    def post(self, request: Request, action: str, *args, **kwargs) -> Response:
        user = request.user
        data = request.data
        if action == "create":
            try:
                private = data.get("private", False)
                env = Environment(
                    env_name=data["name"],
                    config=data["config"],
                    images=data["images"],
                    creator=user,
                    private=private,
                    type=data["type"],
                )
                env.save()
                return get_api_response("Environment created", status=200, success=True)
            except Exception as e:
                log_error(traceback.format_exc())
                return get_api_response(str(e), status=400, success=False)

    def get_authenticators(self):
        if self.request.method == "POST":
            self.authentication_classes = [JWTAuthentication]
        return super().get_authenticators()


class Machine(APIView):
    authentication_classes = [JWTAuthentication]

    def get(self, request: Request, *args, **kwargs) -> Response:
        user = request.user
        if user:
            return get_api_response(user.email, status=200, success=True)
        return get_api_response("Failed", status=400, success=False)

    def post(self, request: Request, *args, **kwargs) -> Response:
        pass


class SandboxView(APIView):
    def post(self, request: Request, env_id=None, *args, **kwargs) -> Response:
        Environment.objects.get(env_id=env_id)


@api_view(("POST",))
@authentication_classes((JWTAuthentication,))
def create_image(request: Request, *args, **kwargs) -> Request:
    user = request.user
    data = request.data

    url = f"{os.getenv('EXECUTOR_API_HOST')}/image/build"

    payload = json.dumps(
        {
            "ImageName": data["ImageName"],
            "Dockerfile": data["Dockerfile"],
            "Tag": data["Tag"],
        }
    )
    headers = {"Content-Type": "application/json"}

    response = requests.request("POST", url, headers=headers, data=payload)
    if response.status_code != 200:
        return get_api_response("Could not create image", 500, False)
    resp_data = response.json()
    DockerImage.objects.create(
        name=resp_data["ImageName"], created_by=user, Dockerfile=data["Dockerfile"]
    )
    return get_api_response("Image created", 200, True)


@api_view(("GET",))
@authentication_classes((JWTAuthentication,))
def get_all_images(request: Request, *args, **kwargs) -> Response:
    user = request.user
    log_debug(user.username)
    try:
        images = DockerImage.objects.filter(created_by=user)
        serializer = DockerImageSerializer(images, many=True)
        return get_api_response(serializer.data, status=200, success=True)
    except Exception as e:
        return get_api_response(str(e), status=500, success=False)


@api_view(("GET",))
@authentication_classes((ResourceAccessAuthentication,))
def get_image(request: Request, image_id: int, *args, **kwargs):
    user = request.user
    log_debug(user)
    try:
        image = DockerImage.objects.get(id=image_id)
        serializer = DockerFileSerializer(image, many=False)
        if serializer.data == {}:
            return get_api_response(
                "No image with specified ID", status=404, success=False
            )
        return get_api_response(serializer.data, status=200, success=True)
    except Exception as e:
        return get_api_response(str(e), status=500, success=False)
