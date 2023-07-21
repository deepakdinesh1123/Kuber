from django.urls import re_path
from environment.views import EnvironmentView, Machine, SandboxView

urlpatterns = [
    re_path(
        "environment/(?P<env_id>[0-9A-Fa-f-]+)/sandbox/",
        SandboxView.as_view(),
        name="sandbox-api",
    ),
    re_path(
        "environment/(?P<env_id>[0-9A-Fa-f-]+)",
        EnvironmentView.as_view(),
        name="getEnvironment",
    ),
    re_path(
        "environment/",
        EnvironmentView.as_view(),
        name="environment-api",
    ),
    re_path("machine/", Machine.as_view(), name="machine"),
]
