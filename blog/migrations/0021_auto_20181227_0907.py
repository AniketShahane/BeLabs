# Generated by Django 2.1.4 on 2018-12-27 03:37

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_auto_20181223_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='pre_time',
            field=models.FloatField(default=1545881848.8058865),
        ),
        migrations.AlterField(
            model_name='blog',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 27, 3, 37, 28, 805743, tzinfo=utc)),
        ),
    ]
