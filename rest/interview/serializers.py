from accounts.models import User
from accounts.serializers import CreatorSerializer
from environment.models import Environment
from rest_framework import serializers

from .models import Interview, InterviewResult, InterviewTest


class InterviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interview
        fields = "__all__"


class InterviewResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterviewResult
        fields = "__all__"


class InterviewTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterviewTest
        fields = "__all__"
