# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-30 04:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m1', models.IntegerField(default=0)),
                ('m2', models.IntegerField(default=0)),
                ('m3', models.IntegerField(default=0)),
                ('m4', models.IntegerField(default=0)),
                ('m5', models.IntegerField(default=0)),
                ('m6', models.IntegerField(default=0)),
                ('m7', models.IntegerField(default=0)),
                ('m8', models.IntegerField(default=0)),
                ('m9', models.IntegerField(default=0)),
                ('m10', models.IntegerField(default=0)),
                ('w1', models.IntegerField(default=0)),
                ('w2', models.IntegerField(default=0)),
                ('w3', models.IntegerField(default=0)),
                ('w4', models.IntegerField(default=0)),
                ('w5', models.IntegerField(default=0)),
                ('w6', models.IntegerField(default=0)),
                ('w7', models.IntegerField(default=0)),
                ('w8', models.IntegerField(default=0)),
                ('w9', models.IntegerField(default=0)),
                ('w10', models.IntegerField(default=0)),
            ],
        ),
    ]