#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: cnicolas
# @Date:   2015-11-19 13:29:32
# @Last Modified by:   cnicolas
# @Last Modified time: 2015-11-25 12:06:44

from django.db import models

def manager_to_string(manager):
	objects = manager.all()
	if not objects:
		return "[]"
	res = "[ "
	for obj in objects:
		res += str(obj) + ", "
	res = res[:-2] + " ]"
	return res


class ClasseManager(models.Manager):
	def create_classe(self, name, armor_type, health):
		classe = self.create(name=name, armor_type=armor_type, health=health)
		return classe

	def __str__(self):
		return manager_to_string(self)

class AttackManager(models.Manager):
	def create_attack(self, name, damage, heal, mana, energy, duration, target):
		attack = self.create(name=name, damage=damage, heal=heal, mana=mana, energy=energy, duration=duration, target=target)
		return attack

	def __str__(self):
		return manager_to_string(self)

class AttackByClasseManager(models.Manager):
	def create_attack_by_classe(self, classe, attack):
		attack_by_classe = self.create(classe=classe, attack=attack)
		return attack_by_classe

	def __str__(self):
		return manager_to_string(self)

class ArmorCategoryManager(models.Manager):
	def create_armor_category(self, place, weight):
		armor_category = self.create(place=place, weight=weight)
		return armor_category

	def __str__(self):
		return manager_to_string(self)

class ArmorPieceManager(models.Manager):
	def create_armor_piece(self, name, price, defense, health, mana, energy, strength, agility, intellect, spirit, category):
		armor_piece = self.create(name=name, price=price, defense=defense, health=health, mana=mana, energy=energy, strength=strength, agility=agility, intellect=intellect, spirit=spirit, category=category)
		return armor_piece

	def __str__(self):
		return manager_to_string(self)

class PlayerManager(models.Manager):
	def create_player(self, pseudo, classe, level, experience, health, mana, energy, strength, agility, intellect, spirit):
		player = self.create(pseudo=pseudo, classe=classe, level=level, experience=experience, health=health, mana=mana, energy=energy, strength=strength, agility=agility, intellect=intellect, spirit=spirit)
		return player

	def __str__(self):
		return manager_to_string(self)

class PlayerArmorManager(models.Manager):
	def create_player_armor(self, player, armor):
		player_armor = self.create(player=player, armor=armor)
		return player_armor

	def __str__(self):
		return manager_to_string(self)
