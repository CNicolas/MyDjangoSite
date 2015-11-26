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
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=100, default='')),
                ('content', models.TextField()),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('date_modification', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('pseudo', models.CharField(unique=True, default='', max_length=100)),
                ('firstname', models.CharField(max_length=100, default='')),
                ('lastname', models.CharField(max_length=100, default='')),
                ('birthdate', models.DateField(blank=True)),
                ('image', models.ImageField(default='profiles/Profil.jpg', upload_to='forum/profiles/', storage=forum.storage.OverwriteStorage())),
                ('previous_login', models.DateTimeField(blank=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(unique=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SubTheme',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(unique=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(unique=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UnreadPost',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
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
