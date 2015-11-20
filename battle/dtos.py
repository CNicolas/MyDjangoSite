#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: cnicolas
# @Date:   2015-11-19 16:37:40
# @Last Modified by:   Aku
# @Last Modified time: 2015-11-20 14:47:13

import logging

from battle.models import AttackByClasse, PlayerArmor, Player

logger = logging.getLogger(__name__)

class ArmorPieceDto:
	def __init__(self, armor):
		self.id = armor.id
		self.name = armor.name
		self.price = armor.price
		self.defense = armor.defense
		self.health = armor.health
		self.mana = armor.mana
		self.strength = armor.strength
		self.intellect = armor.intellect
		self.agility = armor.agility
		self.spirit = armor.spirit
		self.weight = armor.category.weight
		self.place = armor.category.place

	def toDictionnary(self):
		res = {}
		res['id'] = self.id
		res['name'] = self.name
		res['price'] = self.price
		res['defense'] = self.defense
		res['health'] = self.health
		res['mana'] = self.mana
		res['strength'] = self.strength
		res['agility'] = self.agility
		res['intellect'] = self.intellect
		res['spirit'] = self.spirit
		res['weight'] = self.weight
		res['place'] = self.place

		return res

class PlayerDto:
	def __init__(self, player):
		self.id = player.id
		self.pseudo = player.pseudo
		self.level = player.level
		self.experience = player.experience
		self.health = player.health
		self.mana = player.mana
		self.strength = player.strength
		self.agility = player.agility
		self.intellect = player.intellect
		self.spirit = player.spirit
		self.classe = player.classe

		self.amor_type = self.classe.armor_type

		abc = AttackByClasse.objects.filter(classe=self.classe)
		pa = PlayerArmor.objects.filter(player=player)

		self.attacks = [a.attack for a in abc]
		self.armors = [ArmorPieceDto(a.armor) for a in pa]

		self.armor_head = self.find_armor_by_place("Head")
		self.armor_torso = self.find_armor_by_place("Torso")
		self.armor_hand = self.find_armor_by_place("Hand")
		self.armor_neck = self.find_armor_by_place("Neck")
		self.armor_feet = self.find_armor_by_place("Feet")
		self.weapon = self.find_armor_by_place("Weapon")

	def find_armor_by_place(self, place):
		for a in self.armors:
			if a.place == place:
				return a
		return False