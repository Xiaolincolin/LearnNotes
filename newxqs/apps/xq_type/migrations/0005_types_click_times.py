# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-11-28 20:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xq_type', '0004_auto_20181128_1543'),
    ]

    operations = [
        migrations.AddField(
            model_name='types',
            name='click_times',
            field=models.IntegerField(default=0, verbose_name='点击次数'),
        ),
    ]
