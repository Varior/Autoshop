# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-22 19:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('batteries', '0005_сarbatteries_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='сarbatteries',
            name='positive_terminal_side_right',
            field=models.BooleanField(default=True, help_text='Якщо акумулятор з привим плюсом залиште як є, якщо ні то заберіть галочку', verbose_name='Полярність права'),
        ),
        migrations.AlterField(
            model_name='сarbatteries',
            name='slug',
            field=models.SlugField(),
        ),
    ]
