# Generated by Django 4.2.2 on 2023-09-05 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('environment', '0002_remove_sandbox_user_env_pk_alter_sandbox_private'),
    ]

    operations = [
        migrations.AddField(
            model_name='sandbox',
            name='running',
            field=models.BooleanField(default=False),
        ),
    ]
