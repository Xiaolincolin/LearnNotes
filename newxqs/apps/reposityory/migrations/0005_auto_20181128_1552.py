# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-11-28 15:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reposityory', '0004_auto_20181128_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrowbook',
            name='st_id',
            field=models.CharField(default='', max_length=50, verbose_name='学号'),
        ),
    ]