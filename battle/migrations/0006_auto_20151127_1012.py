# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('battle', '0005_attack_symbol'),
    ]

    operations = [
        migrations.AddField(
            model_name='attack',
            name='acronym',
            field=models.CharField(max_length=100, default='CAC'),
        ),
        migrations.AlterField(
            model_name='attack',
            name='symbol',
            field=models.CharField(max_length=100, default='ra ra-sword'),
        ),
    ]
