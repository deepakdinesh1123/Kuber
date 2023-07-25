from environment.models import Environment
from rest_framework import serializers
from user.serializers import CreatorSerializer


class DockerEnvironmentSerializer(serializers.ModelSerializer):
    creator = CreatorSerializer()

    class Meta:
        model = Environment
        fields = ["env_id", "env_name", "creator", "created_at", "config"]
