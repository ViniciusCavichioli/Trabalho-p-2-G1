# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-26 00:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('agenda', '0020_auto_20170925_2117'),
    ]

    operations = [
        migrations.AddField(
            model_name='convite',
            name='anfitriao',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='convite',
            name='convidado',
            field=models.ManyToManyField(null=True, related_name='convidados', to=settings.AUTH_USER_MODEL),
        ),
    ]
