# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-09 19:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interface', '0004_auto_20160309_1538'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='creationDate',
        ),
        migrations.RemoveField(
            model_name='location',
            name='tstamp',
        ),
        migrations.AlterField(
            model_name='location',
            name='extraInfo',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='locName',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='location',
            name='locNameOL',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='notes',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='oLangKey',
            field=models.SmallIntegerField(default=0),
        ),
    ]
