# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-17 08:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0002_auto_20170617_0834'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscriber',
            name='id',
        ),
        migrations.AlterField(
            model_name='subscriber',
            name='name',
            field=models.CharField(max_length=64, primary_key=True, serialize=False),
        ),
    ]
