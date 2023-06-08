from django.urls import path
from language_support.views import LanguageSupport

urlpatterns = [path("api/monarch_config/<str:language>/", LanguageSupport.as_view())]
