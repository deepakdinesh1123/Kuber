# Generated by Django 4.2.2 on 2023-07-16 14:24

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Environment',
            fields=[
                ('env_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('env_name', models.CharField(max_length=100, unique=True)),
                ('dockerimage', models.CharField(max_length=100)),
                ('dockerfile', models.CharField(max_length=1000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('config', models.JSONField(default=dict)),
                ('type', models.CharField(choices=[('compose', 'docker-compose'), ('docker', 'docker')], max_length=10)),
                ('private', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Sandbox',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('private', models.BooleanField(default=False)),
                ('env', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='environment.environment')),
            ],
        ),
    ]
