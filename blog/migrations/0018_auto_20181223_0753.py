# Generated by Django 2.1.4 on 2018-12-23 07:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_auto_20181223_0703'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='pre_time',
            field=models.FloatField(default=1545551624.4533734),
        ),
        migrations.AlterField(
            model_name='blog',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 23, 7, 53, 44, 453286, tzinfo=utc)),
        ),
    ]
