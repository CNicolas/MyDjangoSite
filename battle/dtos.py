#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: cnicolas
# @Date:   2015-11-19 16:37:40
# @Last Modified by:   cnicolas
# @Last Modified time: 2015-11-19 16:54:57

from battle.models import AttackByClasse, PlayerArmor, Player

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

		abc = AttackByClasse.objects.filter(classe=self.classe)
		pa = PlayerArmor.objects.filter(player=player)

		self.attacks = list(abc)
		self.armors = list(pa)