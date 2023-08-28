from uuid import uuid4

from django.db import models
from utils.mixins.model_mixins import TimeStampMixin

# Create your models here.


def default_config(self):
    return {
        "Terminal": True,
        "FileExplorer": True,
        "VidCam": False,
        "TabSwitch": True,
        "CopyPaste": True,
    }


class Interview(TimeStampMixin):
    int_id = models.UUIDField(primary_key=True, default=uuid4, name="interview_id")
    environment = models.ForeignKey("environment.Environment", on_delete=models.CASCADE)
    creator = models.ForeignKey("user.KuberUser", on_delete=models.CASCADE)
    config = models.JSONField(default=default_config)
    time_limit = models.TimeField(null=True)

    def get_interview_url(self):
        return self.int_id


class ValidateSubmission(TimeStampMixin):
    script = models.CharField(max_length=1000, null=True)
    command = models.CharField(max_length=100)
    directory = models.CharField(max_length=100)
    interview = models.ForeignKey(Interview, on_delete=models.CASCADE)


class InterviewResult(models.Model):
    interview = models.ForeignKey(Interview, on_delete=models.CASCADE)
    interviewee = models.ForeignKey("user.KuberUser", on_delete=models.CASCADE)
    result = models.BooleanField()
