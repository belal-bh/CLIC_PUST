# Generated by Django 2.2.1 on 2020-03-09 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resource', '0003_auto_20200309_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='status',
            field=models.CharField(blank=True, default='available', max_length=15, null=True),
        ),
    ]