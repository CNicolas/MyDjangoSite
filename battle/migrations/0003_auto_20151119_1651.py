# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('battle', '0002_auto_20151119_1646'),
    ]

    operations = [
        migrations.RenameField(
            model_name='playerarmor',
            old_name='piece',
            new_name='armor',
        ),
    ]
