from accounts.views import RegisterView
from django.urls import path

urlpatterns = [
    path("auth/github/", RegisterView.as_view(), name="github-auth"),
]
