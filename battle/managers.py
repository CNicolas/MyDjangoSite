#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: cnicolas
# @Date:   2015-11-19 13:29:32
# @Last Modified by:   cnicolas
# @Last Modified time: 2015-11-25 15:44:23

import logging

from django.db import models

logger = logging.getLogger(__name__)

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
	def create_classe(self, name, weight, health):
		check = self.filter(name=name, weight=weight, health=health)
		if len(check) > 0:
			return check[0]
		else:
			classe = self.create(name=name, weight=weight, health=health)
			return classe

	def __str__(self):
		return manager_to_string(self)

class AttackManager(models.Manager):
	def create_attack(self, name, damage, heal, mana, energy, critical, duration, target):
		check = self.filter(name=name, damage=damage, heal=heal, mana=mana, energy=energy, critical=critical, duration=duration, target=target)
		# print(name, check)
		if len(check) > 0:
			return check[0]
		else:
			attack = self.create(name=name, damage=damage, heal=heal, mana=mana, energy=energy, duration=duration, target=target)
			return attack

	def __str__(self):
		return manager_to_string(self)

class AttackByClasseManager(models.Manager):
	def create_attack_by_classe(self, classe, attack):
		check = self.filter(classe=classe, attack=attack)
		if len(check) > 0:
			return check[0]
		else:
			attack_by_classe = self.create(classe=classe, attack=attack)
			return attack_by_classe

	def __str__(self):
		return manager_to_string(self)

class ArmorPieceManager(models.Manager):
	def create_armor_piece(self, name, price, place, weight, defense, health, mana, energy, strength, agility, intellect, spirit):
		check = self.filter(name=name, price=price, place=place, weight=weight, defense=defense, health=health, mana=mana, energy=energy, strength=strength, agility=agility, intellect=intellect, spirit=spirit)
		if len(check) > 0:
			return check[0]
		else:
			armor_piece = self.create(name=name, price=price, place=place, weight=weight, defense=defense, health=health, mana=mana, energy=energy, strength=strength, agility=agility, intellect=intellect, spirit=spirit)
			return armor_piece

	def __str__(self):
		return manager_to_string(self)

class PlayerManager(models.Manager):
	def create_player(self, pseudo, classe, level, experience, health, mana, energy, strength, agility, intellect, spirit):
		check = self.filter(pseudo=pseudo, classe=classe, level=level, experience=experience, health=health, mana=mana, energy=energy, strength=strength, agility=agility, intellect=intellect, spirit=spirit)
		if len(check) > 0:
			return check[0]
		else:
			player = self.create(pseudo=pseudo, classe=classe, level=level, experience=experience, health=health, mana=mana, energy=energy, strength=strength, agility=agility, intellect=intellect, spirit=spirit)
			return player

	def __str__(self):
		return manager_to_string(self)

class PlayerArmorManager(models.Manager):
	def create_player_armor(self, player, armor):
		check = self.filter(player=player, armor=armor)
		if len(check) > 0:
			return check[0]
		else:
			player_armor = self.create(player=player, armor=armor)
			return player_armor

	def __str__(self):
		return manager_to_string(self)
