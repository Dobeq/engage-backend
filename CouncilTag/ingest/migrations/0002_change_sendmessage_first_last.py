# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-06-21 17:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='first_name',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='last_name',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
