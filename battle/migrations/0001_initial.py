# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArmorPiece',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(unique=True, max_length=100)),
                ('place', models.CharField(max_length=100)),
                ('weight', models.CharField(max_length=100)),
                ('price', models.SmallIntegerField(validators=[django.core.validators.MinValueValidator(10)], default=10)),
                ('defense', models.SmallIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)], default=0)),
                ('health', models.SmallIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)], default=0)),
                ('mana', models.SmallIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)], default=0)),
                ('energy', models.SmallIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)], default=0)),
                ('strength', models.SmallIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], default=0)),
                ('agility', models.SmallIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], default=0)),
                ('intellect', models.SmallIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], default=0)),
                ('spirit', models.SmallIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Attack',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=100, default='')),
                ('damage', models.SmallIntegerField(default=0)),
                ('heal', models.SmallIntegerField(default=0)),
                ('mana', models.SmallIntegerField(default=0)),
                ('energy', models.SmallIntegerField(default=0)),
                ('critical', models.SmallIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], default=10)),
                ('duration', models.SmallIntegerField(default=1)),
                ('target', models.SmallIntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='AttackByClasse',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('attack', models.ForeignKey(to='battle.Attack')),
            ],
        ),
        migrations.CreateModel(
            name='Classe',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(unique=True, max_length=100, default='')),
                ('weight', models.CharField(max_length=100)),
                ('health', models.SmallIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], default=0)),
                ('primary_stat', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('pseudo', models.CharField(unique=True, max_length=100, default='')),
                ('level', models.SmallIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(20)], default=1)),
                ('experience', models.SmallIntegerField(validators=[django.core.validators.MinValueValidator(0)], default=0)),
                ('health', models.SmallIntegerField(validators=[django.core.validators.MinValueValidator(0)], default=100)),
                ('mana', models.SmallIntegerField(validators=[django.core.validators.MinValueValidator(0)], default=100)),
                ('energy', models.SmallIntegerField(validators=[django.core.validators.MinValueValidator(0)], default=100)),
                ('strength', models.SmallIntegerField(validators=[django.core.validators.MinValueValidator(8)], default=10)),
                ('agility', models.SmallIntegerField(validators=[django.core.validators.MinValueValidator(8)], default=10)),
                ('intellect', models.SmallIntegerField(validators=[django.core.validators.MinValueValidator(8)], default=10)),
                ('spirit', models.SmallIntegerField(validators=[django.core.validators.MinValueValidator(8)], default=10)),
                ('classe', models.ForeignKey(to='battle.Classe')),
            ],
        ),
        migrations.CreateModel(
            name='PlayerArmor',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('armor', models.ForeignKey(to='battle.ArmorPiece')),
                ('player', models.ForeignKey(to='battle.Player')),
            ],
        ),
        migrations.AddField(
            model_name='attackbyclasse',
            name='classe',
            field=models.ForeignKey(to='battle.Classe'),
        ),
    ]
