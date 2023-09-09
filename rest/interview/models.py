from uuid import uuid4

from django.db import models
from utils.mixins.model_mixins import TimeStampMixin

# Create your models here.


def default_config():
    return {
        "Terminal": True,
        "FileExplorer": True,
        "VidCam": False,
        "TabSwitch": True,
        "CopyPaste": True,
    }


class Interview(TimeStampMixin):
    id = models.UUIDField(primary_key=True, default=uuid4, name="interview_id")
    name = models.CharField(max_length=100, unique=True, default="Interview Object")
    environment = models.ForeignKey("environment.Environment", on_delete=models.CASCADE)
    creator = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    config = models.JSONField(default=default_config)
    problem = models.TextField(blank=True, null=True)
    time_limit = models.TimeField(null=True)

    def get_interview_url(self):
        return self.int_id

    def __str__(self) -> str:
        return self.name


class InterviewTest(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, name="id", editable=False)
    interview = models.ForeignKey(
        to=Interview,
        on_delete=models.CASCADE,
    )
    github_url = models.URLField(max_length=100)
    test_command = models.CharField(max_length=100)
    directory = models.CharField(max_length=200, blank=True)
    setup_command = models.CharField(max_length=100, blank=True)


class InterviewResult(models.Model):
    interview = models.ForeignKey(Interview, on_delete=models.CASCADE)
    interviewee = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    submitted_at = models.DateTimeField(auto_now_add=True)
    result = models.BooleanField()
