# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-11-30 18:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courese', '0003_stggrade_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stggrade',
            name='name',
        ),
    ]