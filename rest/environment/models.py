from uuid import uuid4

from accounts.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from utils.mixins.model_mixins import TimeStampMixin

ENVIRONMENT_CHOICES = (("compose", "docker-compose"), ("docker", "docker"))
CATEGORY_CHOICES = (("p", "p"), ("g", "g"))
SANDBOX_ACTIONS = (
    ("create", "Create Sandbox"),
    ("delete", "Delete Sandbox"),
    ("execute", "Execute commands in sandbox"),
)


class DockerImage(TimeStampMixin):
    id = models.UUIDField(primary_key=True, default=uuid4, name="id", editable=False)
    name = models.CharField(max_length=100)
    Dockerfile = models.CharField(max_length=1000)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    private = models.BooleanField(default=True)


# Create your models here.
class Environment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, name="env_id")
    name = models.CharField(max_length=100, unique=True, name="env_name")
    image = models.ForeignKey(DockerImage, on_delete=models.DO_NOTHING)
    creator = models.ForeignKey(
        to=User, related_name="+", to_field="id", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    config = models.JSONField(name="config", default=dict)
    type = models.CharField(choices=ENVIRONMENT_CHOICES, max_length=10)
    private = models.BooleanField(default=True, editable=True)

    def __str__(self) -> str:
        return self.env_name


class Sandbox(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, name="id", editable=False)
    creator = models.ForeignKey(
        to=User, related_name="+", to_field="id", on_delete=models.CASCADE
    )
    env = models.ForeignKey(
        to=Environment,
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    name = models.CharField(max_length=100, unique=True)
    private = models.BooleanField(default=True)
    containers = models.JSONField(
        default=dict, blank=True, null=True
    )  # names of the containers are filled by kuber
    running = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name
