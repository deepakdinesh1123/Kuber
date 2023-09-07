import os

import hvac
import jwt
import requests
from django.http import HttpResponse, HttpResponseBadRequest
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from utils.logger import log_debug
from utils.response import get_api_response

from .models import User


class RegisterView(APIView):
    def post(self, request, *args, **kwargs):
        # vault_client = hvac.Client(url=os.getenv("VAULT_URL"))
        # vault_token = os.getenv("VAULT_TOKEN")

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

        # Create a new User instance
        user = User(
            username=username,
            email=email,
            github_username=username,
        )
        user.set_unusable_password()
        user.save()

        # Extract the UUID of the newly registered user
        user_uuid = str(user.id)

        log_debug(f"id {user_uuid}")

        jwt_payload = {"user_id": user_uuid}
        jwt_token = jwt.encode(
            jwt_payload, os.getenv("JWT_SECRET_KEY"), algorithm="HS256"
        )

        log_debug(f"token {jwt_token}")

        # Send user UUID and access token to HashiCorp Vault
        # self.send_to_hashicorp_vault(
        #     vault_client, vault_token, user_uuid, access_token, username
        # )

        response = get_api_response(jwt_token, status=200, success=True)
        return response

    def exchange_code_for_token(self, code):
        response = requests.post(
            os.getenv("GIT_OAUTH_URL"),
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
        response = requests.get(os.getenv("GIT_API_URL"), headers=headers)
        if response.status_code == 200:
            user_data = response.json()
            return user_data  # Return the raw user data
        return None

    def send_to_hashicorp_vault(
        self, vault_client, vault_token, user_uuid, access_token, username
    ):
        if not vault_client.is_authenticated():
            vault_client.auth_token(vault_token)

        vault_client.secrets.kv.v2.create_or_update_secret(
            path=username, secret={user_uuid: access_token}
        )


class PermissionView(APIView):
    pass
