# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-08 11:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Localisation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(help_text='This length is no more than 50 characters.', max_length=50)),
                ('lastname', models.CharField(help_text='This length is no more than 50 characters.', max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'New Author'), (10, 'Author'), (20, 'Retirement')], default=0)),
                ('added_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now=True)),
            ],
            options={
                'db_table': 'test_author',
            },
        ),
        migrations.CreateModel(
            name='AuthorAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_1', models.CharField(help_text='This length is no more than 50 characters.', max_length=50)),
                ('address_2', models.CharField(help_text='Apt. No., Suite No. and so on.<br>This length is no more than 50 characters.', max_length=50)),
                ('city', models.CharField(help_text='City Name. This length is no more than 20 characters.', max_length=20)),
                ('zip', models.CharField(help_text='Zipcode.This length is no more than 20 characters.', max_length=20)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Author.Author')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Localisation.Country')),
                ('zone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Localisation.Zone')),
            ],
            options={
                'db_table': 'test_author_address',
            },
        ),
    ]
