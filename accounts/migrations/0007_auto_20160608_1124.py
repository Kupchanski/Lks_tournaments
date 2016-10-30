# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-08 06:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_user_is_inteam'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='mix_banned',
            field=models.BooleanField(default=False, help_text='Запрет участия в миксах', verbose_name='Бан на миксы'),
        ),
        migrations.AddField(
            model_name='user',
            name='muted',
            field=models.BooleanField(default=False, help_text='Убрать возможность комментировать', verbose_name='Мут'),
        ),
        migrations.AddField(
            model_name='user',
            name='team_banned',
            field=models.BooleanField(default=False, help_text='Запрет вступления в команды', verbose_name='Бан на команды'),
        ),
    ]