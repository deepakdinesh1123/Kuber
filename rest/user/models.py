from uuid import uuid4

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.exceptions import ValidationError
from django.db import models
from utils.mixins.model_mixins import TimeStampMixin


class UserManager(BaseUserManager):
    use_in_migration = True

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is Required")
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff = True")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser = True")

        return self.create_user(email, password, **extra_fields)


class KuberUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid4, name="id", editable=False)
    username = models.CharField(max_length=100, unique=True, name="username")
    github_username = models.CharField(
        max_length=100, editable=False, blank=True, null=True, name="github_username"
    )
    github_repos = models.JSONField(null=True, default=dict)
    email = models.EmailField(max_length=100, unique=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = "username"

    def __str__(self):
        return self.username


class Role(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid4, name="role_id", editable=False
    )
    role_name = models.CharField(
        max_length=20, editable=False, name="role_name", unique=True
    )
    permissions = models.JSONField(unique=True, editable=False)


# class Organization(TimeStampMixin):
#     pass

# class Team(TimeStampMixin):
#     pass
