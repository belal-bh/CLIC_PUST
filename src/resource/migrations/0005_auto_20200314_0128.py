# Generated by Django 2.2.1 on 2020-03-13 19:28

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resource', '0004_auto_20200309_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='weblinks',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=120), blank=True, null=True, size=None),
        ),
    ]
