# Generated by Django 3.1 on 2021-12-11 04:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20211210_1842'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='admin',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
