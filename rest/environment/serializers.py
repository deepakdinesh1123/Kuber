from environment.models import Environment
from rest_framework import serializers


class DockerEnvironmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Environment
        fields = ["env_name", "images", "creator", "created_at", "config"]
