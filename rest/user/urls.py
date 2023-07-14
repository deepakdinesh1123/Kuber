from django.urls import path
from user.views import RegisterView

urlpatterns = [path("/authorize/github", RegisterView.as_view())]
