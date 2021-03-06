# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-09 10:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Author', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name': 'Author', 'verbose_name_plural': 'Author'},
        ),
        migrations.AlterModelOptions(
            name='authoraddress',
            options={'verbose_name': 'Author Address', 'verbose_name_plural': 'Author Address'},
        ),
        migrations.AlterField(
            model_name='author',
            name='added_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='updated_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
