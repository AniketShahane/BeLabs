# Generated by Django 2.1.3 on 2019-01-13 08:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0020_auto_20181228_2234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='pre_time',
            field=models.FloatField(default=1547369682.5495749),
        ),
        migrations.AlterField(
            model_name='comment',
            name='pub_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 13, 8, 54, 42, 549556, tzinfo=utc)),
        ),
    ]
