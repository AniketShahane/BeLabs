# Generated by Django 2.1.4 on 2018-12-28 16:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0018_auto_20181227_1050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='pre_time',
            field=models.FloatField(default=1546015892.064762),
        ),
        migrations.AlterField(
            model_name='comment',
            name='pub_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 28, 16, 51, 32, 64743, tzinfo=utc)),
        ),
    ]