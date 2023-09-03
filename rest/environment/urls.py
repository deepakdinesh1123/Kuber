from django.urls import re_path
from environment.views import (
    EnvironmentView,
    Machine,
    SandboxView,
    create_image,
    get_all_images,
    get_image,
    json_schema_view,
)

urlpatterns = [
    re_path(
        r"environment/(?P<env_id>[0-9A-Fa-f-]+)/sandbox/",
        SandboxView.as_view(),
        name="sandbox-api",
    ),
    re_path(
        r"environment/(?P<env_id>[0-9A-Fa-f-]+)",
        EnvironmentView.as_view(),
        name="getEnvironment",
    ),
    re_path(
        "environment/",
        EnvironmentView.as_view(),
        name="environment-api",
    ),
    re_path(
        r"sandbox/",
        SandboxView.as_view(),
        name="getSandbox",
    ),
    re_path("machine/", Machine.as_view(), name="machine"),
    re_path("image/build", create_image, name="build_image"),
    re_path(r"image/(?P<image_id>\d+)/$", get_image, name="get_image"),
    # re_path("", get_all_images, name="get_all_images"),
    re_path("forms/env/", json_schema_view, name="json_schema"),
]
