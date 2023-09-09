from django.urls import path, re_path

from .views import FormView, InterviewView

urlpatterns = [
    re_path(
        r"interview/(?P<interview_id>[0-9A-Fa-f-]+)",
        InterviewView.as_view(),
        name="interview-api",
    ),
    re_path(
        r"interview",
        InterviewView.as_view(),
        name="post-interview-api",
    ),
    re_path(
        r"forms/(?P<interview_id>[0-9A-Fa-f-]+)", FormView.as_view(), name="forms-api"
    ),
    re_path(r"forms", FormView.as_view(), name="forms-api"),
]