# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-07-23 07:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diaries', '0004_auto_20180723_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='gender',
            field=models.IntegerField(choices=[(0, b'Woman'), (1, b'Man')], default=0, verbose_name=b'\xe6\x80\xa7\xe5\x88\xab'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='height',
            field=models.FloatField(verbose_name=b'\xe8\xba\xab\xe9\xab\x98'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='personal_page_url',
            field=models.URLField(verbose_name=b'\xe4\xb8\xaa\xe4\xba\xba\xe4\xb8\xbb\xe9\xa1\xb5'),
        ),
    ]