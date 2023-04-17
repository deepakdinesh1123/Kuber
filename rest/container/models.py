from uuid import uuid4

from django.db import models
from environment.models import DockerEnvironment
from user.models import KuberUser


# Create your models here.
class Container(models.Model):
    container_id = models.UUIDField(
        primary_key=True, default=uuid4, name="container_id"
    )
    container_name = models.CharField(max_length=100, name="container_name")
    environment = models.ForeignKey(
        to=DockerEnvironment,
        on_delete=models.CASCADE,
        to_field="env_id",
        related_name="+",
    )
    config = models.JSONField(name="config")
    created_by = models.ForeignKey(
        to=KuberUser, on_delete=models.CASCADE, to_field="id", related_name="+"
    )


class UserContainers(models.Model):
    user_id = models.ForeignKey(
        to=KuberUser, on_delete=models.CASCADE, to_field="id", related_name="+"
    )
    container_id = models.ForeignKey(
        to=Container,
        on_delete=models.CASCADE,
        to_field="container_id",
        related_name="+",
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user_id", "container_id"], name="user_container_pk"
            )
        ]
