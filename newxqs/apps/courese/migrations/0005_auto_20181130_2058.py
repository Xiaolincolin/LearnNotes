# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-11-30 20:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courese', '0004_remove_stggrade_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='majorsystem',
            name='c_type',
            field=models.CharField(max_length=100, unique=True, verbose_name='课程性质'),
        ),
        migrations.AlterField(
            model_name='majorsystem',
            name='major',
            field=models.CharField(max_length=50, verbose_name='专业'),
        ),
    ]
