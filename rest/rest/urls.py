"""rest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from user.views import RegisterView

VERSION = "(?<version>(v1|v2))/"
PREFIX = "api/" + VERSION

urlpatterns = [
    path("admin/", admin.site.urls),
    re_path("account/", include("user.urls")),
    re_path("languages/", include("language_support.urls")),
    re_path("environments/", include("environment.urls")),
    path("users/", include("user.urls")),
]
