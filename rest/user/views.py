import os

import requests
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from user.exceptions import UserAlreadyExists
from user.serializers import UserSerializer

from .models import KuberUser

# Create your views here.


class RegisterView(APIView):
    def post(self, request) -> Response:
        data = request.data
        code = data["code"]
        resp = requests.post(
            "https://github.com/login/oauth/access_token",
            params={
                "client_id": os.getenv("GITHUB_CLIENT_ID"),
                "client_secret": os.getenv("GITHUB_CLIENT_SECRET"),
                "code": code,
            },
            headers={"Accept": "application/json"},
        )
        access_token = resp.json()["access_token"]
        resp = requests.get(
            "https://api.github.com/user",
            headers={
                "Authorization": f"Bearer {access_token}",
                "Accept": "application/vnd.github+json",
            },
        )
        # user_data = resp.json()
        # # username = user_data["login"]
        # # email = user_data["email"]
        # # req_user_data = {"username": username, "email": email}

        # # user = KuberUser()
