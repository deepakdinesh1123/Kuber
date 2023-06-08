from environment.models import DockerEnvironment
from rest_framework import serializers


class DockerEnvironmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DockerEnvironment
        fields = ["env_name", "images", "creator", "created_at", "config"]
