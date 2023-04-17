from django.db import IntegrityError
from rest_framework import serializers

from .exceptions import UserAlreadyExists
from .models import KuberUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = KuberUser
        fields = ["id", "username", "email", "password"]

    def create(self, validated_data):
        try:
            user = KuberUser.objects.create(
                email=validated_data["email"], username=validated_data["username"]
            )
            user.set_password(validated_data["password"])
            user.save()
        except IntegrityError:
            raise UserAlreadyExists
        return user
