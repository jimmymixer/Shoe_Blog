# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-01 16:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LoginReg', '0001_initial'),
        ('Quotes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favorites',
            name='fquote_q',
        ),
        migrations.RemoveField(
            model_name='favorites',
            name='user_fav_quote',
        ),
        migrations.AddField(
            model_name='quotes',
            name='favorited_by',
            field=models.ManyToManyField(related_name='favorited_by_user', to='LoginReg.User'),
        ),
        migrations.DeleteModel(
            name='Favorites',
        ),
    ]
