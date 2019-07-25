# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-07-24 03:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('breath_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SerenityShift',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suds_level_begin', models.IntegerField(default=0)),
                ('suds_level_end', models.IntegerField(default=0)),
                ('currency', models.IntegerField(default=0)),
                ('taste', models.IntegerField(default=0)),
                ('touch', models.IntegerField(default=0)),
                ('visual', models.IntegerField(default=0)),
                ('auditory', models.IntegerField(default=0)),
                ('smell', models.IntegerField(default=0)),
                ('num_breathing', models.IntegerField(default=0)),
                ('journal', models.TextField(default='')),
                ('gratitude_list', models.TextField(default='')),
                ('activity_list', models.TextField(default='')),
                ('observations', models.TextField(default='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('player', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='list_of_shifts_associated_with_user', to='breath_app.User')),
            ],
        ),
    ]
