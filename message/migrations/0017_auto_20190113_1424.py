# Generated by Django 2.1.3 on 2019-01-13 08:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0016_auto_20181228_2234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='pre_time',
            field=models.FloatField(default=1547369682.547722),
        ),
        migrations.AlterField(
            model_name='message',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 13, 8, 54, 42, 547694, tzinfo=utc)),
        ),
    ]
