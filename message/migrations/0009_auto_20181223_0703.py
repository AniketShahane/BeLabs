# Generated by Django 2.1.4 on 2018-12-23 07:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0008_auto_20181222_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 23, 7, 3, 47, 98499, tzinfo=utc)),
        ),
    ]
