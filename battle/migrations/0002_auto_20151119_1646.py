# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('battle', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='armorpiece',
            old_name='wisdom',
            new_name='agility',
        ),
        migrations.RenameField(
            model_name='player',
            old_name='wisdom',
            new_name='agility',
        ),
    ]
