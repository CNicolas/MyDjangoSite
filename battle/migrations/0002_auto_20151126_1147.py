# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('battle', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classe',
            name='primary_stat',
        ),
        migrations.AddField(
            model_name='attack',
            name='stat',
            field=models.CharField(max_length=100, default='strength'),
            preserve_default=False,
        ),
    ]
