from uuid import uuid4

from django.contrib.postgres.fields import ArrayField
from django.db import models
from environment.models import DockerEnvironment
from user.models import KuberUser

ENV_CHOICES = [("docker", "docker"), ("compose", "docker-compose")]


# Create your models here.
class Containers(models.Model):
    ID = models.UUIDField(primary_key=True, default=uuid4)
    file = models.CharField(max_length=10, choices=ENV_CHOICES)
    environment = models.ForeignKey(
        to=DockerEnvironment,
        on_delete=models.CASCADE,
        to_field="env_id",
        related_name="+",
    )
    config = models.JSONField(name="config")
    continer_ids = ArrayField(models.CharField(max_length=100), name="container_ids")
    created_by = models.ForeignKey(
        to=KuberUser, on_delete=models.CASCADE, to_field="id", related_name="+"
    )
