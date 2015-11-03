# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_auto_20151022_0936'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(unique=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(unique=True, max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='subject',
            name='theme',
            field=models.ForeignKey(to='forum.Theme'),
        ),
        migrations.AddField(
            model_name='post',
            name='subject',
            field=models.ForeignKey(to='forum.Subject'),
        ),
        migrations.AddField(
            model_name='post',
            name='theme',
            field=models.ForeignKey(to='forum.Theme'),
        ),
    ]
