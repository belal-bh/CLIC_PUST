# Generated by Django 2.2.1 on 2020-03-14 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resource', '0006_auto_20200314_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='author',
            name='nicname',
            field=models.CharField(max_length=30),
        ),
    ]
