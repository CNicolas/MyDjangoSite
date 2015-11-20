# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('battle', '0003_auto_20151119_1651'),
    ]

    operations = [
        migrations.RenameField(
            model_name='armorcategory',
            old_name='name',
            new_name='place',
        ),
        migrations.AddField(
            model_name='classe',
            name='armor_type',
            field=models.SmallIntegerField(default=2, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(3)]),
        ),
    ]
