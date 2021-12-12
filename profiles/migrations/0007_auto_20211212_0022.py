# Generated by Django 3.1 on 2021-12-12 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_auto_20211211_0146'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Activado'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='type',
            field=models.CharField(choices=[('VE', 'Vendedor'), ('TR', 'Transportador'), ('AD', 'Administrador')], default='AD', max_length=2, verbose_name='Tipo'),
        ),
    ]