# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-03 18:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('port', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='port',
            name='id',
        ),
        migrations.AlterField(
            model_name='port',
            name='portid',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
