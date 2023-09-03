from accounts.serializers import CreatorSerializer
from environment.models import DockerImage, Environment, Sandbox
from rest_framework import serializers


class DockerEnvironmentSerializer(serializers.ModelSerializer):
    creator = CreatorSerializer()

    class Meta:
        model = Environment
        fields = ["env_id", "env_name", "creator", "created_at", "config"]


class DockerImageSerializer(serializers.ModelSerializer):
    created_by = CreatorSerializer()

    class Meta:
        model = DockerImage
        fields = ["id", "name", "created_by"]


class DockerFileSerializer(serializers.ModelSerializer):
    created_by = CreatorSerializer()

    class Meta:
        model = DockerImage
        fields = ["id", "name", "created_by", "Dockerfile"]


class SandboxSerializer(serializers.ModelSerializer):
    # sandbox_creator = serializers.CharField(source="sandbox_creator.username")
    # user = serializers.CharField(source="user.username")
    # env = serializers.CharField(source="env.env_name")

    class Meta:
        model = Sandbox
        fields = ["name", "sandbox_creator", "user", "containers", "env"]
