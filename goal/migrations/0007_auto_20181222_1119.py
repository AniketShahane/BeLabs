# Generated by Django 2.1.4 on 2018-12-22 11:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goal', '0006_auto_20181222_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 22, 11, 19, 20, 201785)),
        ),
    ]
