# Generated by Django 2.1.4 on 2018-12-22 11:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20181222_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 22, 11, 19, 20, 202452)),
        ),
    ]
