# Generated by Django 4.2.4 on 2023-09-05 08:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import interview.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('environment', '0002_remove_sandbox_user_env_pk_alter_sandbox_private'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interview',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('interview_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('config', models.JSONField(default=interview.models.default_config)),
                ('time_limit', models.TimeField(null=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('environment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='environment.environment')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='InterviewTest',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('github_url', models.URLField(max_length=100)),
                ('test_command', models.CharField(max_length=100)),
                ('directory', models.CharField(blank=True, max_length=200)),
                ('setup_command', models.CharField(blank=True, max_length=100)),
                ('interview', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interview.interview')),
            ],
        ),
        migrations.CreateModel(
            name='InterviewResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
                ('result', models.BooleanField()),
                ('interview', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interview.interview')),
                ('interviewee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]