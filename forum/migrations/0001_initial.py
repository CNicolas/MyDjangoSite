# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import forum.storage


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100)),
                ('content', models.TextField()),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('date_modification', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('pseudo', models.CharField(unique=True, default='', max_length=100)),
                ('firstname', models.CharField(default='', max_length=100)),
                ('lastname', models.CharField(default='', max_length=100)),
                ('birthdate', models.DateField(blank=True)),
                ('image', models.ImageField(upload_to='forum/profiles/', default='profiles/Profil.jpg', storage=forum.storage.OverwriteStorage())),
                ('previous_login', models.DateTimeField(blank=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(unique=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SubTheme',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(unique=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(unique=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UnreadPost',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('post', models.ForeignKey(to='forum.Post')),
                ('profile', models.ForeignKey(to='forum.Profile')),
                ('subject', models.ForeignKey(to='forum.Subject')),
            ],
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
