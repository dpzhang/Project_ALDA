# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-09 22:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_auto_20170309_2222'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testchoice',
            name='test',
        ),
    ]