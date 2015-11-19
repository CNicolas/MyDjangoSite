# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArmorCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('weight', models.SmallIntegerField(default=2, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(3)])),
            ],
        ),
        migrations.CreateModel(
            name='ArmorPiece',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('price', models.SmallIntegerField(default=10, validators=[django.core.validators.MinValueValidator(10)])),
                ('defense', models.SmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('health', models.SmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('mana', models.SmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('strength', models.SmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('wisdom', models.SmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('intellect', models.SmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('spirit', models.SmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('category', models.ForeignKey(to='battle.ArmorCategory')),
            ],
        ),
        migrations.CreateModel(
            name='Attack',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, default='', unique=True)),
                ('damage', models.SmallIntegerField(default=0)),
                ('heal', models.SmallIntegerField(default=0)),
                ('mana', models.SmallIntegerField(default=0)),
                ('target', models.SmallIntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='AttackByClasse',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('attack', models.ForeignKey(to='battle.Attack')),
            ],
        ),
        migrations.CreateModel(
            name='Classe',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, default='', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('pseudo', models.CharField(max_length=100, default='', unique=True)),
                ('level', models.SmallIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(20)])),
                ('experience', models.SmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('health', models.SmallIntegerField(default=100, validators=[django.core.validators.MinValueValidator(0)])),
                ('mana', models.SmallIntegerField(default=100, validators=[django.core.validators.MinValueValidator(0)])),
                ('strength', models.SmallIntegerField(default=10, validators=[django.core.validators.MinValueValidator(8)])),
                ('wisdom', models.SmallIntegerField(default=10, validators=[django.core.validators.MinValueValidator(8)])),
                ('intellect', models.SmallIntegerField(default=10, validators=[django.core.validators.MinValueValidator(8)])),
                ('spirit', models.SmallIntegerField(default=10, validators=[django.core.validators.MinValueValidator(8)])),
                ('classe', models.ForeignKey(to='battle.Classe')),
            ],
        ),
        migrations.CreateModel(
            name='PlayerArmor',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('piece', models.ForeignKey(to='battle.ArmorPiece')),
                ('player', models.ForeignKey(to='battle.Player')),
            ],
        ),
        migrations.AddField(
            model_name='attackbyclasse',
            name='classe',
            field=models.ForeignKey(to='battle.Classe'),
        ),
    ]
