# Generated by Django 4.2.2 on 2023-07-15 12:02

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('environment', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='environment',
            name='dockerfiles',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(), size=None),
        ),
    ]
