from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .exceptions import UserAlreadyExists
from .serializers import UserSerializer

# Create your views here.


class RegisterView(APIView):
    def post(self, request) -> Response:
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            serializer.save()
        except UserAlreadyExists:
            return Response(
                "User with provided email already exists",
                status=status.HTTP_405_METHOD_NOT_ALLOWED,
            )
        resp = Response(serializer.data, status=status.HTTP_201_CREATED)
        resp.set_cookie("logged_in", "True")
        return resp
