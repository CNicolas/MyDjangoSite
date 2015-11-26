# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('battle', '0004_auto_20151126_1529'),
    ]

    operations = [
        migrations.AddField(
            model_name='attack',
            name='symbol',
            field=models.CharField(max_length=100, default='ra ra-sword'),
            preserve_default=False,
        ),
    ]
