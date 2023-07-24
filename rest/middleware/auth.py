import jwt
from django.conf import settings
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from rest_framework import exceptions

User = get_user_model()


class JWTAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        token = self.get_token_from_request(request)

        if token:
            try:
                payload = jwt.decode(
                    token, settings.JWT_SECRET_KEY, algorithms=["HS256"]
                )
                user = User.objects.get(id=payload["user_id"])
                request.user = user
                request.jwt_payload = payload
            except (jwt.DecodeError, User.DoesNotExist):
                raise exceptions.AuthenticationFailed("Invalid token")

        response = self.get_response(request)
        return response

    def get_token_from_request(self, request):
        authorization_header = request.META.get("HTTP_AUTHORIZATION")

        if authorization_header:
            try:
                auth_type, token = authorization_header.split(" ")
                if auth_type.lower() == "bearer":
                    return token
            except ValueError:
                pass

        return None
