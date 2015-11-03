# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0005_auto_20151023_1421'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=models.TextField(default='content'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='date_creation',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 27, 14, 24, 2, 363742, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='date_modification',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 27, 14, 24, 7, 451742, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='profile',
            field=models.ForeignKey(default=1, to='forum.Profile'),
            preserve_default=False,
        ),
    ]
