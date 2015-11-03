# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import forum.storage


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0010_auto_20151028_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='profiles/Profil.jpg', storage=forum.storage.OverwriteStorage(), upload_to='forum/profiles/'),
        ),
    ]
