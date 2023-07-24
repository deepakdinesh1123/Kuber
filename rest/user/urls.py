from django.urls import path
from user.views import RegisterView

urlpatterns = [path("auth/github", RegisterView.as_view(), name="github-auth")]
