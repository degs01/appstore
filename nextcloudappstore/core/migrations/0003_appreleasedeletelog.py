# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-23 19:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20160913_1909'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppReleaseDeleteLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_modified', models.DateTimeField(auto_now=True, db_index=True)),
            ],
        ),
    ]
