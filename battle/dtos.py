#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: cnicolas
# @Date:   2015-11-19 16:37:40
# @Last Modified by:   Aku
# @Last Modified time: 2015-11-20 11:52:08

import logging

from battle.models import AttackByClasse, PlayerArmor, Player

logger = logging.getLogger(__name__)

class AttackDto:
	def __init__(self, player):
		pass

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
		self.armors = [a.armor for a in pa]

		self.armor_head = self.find_armor_by_place("Head")
		self.armor_torso = self.find_armor_by_place("Torso")
		self.armor_feet = self.find_armor_by_place("Feet")
		self.weapon = self.find_armor_by_place("Weapon")

	def find_armor_by_place(self, place):
		for a in self.armors:
			if a.category.place == place:
				return a
		return False