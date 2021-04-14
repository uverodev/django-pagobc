# Generated by Django 3.1 on 2021-04-14 15:48

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_auto_20210406_1848'),
        ('core', '0015_auto_20210413_2047'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='fee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='core.fee'),
        ),
        migrations.AlterField(
            model_name='checkout',
            name='payment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='core.payment'),
        ),
        migrations.AlterField(
            model_name='fee',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='clients.client'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='clients.client'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='date_expiration',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 17, 11, 48, 51, 829798), verbose_name='Fecha Vencimiento'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='plataform',
            field=models.CharField(choices=[('va', 'Vacío'), ('om', 'Otros Métodos'), ('ap', 'Aqui Pago'), ('pe', 'Pago Express')], default='va', max_length=2, verbose_name='Método de Pago'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='status',
            field=models.CharField(choices=[('pe', 'Pendiente'), ('pa', 'Pagado'), ('an', 'Anulado')], default='pe', max_length=2, verbose_name='Estado'),
        ),
    ]
