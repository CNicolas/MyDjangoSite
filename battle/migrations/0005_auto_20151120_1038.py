# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('battle', '0004_auto_20151120_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='armorcategory',
            name='place',
            field=models.CharField(max_length=100),
        ),
    ]
