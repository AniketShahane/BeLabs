# Generated by Django 2.1.4 on 2018-12-22 20:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0009_auto_20181222_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='pub_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 22, 20, 24, 4, 857895)),
        ),
    ]