# Generated by Django 2.1.3 on 2019-01-13 12:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0017_auto_20190113_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='pre_time',
            field=models.FloatField(default=1547380975.9619799),
        ),
        migrations.AlterField(
            model_name='message',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 13, 12, 2, 55, 961952, tzinfo=utc)),
        ),
    ]
