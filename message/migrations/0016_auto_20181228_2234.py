# Generated by Django 2.1.4 on 2018-12-28 17:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0015_auto_20181228_2221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='pre_time',
            field=models.FloatField(default=1546016667.4670599),
        ),
        migrations.AlterField(
            model_name='message',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 28, 17, 4, 27, 467029, tzinfo=utc)),
        ),
    ]