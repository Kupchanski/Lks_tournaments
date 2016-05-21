# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-21 05:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_coach',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_organizer',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_referee',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_responsible',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_staff',
        ),
        migrations.AlterField(
            model_name='user',
            name='banned',
            field=models.BooleanField(default=False, help_text='Забанить игрока на сайте', verbose_name='Забанен'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_admin',
            field=models.BooleanField(default=False, help_text='Админ сайта', verbose_name='Админ'),
        ),
    ]