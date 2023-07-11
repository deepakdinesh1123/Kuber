import json
import traceback

from django.shortcuts import render
from grpc_client.environment import create_environment
from rest_framework import status
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from utils.logger import log_debug, log_error
from utils.response import get_api_response

from .models import Environment, Sandbox
from .serializers import DockerEnvironmentSerializer


# Create your views here.
class DockerRegistry(APIView):
    parser_classes = [IsAuthenticated]

    # Choose a Registry serivce that provides
    # option to create repos using REST API
    def post(self, request):
        pass

    def get(self, request):
        pass


class DockerImage(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        pass


class EnvironmentView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request: Request, action: str, *args, **kwargs) -> Response:
        user = request.user

        if action == "getEnvironments":
            try:
                envs = Environment.objects.filter(creator=user)
                serializer = DockerEnvironmentSerializer(envs, many=True)
            except Exception as e:
                return get_api_response(str(e), status=400, success=False)
            return get_api_response(serializer.data, status=200, success=True)

    def post(self, request: Request, action: str, *args, **kwargs) -> Response:
        user = request.user
        data = request.data
        log_debug(data)
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

        if action == "start":
            env_id = data["env_id"]
            try:
                env = Environment.objects.get(env_id=env_id)
            except Exception:
                return get_api_response(
                    "Environment does not exist", status=400, success=False
                )
            resp = create_environment(
                name=env.env_name,
                tag="1.0",
                config=env.config,
                images=env.images,
                type=env.type,
                files=env,
                projectName=data["project_name"],
            )

            if resp is None:
                raise

    def get_permissions(self):
        if self.request.method == "DELETE":
            self.permission_classes = [IsAuthenticated, IsAdminUser]
        return super().get_permissions()


class Machine(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request: Request, action: str, *args, **kwargs) -> Response:
        if action == "getMachine":
            data = {"host": "localhost", "port": 9000}
            return get_api_response(data, 200, True)

    def post(self, request: Request, *args, **kwargs) -> Response:
        pass
