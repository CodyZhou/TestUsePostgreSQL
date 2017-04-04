# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-15 15:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0003_auto_20170309_1006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='publisher_id', to='Publisher.Publisher'),
        ),
    ]