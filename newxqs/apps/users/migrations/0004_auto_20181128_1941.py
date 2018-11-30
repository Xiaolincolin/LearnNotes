# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-11-28 19:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_mymessage_myclass'),
    ]

    operations = [
        migrations.AddField(
            model_name='mymessage',
            name='early_warning',
            field=models.CharField(choices=[('normal', '正常'), ('caution', '警告'), ('fw_st', '跟班'), ('demotion', '降级'), ('dropout', '退学')], default='正常', max_length=10),
        ),
        migrations.AlterField(
            model_name='mymessage',
            name='gender',
            field=models.CharField(choices=[('male', '男'), ('famale', '女')], default='男', max_length=6),
        ),
    ]