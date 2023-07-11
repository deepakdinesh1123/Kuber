from django.urls import path
from environment.views import EnvironmentView, Machine

urlpatterns = [
    path(
        "api/v1/environment/<str:action>/",
        EnvironmentView.as_view(),
        name="environment-api",
    ),
    path("machine/api/v1/<str:action>/", Machine.as_view(), name="machine-api"),
]
