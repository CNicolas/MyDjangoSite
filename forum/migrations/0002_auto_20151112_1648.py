# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import forum.storage
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('title', models.CharField(default='', max_length=100)),
                ('content', models.TextField()),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('date_modification', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('title', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubTheme',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('title', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('title', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='UnreadPost',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('post', models.ForeignKey(to='forum.Post')),
            ],
        ),
        migrations.RemoveField(
            model_name='profile',
            name='age',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
        migrations.AddField(
            model_name='profile',
            name='birthdate',
            field=models.DateField(blank=True, default=datetime.datetime(2015, 11, 12, 15, 48, 26, 715733, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='profiles/Profil.jpg', storage=forum.storage.OverwriteStorage(), upload_to='forum/profiles/'),
        ),
        migrations.AddField(
            model_name='profile',
            name='previous_login',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2015, 11, 12, 15, 48, 32, 51733, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='firstname',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='lastname',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='pseudo',
            field=models.CharField(default='', max_length=100, unique=True),
        ),
        migrations.AddField(
            model_name='unreadpost',
            name='profile',
            field=models.ForeignKey(to='forum.Profile'),
        ),
        migrations.AddField(
            model_name='unreadpost',
            name='subject',
            field=models.ForeignKey(to='forum.Subject'),
        ),
        migrations.AddField(
            model_name='subtheme',
            name='theme',
            field=models.ForeignKey(to='forum.Theme'),
        ),
        migrations.AddField(
            model_name='subject',
            name='subtheme',
            field=models.ForeignKey(to='forum.SubTheme'),
        ),
        migrations.AddField(
            model_name='subject',
            name='theme',
            field=models.ForeignKey(to='forum.Theme'),
        ),
        migrations.AddField(
            model_name='post',
            name='profile',
            field=models.ForeignKey(to='forum.Profile'),
        ),
        migrations.AddField(
            model_name='post',
            name='subject',
            field=models.ForeignKey(to='forum.Subject'),
        ),
        migrations.AddField(
            model_name='post',
            name='subtheme',
            field=models.ForeignKey(to='forum.SubTheme'),
        ),
        migrations.AddField(
            model_name='post',
            name='theme',
            field=models.ForeignKey(to='forum.Theme'),
        ),
    ]
