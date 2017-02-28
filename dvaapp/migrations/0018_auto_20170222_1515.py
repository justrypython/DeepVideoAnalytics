# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-22 15:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dvaapp', '0017_framelabel_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='url',
            field=models.TextField(default=True),
        ),
        migrations.AddField(
            model_name='video',
            name='youtube_video',
            field=models.BooleanField(default=False),
        ),
    ]