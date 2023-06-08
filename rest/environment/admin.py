from django.contrib import admin
from environment.models import DockerEnvironment, UserDockerEnvironments

# Register your models here.
admin.site.register(DockerEnvironment)
admin.site.register(UserDockerEnvironments)
