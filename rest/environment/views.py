import json
import os
import traceback
from django.shortcuts import get_object_or_404
import requests
from accounts.authentication import (
    JWTAuthentication,
    ResourceAccessAuthentication,
)
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from utils.logger import log_debug, log_error, log_info
from utils.response import get_api_response
from .forms import EnvForm
from .models import DockerImage, Environment, Sandbox, ENVIRONMENT_CHOICES
from .serializers import (
    DockerEnvironmentSerializer,
    DockerFileSerializer,
    DockerImageSerializer,
    SandboxSerializer,
    EnvironmentSerializer
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

    def post(self, request: Request, *args, **kwargs) -> Response:
        try:
            config_data = request.data.get("config", "")

            if not config_data.startswith("{") and not config_data.endswith("}"):
                config_data = "{" + config_data + "}"

            try:
                config_dict = json.loads(config_data)
            except json.JSONDecodeError as e:
                return get_api_response("Invalid config format", status=400, success=False)

            request.data["config"] = config_dict
            request.data["creator"] = request.user.id
            serializer = EnvironmentSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()
                return get_api_response("Environment created", status=200, success=True)
            else:
                return get_api_response(serializer.errors, status=400, success=False)
        except Exception as e:
            return get_api_response(str(e), status=500, success=False)

    def delete(self, request: Request, env_id=None, *args, **kwargs) -> Response:
        if env_id:
            try:
                env = get_object_or_404(Environment, env_id=env_id)
                env.delete()
                return get_api_response("Environment deleted", status=204, success=True)
            except Exception as e:
                return get_api_response(str(e), status=500, success=False)
        else:
            return get_api_response("env_id parameter is required", status=400, success=False)

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
    authentication_classes = [JWTAuthentication]

    def post(self, request: Request, env_id=None, *args, **kwargs) -> Response:
        pass

    def get(self, request: Request, *args, **kwargs) -> Response:
        try:
            sandboxes = Sandbox.objects.all()
            serializer = SandboxSerializer(sandboxes, many=True)
            return get_api_response(serializer.data, status=200, success=True)
        except Exception as e:
            return get_api_response(str(e), status=500, success=False)


class FormView(APIView):
    authentication_classes = [JWTAuthentication]

    def get(self, request: Request, *args, **kwargs) -> Response:
        user = request.user
        user_images = DockerImage.objects.filter(created_by=user)
        types = dict(ENVIRONMENT_CHOICES)
        args_list = {
            'image': {
                str(image.id): image.name for image in user_images
            },
            'type': types


        }
        form = EnvForm()
        json_schema = form.generate_json_schema(args_list=args_list)
        return get_api_response(json_schema, status=200, success=True)


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
