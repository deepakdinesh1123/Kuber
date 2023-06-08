from django.urls import path
from environment.views import Environment, Machine

urlpatterns = [
    path("api/v1/<str:action>/", Environment.as_view(), name="environment-api"),
    path("machine/api/v1/<str:action>/", Machine.as_view(), name="machine-api"),
]
