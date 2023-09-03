from accounts.exceptions import UserAlreadyExists
from accounts.models import User
from django.db import IntegrityError
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]

    def create(self, validated_data):
        try:
            user = User.objects.create_user(
                email=validated_data["email"], username=validated_data["username"]
            )
            user.set_password(validated_data["password"])
            user.save()
        except IntegrityError:
            raise UserAlreadyExists
        return user


class CreatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username"]
