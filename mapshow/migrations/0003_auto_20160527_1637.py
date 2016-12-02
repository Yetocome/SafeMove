# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-27 16:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapshow', '0002_auto_20160527_1358'),
    ]

    operations = [
        migrations.CreateModel(
            name='VisitorEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=30)),
                ('phone_number', models.CharField(default='', max_length=15)),
                ('age', models.IntegerField(default=0)),
                ('description', models.TextField(default='')),
                ('email', models.TextField(default='')),
                ('event_type', models.IntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='UserEvent',
        ),
    ]
