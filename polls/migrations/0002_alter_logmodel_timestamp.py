# Generated by Django 3.2.6 on 2021-08-28 16:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logmodel',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 28, 16, 32, 14, 284888, tzinfo=utc)),
        ),
    ]