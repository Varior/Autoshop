# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-23 17:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('batteries', '0007_auto_20160622_2341'),
    ]

    operations = [
        migrations.AddField(
            model_name='brandname',
            name='brand_info',
            field=models.TextField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='brandname',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='series',
            name='series_info',
            field=models.TextField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='series',
            name='slug',
            field=models.SlugField(default=5),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='typeofbattery',
            name='slug',
            field=models.SlugField(max_length=10),
        ),
    ]
