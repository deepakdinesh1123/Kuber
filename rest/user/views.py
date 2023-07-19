import json
import logging
import os

import hvac
import jwt
import requests
from django.http import HttpResponse, HttpResponseBadRequest
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import KuberUser


class RegisterView(APIView):
    def __init__(self):
        self.vault_client = hvac.Client(
            url="http://localhost:8200"
        )  # Adjust Vault URL if necessary
        self.vault_token = os.getenv(
            "VAULT_TOKEN"
        )  # Retrieve Vault token from environment variables

    def post(self, request):
        code = request.data.get("code")
        if not code:
            return HttpResponseBadRequest("Authorization code is missing")

        # Exchange the authorization code for an access token
        access_token = self.exchange_code_for_token(code)

        if not access_token:
            return HttpResponseBadRequest("Failed to obtain access token")

        # Get user details using the access token
        user_data = self.get_user_data(access_token)

        if not user_data:
            return HttpResponseBadRequest("Failed to retrieve user data")

        # Extract username and email from user data
        username = user_data.get("login")
        email = user_data.get("email")

        # Create a new KuberUser instance
        user = KuberUser(
            username=username,
            email=email,
            github_username=username,
        )
        user.set_unusable_password()
        user.save()

        jwt_payload = {"access_token": access_token}
        jwt_token = jwt.encode(
            jwt_payload, os.getenv("JWT_SECRET_KEY"), algorithm="HS256"
        )

        # Extract the UUID of the newly registered user
        user_uuid = str(user.id)

        # Send user UUID and access token to HashiCorp Vault
        self.send_to_hashicorp_vault(user_uuid, access_token, username)

        response = Response(
            {"message": "User registered successfully"}, status=status.HTTP_201_CREATED
        )
        response.set_cookie("access_token", jwt_token, max_age=3600)

        return response

    def exchange_code_for_token(self, code):
        response = requests.post(
            "https://github.com/login/oauth/access_token",
            params={
                "client_id": os.getenv("GITHUB_CLIENT_ID"),
                "client_secret": os.getenv("GITHUB_CLIENT_SECRET"),
                "code": code,
            },
            headers={"Accept": "application/json"},
        )
        data = response.json()
        access_token = data.get("access_token")
        return access_token

    def get_user_data(self, access_token):
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Accept": "application/vnd.github+json",
        }
        response = requests.get("https://api.github.com/user", headers=headers)
        user_data = response.json()
        return user_data

    def send_to_hashicorp_vault(self, user_uuid, access_token, username):
        logging.basicConfig(
            filename="app.log",
            level=logging.DEBUG,
            format="%(asctime)s - %(levelname)s - %(message)s",
        )
        logging.debug(self.vault_client.is_authenticated())
        if not self.vault_client.is_authenticated():
            self.vault_client.auth_token(self.vault_token)

        create_response = self.vault_client.secrets.kv.v2.create_or_update_secret(
            path=username, secret={user_uuid: access_token}
        )
        logging.debug(json.dumps(create_response, indent=4, sort_keys=True))
