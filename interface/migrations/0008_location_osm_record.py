# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-13 14:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interface', '0007_auto_20160309_2043'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='osm_record',
            field=models.TextField(null=True),
        ),
    ]
