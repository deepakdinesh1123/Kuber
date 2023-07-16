from django.urls import re_path
from environment.views import EnvironmentView, SandboxView

urlpatterns = [
    re_path(
        "<str:action>/",
        EnvironmentView.as_view(),
        name="environment-api",
    ),
    re_path("sandbox/<str:action>/", SandboxView.as_view(), name="sandbox-api"),
]
