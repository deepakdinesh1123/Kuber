from django.shortcuts import render
from language_support.models import Language
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.
class LanguageSupport(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, language):
        config = Language.objects.get(name=language)
        return Response(config.tokenizer)

    def get_permissions(self):
        return super().get_permissions()
