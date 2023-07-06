# Generated by Django 4.2 on 2023-06-03 17:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_client', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clients',
                                    to=settings.AUTH_USER_MODEL, verbose_name='Создан'),
        ),
    ]