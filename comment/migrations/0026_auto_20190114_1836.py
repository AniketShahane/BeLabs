# Generated by Django 2.1.3 on 2019-01-14 13:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0025_auto_20190113_2219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='pub_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 14, 13, 6, 24, 235772, tzinfo=utc)),
        ),
    ]