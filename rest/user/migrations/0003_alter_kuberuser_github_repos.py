# Generated by Django 4.2 on 2023-04-14 06:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0002_alter_kuberuser_github_repos"),
    ]

    operations = [
        migrations.AlterField(
            model_name="kuberuser",
            name="github_repos",
            field=models.JSONField(default=dict, null=True),
        ),
    ]
