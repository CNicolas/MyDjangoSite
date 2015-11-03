# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0004_auto_20151023_1402'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubTheme',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=100, unique=True)),
                ('theme', models.ForeignKey(to='forum.Theme')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='subtheme',
            field=models.ForeignKey(default=1, to='forum.SubTheme'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subject',
            name='subtheme',
            field=models.ForeignKey(default=1, to='forum.SubTheme'),
            preserve_default=False,
        ),
    ]
