# Generated by Django 3.1 on 2021-12-10 05:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20211210_0159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='date_expiration',
            field=models.CharField(default=datetime.datetime(2021, 12, 13, 5, 3, 25, 898742, tzinfo=utc), max_length=30, verbose_name='Fecha Vencimiento'),
        ),
    ]