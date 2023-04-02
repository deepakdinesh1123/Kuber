from django.db import models
from uuid import uuid4
from django.core.exceptions import ValidationError


def validate_env_ids(envs):
    for id in envs['id']:
        try:
            Environment.objects.get(id=id)
        except Environment.DoesNotExist:
            raise ValidationError

def validate_container_ids(containers):
    for id in containers:
        try:
            Container.objects.get(id=id)
        except Container.DoesNotExist:
            raise ValidationError



class KuberUser(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid4, name="user_id")
    username = models.CharField(max_length=100, unique=True, name="username")
    environments = models.JSONField(validators=[validate_env_ids], default=dict)
    active_containers = models.JSONField(validators=[validate_container_ids], default=dict)
    github_username = models.CharField(max_length=100, editable=False, blank=True, null=True, name="github_username")
    github_repos = models.JSONField()

class Environment(models.Model):
    env_id = models.UUIDField(primary_key=True, default=uuid4, name="env_id")
    env_name = models.CharField(max_length=100, unique=True, name="env_name")
    image = models.CharField(max_length=100, name="dockerimage")
    creator = models.ForeignKey(to=KuberUser, related_name="creator_id", to_field="user_id", on_delete=models.CASCADE, name="creator")
    config = models.JSONField(name="config", default=dict)


class Container(models.Model):
    container_id = models.UUIDField(primary_key=True, default=uuid4, name="container_id")
    container_name = models.CharField(max_length=100, name="container_name")
    environment = models.ForeignKey(to=Environment, on_delete=models.CASCADE, to_field="env_id", related_name="environment_id", name="environment")
    config = models.JSONField(name="config")
    created_by = models.ForeignKey(to=KuberUser, on_delete=models.CASCADE, to_field="user_id", related_name="userid", name="created_by")

