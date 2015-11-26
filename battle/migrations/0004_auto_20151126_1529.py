# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('battle', '0003_auto_20151126_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ennemyattack',
            name='name',
            field=models.CharField(default='Attaque', max_length=100),
        ),
    ]
