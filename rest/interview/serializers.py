from .models import Interview, InterviewResult, InterviewTest
from rest_framework import serializers
from environment.models import Environment
from accounts.models import User
from accounts.serializers import CreatorSerializer


class InterviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Interview
        fields = '__all__'


class InterviewResultSerializer(serializers.ModelSerializer):

    class Meta:
        model = InterviewResult
        fields = '__all__'


class InterviewTestSerializer(serializers.ModelSerializer):

    class Meta:
        model = InterviewTest
        fields = '__all__'
