from accounts.serializers import CreatorSerializer
from environment.models import DockerImage, Environment, Sandbox
from rest_framework import serializers


class EnvironmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Environment
        fields = "__all__"


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
    class Meta:
        model = Sandbox
        fields = ["name", "sandbox_creator", "user", "containers", "env"]
