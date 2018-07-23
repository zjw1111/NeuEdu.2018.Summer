# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-07-23 07:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('diaries', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='budget',
            field=models.FloatField(verbose_name=b'\xe9\xa2\x84\xe7\xae\x97'),
        ),
        migrations.AlterField(
            model_name='diary',
            name='date',
            field=models.DateField(auto_now=True, verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f'),
        ),
        migrations.AlterField(
            model_name='diary',
            name='note',
            field=models.TextField(verbose_name=b'\xe6\x97\xa5\xe8\xae\xb0\xe6\x96\x87\xe6\x9c\xac'),
        ),
        migrations.AlterField(
            model_name='diary',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\x90\x8d'),
        ),
        migrations.AlterField(
            model_name='diary',
            name='weight',
            field=models.FloatField(verbose_name=b'\xe4\xbd\x93\xe9\x87\x8d'),
        ),
    ]
