# Generated by Django 3.1 on 2021-04-17 01:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_auto_20210414_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='date_expiration',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 19, 21, 19, 37, 435163), verbose_name='Fecha Vencimiento'),
        ),
    ]
