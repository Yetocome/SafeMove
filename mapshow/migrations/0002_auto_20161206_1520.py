# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-12-06 15:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapshow', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visualdata',
            name='lat',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='visualdata',
            name='lng',
            field=models.CharField(max_length=100),
        ),
    ]
