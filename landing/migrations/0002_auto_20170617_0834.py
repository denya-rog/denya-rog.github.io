# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-17 08:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=64)),
            ],
            options={
                'verbose_name': 'MySubscriber',
                'verbose_name_plural': 'All MySubscribers',
            },
        ),
        migrations.DeleteModel(
            name='Subscribers',
        ),
    ]
