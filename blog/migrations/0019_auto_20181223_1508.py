# Generated by Django 2.1.4 on 2018-12-23 09:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_auto_20181223_0753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='pre_time',
            field=models.FloatField(default=1545557925.096321),
        ),
        migrations.AlterField(
            model_name='blog',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 23, 9, 38, 45, 96231, tzinfo=utc)),
        ),
    ]
