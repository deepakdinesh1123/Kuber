from uuid import uuid4

from django.contrib.postgres.fields import ArrayField
from django.db import models
from user.models import KuberUser, Role

ENVIRONMENT_CHOICES = (("compose", "docker-compose"), ("docker", "docker"))


# Create your models here.
class Environment(models.Model):
    env_id = models.UUIDField(primary_key=True, default=uuid4, name="env_id")
    env_name = models.CharField(max_length=100, unique=True, name="env_name")
    images = ArrayField(models.CharField(max_length=100, name="dockerimage"))
    dockerfiles = ArrayField(models.FileField())
    creator = models.ForeignKey(
        to=KuberUser, related_name="+", to_field="id", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    config = models.JSONField(name="config", default=dict)
    type = models.CharField(choices=ENVIRONMENT_CHOICES, max_length=10)
    private = models.BooleanField(default=False, editable=True)


class Sandbox(models.Model):
    sandbox_creator = models.ForeignKey(
        to=KuberUser, related_name="+", to_field="id", on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        to=KuberUser, related_name="+", to_field="id", on_delete=models.CASCADE
    )
    env = models.ForeignKey(
        to=Environment,
        related_name="+",
        to_field="env_id",
        on_delete=models.CASCADE,
    )
    user_role = models.ForeignKey(
        to=Role, related_name="+", to_field="role_name", on_delete=models.PROTECT
    )
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["sandbox_creator", "env"], name="user_env_pk"
            )
        ]
