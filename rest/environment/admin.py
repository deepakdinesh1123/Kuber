from django.contrib import admin
from environment.models import DockerImage, Environment, Sandbox

# Register your models here.
admin.site.register(Environment)
admin.site.register(Sandbox)
admin.site.register(DockerImage)
