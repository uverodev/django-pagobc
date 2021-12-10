# Generated by Django 3.1 on 2021-12-10 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20211210_0203'),
    ]

    operations = [
        migrations.RenameField(
            model_name='checkout',
            old_name='user',
            new_name='owner',
        ),
        migrations.RenameField(
            model_name='fee',
            old_name='user',
            new_name='owner',
        ),
        migrations.RenameField(
            model_name='payment',
            old_name='user',
            new_name='owner',
        ),
        migrations.AlterField(
            model_name='payment',
            name='date_expiration',
            field=models.CharField(default='13-12-2021', max_length=30, verbose_name='Fecha Vencimiento'),
        ),
    ]