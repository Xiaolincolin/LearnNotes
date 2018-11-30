# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-11-28 15:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reposityory', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='banner',
            options={'verbose_name': '大赛信息', 'verbose_name_plural': '大赛信息'},
        ),
        migrations.AddField(
            model_name='banner',
            name='image',
            field=models.ImageField(default='banner/default.png', upload_to='banner/%Y/%m', verbose_name='轮播图'),
        ),
        migrations.AddField(
            model_name='banner',
            name='index',
            field=models.IntegerField(default=100, verbose_name='顺序'),
        ),
    ]
