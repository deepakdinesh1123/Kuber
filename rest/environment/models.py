from uuid import uuid4

from django.db import models
from user.models import KuberUser
from utils.mixins.model_mixins import TimeStampMixin

ENVIRONMENT_CHOICES = (("compose", "docker-compose"), ("docker", "docker"))
CATEGORY_CHOICES = (("p", "p"), ("g", "g"))
SANDBOX_ACTIONS = (
    ("create", "Create Sandbox"),
    ("delete", "Delete Sandbox"),
    ("execute", "Execute commands in sandbox"),
)


class DockerImage(TimeStampMixin):
    name = models.CharField(max_length=100)
    Dockerfile = models.CharField(max_length=1000)
    created_by = models.ForeignKey(KuberUser, on_delete=models.CASCADE)


# Create your models here.
class Environment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, name="env_id")
    name = models.CharField(max_length=100, unique=True, name="env_name")
    image = models.ForeignKey(DockerImage, on_delete=models.DO_NOTHING)
    dockerfile = models.CharField(max_length=1000, name="dockerfile")
    creator = models.ForeignKey(
        to=KuberUser, related_name="+", to_field="id", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    config = models.JSONField(name="config", default=dict)
    type = models.CharField(choices=ENVIRONMENT_CHOICES, max_length=10)
    private = models.BooleanField(default=False, editable=True)

    def __str__(self) -> str:
        return self.env_name


class EnvironmentTest(models.Model):
    environment = models.ForeignKey(
        to=Environment,
        related_name="+",
        to_field="env_id",
        on_delete=models.CASCADE,
    )
    github_url = models.URLField(max_length=100)
    test_command = models.CharField(max_length=100)
    directory = models.CharField(max_length=200, blank=True)
    setup_command = models.CharField(max_length=100, blank=True)


class Sandbox(models.Model):
    sandbox_creator = models.ForeignKey(
        to=KuberUser, related_name="+", to_field="id", on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        to=KuberUser, related_name="+", to_field="id", on_delete=models.CASCADE
    )
    env = models.ForeignKey(
        to=Environment,
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    name = models.CharField(max_length=100, unique=True)
    private = models.BooleanField(default=False)
    containers = models.JSONField(
        default=dict, blank=True, null=True
    )  # names of the containers are filled by kuber

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["sandbox_creator", "env"], name="user_env_pk"
            )
        ]


# class SandboxPermissions(models.Model):
#     category = models.CharField(max_length=1, choices=CATEGORY_CHOICES)
#     sandbox = models.ForeignKey(Sandbox, related_name="+", to_field="name", on_delete=models.CASCADE)
#     user = models.ForeignKey(KuberUser, related_name="+", to_field="id", on_delete=models.CASCADE)
#     action = models.CharField(max_length=15, choices=SANDBOX_ACTIONS)

# class EnvironmentPermissions(models.Model):
#     category = models.CharField(max_length=1, choices=CATEGORY_CHOICES)
#     environment = models.ForeignKey(Environment, related_name="+",
# to_field="name", on_delete=models.CASCADE)
