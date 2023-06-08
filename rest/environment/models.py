from uuid import uuid4

from django.contrib.postgres.fields import ArrayField
from django.db import models
from user.models import KuberUser, UserRole


# Create your models here.
class DockerEnvironment(models.Model):
    env_id = models.UUIDField(primary_key=True, default=uuid4, name="env_id")
    env_name = models.CharField(max_length=100, unique=True, name="env_name")
    images = ArrayField(models.CharField(max_length=100, name="dockerimage"))
    creator = models.ForeignKey(
        to=KuberUser, related_name="+", to_field="id", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    config = models.JSONField(name="config", default=dict)


class UserDockerEnvironments(models.Model):
    creator = models.ForeignKey(
        to=KuberUser, related_name="+", to_field="id", on_delete=models.CASCADE
    )
    docker_env = models.ForeignKey(
        to=DockerEnvironment,
        related_name="+",
        to_field="env_id",
        on_delete=models.CASCADE,
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["creator", "docker_env"], name="user_env_pk"
            )
        ]
