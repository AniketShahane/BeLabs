# Generated by Django 2.1.4 on 2018-12-28 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goal', '0017_auto_20181228_2221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='time',
            field=models.FloatField(default=1546016667.4676096),
        ),
    ]