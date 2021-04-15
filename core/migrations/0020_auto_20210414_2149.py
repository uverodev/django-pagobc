# Generated by Django 3.1 on 2021-04-15 01:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_auto_20210414_1944'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkout',
            name='transaction_reversed',
        ),
        migrations.AlterField(
            model_name='payment',
            name='date_expiration',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 17, 21, 49, 46, 108504), verbose_name='Fecha Vencimiento'),
        ),
    ]
