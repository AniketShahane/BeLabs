# Generated by Django 2.1.3 on 2019-01-13 16:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0026_auto_20190113_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='body',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='blog',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 13, 16, 49, 50, 406210, tzinfo=utc)),
        ),
    ]