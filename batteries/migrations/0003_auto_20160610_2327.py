# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-10 20:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('batteries', '0002_auto_20160608_0020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='series',
            name='brand',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='batteries.BrandName'),
        ),
    ]