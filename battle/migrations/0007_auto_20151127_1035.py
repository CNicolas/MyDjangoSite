# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('battle', '0006_auto_20151127_1012'),
    ]

    operations = [
        migrations.AddField(
            model_name='ennemyattack',
            name='acronym',
            field=models.CharField(default='CAC', max_length=100),
        ),
        migrations.AddField(
            model_name='ennemyattack',
            name='symbol',
            field=models.CharField(default='ra ra-sword', max_length=100),
        ),
    ]
