# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('battle', '0002_auto_20151126_1147'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ennemy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(unique=True, default='Monstre', max_length=100)),
                ('level', models.SmallIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(20)])),
                ('health', models.SmallIntegerField(default=100, validators=[django.core.validators.MinValueValidator(0)])),
            ],
        ),
        migrations.CreateModel(
            name='EnnemyAttack',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(unique=True, default='Attaque', max_length=100)),
                ('damage', models.SmallIntegerField(default=0)),
                ('heal', models.SmallIntegerField(default=0)),
                ('critical', models.SmallIntegerField(default=10, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('duration', models.SmallIntegerField(default=1)),
                ('cooldown', models.SmallIntegerField(default=1)),
                ('target', models.SmallIntegerField(default=1)),
                ('ennemy', models.ForeignKey(to='battle.Ennemy')),
            ],
        ),
        migrations.AddField(
            model_name='attack',
            name='cooldown',
            field=models.SmallIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='attack',
            name='name',
            field=models.CharField(default='Corps à Corps', max_length=100),
        ),
    ]
