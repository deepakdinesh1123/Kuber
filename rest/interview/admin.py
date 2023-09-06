from django.contrib import admin

from .models import Interview, InterviewResult, InterviewTest

# Register your models here.
admin.site.register(Interview)
admin.site.register(InterviewResult)
admin.site.register(InterviewTest)
