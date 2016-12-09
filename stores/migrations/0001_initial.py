# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-12-09 02:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('suite_number', models.CharField(max_length=255)),
                ('address_line_1', models.IntegerField()),
                ('address_line_2', models.EmailField(blank=True, default='', max_length=255)),
                ('address_city', models.CharField(max_length=255)),
                ('address_state', models.CharField(max_length=255)),
                ('address_zipcode', models.IntegerField()),
            ],
        ),
    ]