from django.db import IntegrityError
from rest_framework import serializers
from user.exceptions import UserAlreadyExists
from user.models import KuberUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = KuberUser
        fields = ["id", "username", "email"]

    def create(self, validated_data):
        try:
            user = KuberUser.objects.create_user(
                email=validated_data["email"], username=validated_data["username"]
            )
            user.set_password(validated_data["password"])
            user.save()
        except IntegrityError:
            raise UserAlreadyExists
        return user


class CreatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = KuberUser
        fields = ["username"]
