# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-18 23:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0005_auto_20170918_2028'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AgPrivada',
            new_name='AgendaPrivada',
        ),
        migrations.AlterField(
            model_name='agendaprivada',
            name='usuarios',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agenda.Usuario'),
        ),
    ]
