# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-11-28 20:11
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courese', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='majorsystem',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间'),
        ),
        migrations.AddField(
            model_name='stcredit',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间'),
        ),
    ]