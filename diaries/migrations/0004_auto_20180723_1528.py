# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-07-23 07:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diaries', '0003_auto_20180723_1528'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserInnfo',
            new_name='UserInfo',
        ),
    ]