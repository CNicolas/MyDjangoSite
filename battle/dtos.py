#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: cnicolas
# @Date:   2015-11-19 16:37:40
# @Last Modified by:   cnicolas
# @Last Modified time: 2015-11-26 10:34:59

import logging

from battle.models import AttackByClasse, PlayerArmor, Player
from battle.utils import armorWeightByName

logger = logging.getLogger(__name__)

class ArmorPieceDto:
	def __init__(self, armor):
		self.id = armor.id
		self.name = armor.name
		self.place = armor.place
		self.weight = armor.weight
		self.price = armor.price
		self.defense = armor.defense
		self.health = armor.health
		self.mana = armor.mana
		self.energy = armor.energy
		self.strength = armor.strength
		self.intellect = armor.intellect
		self.agility = armor.agility
		self.spirit = armor.spirit

	def toDictionnary(self):
		res = {}
		res['id'] = self.id
		res['name'] = self.name
		res['place'] = self.place
		res['weight'] = self.weight
		res['price'] = self.price
		res['defense'] = self.defense
		res['health'] = self.health
		res['mana'] = self.mana
		res['strength'] = self.strength
		res['agility'] = self.agility
		res['intellect'] = self.intellect
		res['spirit'] = self.spirit
		return res

class PlayerDto:
	def __init__(self, player):
		self.id = player.id
		self.pseudo = player.pseudo
		self.level = player.level
		self.experience = player.experience
		self.health = player.health
		self.mana = player.mana
		self.energy = player.energy
		self.strength = player.strength
		self.agility = player.agility
		self.intellect = player.intellect
		self.spirit = player.spirit
		self.classe = player.classe

		self.weight = armorWeightByName[self.classe.weight]

		abc = AttackByClasse.objects.filter(classe=self.classe)
		pa = PlayerArmor.objects.filter(player=player)

		self.attacks = [a.attack for a in abc]
		self.armors = [ArmorPieceDto(a.armor) for a in pa]

		self.armor_head = self.find_armor_by_place("head")
		self.armor_torso = self.find_armor_by_place("torso")
		self.armor_hand = self.find_armor_by_place("hand")
		self.armor_neck = self.find_armor_by_place("neck")
		self.armor_feet = self.find_armor_by_place("feet")
		self.weapon = self.find_armor_by_place("weapon")

		self.health_bonus = sum(a.health for a in self.armors) + self.classe.health
		self.mana_bonus = sum(a.mana for a in self.armors)
		self.energy_bonus = sum(a.energy for a in self.armors)
		self.strength_bonus = sum(a.strength for a in self.armors)
		self.agility_bonus = sum(a.agility for a in self.armors)
		self.intellect_bonus = sum(a.intellect for a in self.armors)
		self.spirit_bonus = sum(a.spirit for a in self.armors)

		self.full_health = self.health + self.health_bonus
		self.full_mana = self.mana + self.mana_bonus
		self.full_energy = self.energy + self.energy_bonus
		self.full_strength = self.strength + self.strength_bonus
		self.full_agility = self.agility + self.agility_bonus
		self.full_intellect = self.intellect + self.intellect_bonus
		self.full_spirit = self.spirit + self.spirit_bonus		

	def find_armor_by_place(self, place):
		for a in self.armors:
			if a.place == place:
				return a
		return False
