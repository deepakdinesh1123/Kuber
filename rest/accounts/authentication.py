import os

import jwt
from accounts.models import User
from django.conf import settings
from django.contrib.auth.models import AnonymousUser
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed


class JWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.headers.get("Authorization")
        if not auth_header:
            raise AuthenticationFailed("Token not provided")

        try:
            token = auth_header.split()[
                1
            ]  # Extract the token from the "Bearer <token>" format
            # Verify and decode the JWT token using the secret key
            payload = jwt.decode(
                token, os.getenv("JWT_SECRET_KEY"), algorithms=["HS256"]
            )
            user = User.objects.get(id=payload["user_id"])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Token has expired.")
        except jwt.InvalidTokenError:
            raise AuthenticationFailed("Invalid token.")
        except User.DoesNotExist:
            raise AuthenticationFailed("No user found for this token.")

        # Set the user object to request.user
        return (user, token)  # Return a tuple of (user, token)

    def authenticate_header(self, request):
        return "Bearer"


class ResourceAccessAuthentication(BaseAuthentication):
    """
    This Authentication class is used to allow users to access resources
    that have an option of being either public or private
    """

    def authenticate(self, request):
        auth_header = request.headers.get("Authorization")
        if not auth_header:
            return (AnonymousUser(), None)

        try:
            token = auth_header.split()[
                1
            ]  # Extract the token from the "Bearer <token>" format
            # Verify and decode the JWT token using the secret key
            payload = jwt.decode(
                token, os.getenv("JWT_SECRET_KEY"), algorithms=["HS256"]
            )
            user = User.objects.get(id=payload["user_id"])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Token has expired.")
        except jwt.InvalidTokenError:
            raise AuthenticationFailed("Invalid token.")
        except User.DoesNotExist:
            raise AuthenticationFailed("No user found for this token.")

        # Set the user object to request.user
        return (user, token)  # Return a tuple of (user, token)

    def authenticate_header(self, request):
        return "Bearer"
