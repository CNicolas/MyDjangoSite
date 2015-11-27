#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Aku
# @Date:   2015-11-20 14:32:30
# @Last Modified by:   cnicolas
# @Last Modified time: 2015-11-26 11:37:25

import logging
import json

from os import listdir
from os.path import isfile, join
from django.http import HttpResponse, JsonResponse

from battle.models import Classe, Attack, AttackByClasse, ArmorPiece, Player, PlayerArmor, Ennemy, EnnemyAttack
from battle.dtos import ArmorPieceDto
from battle.utils import armorWeightByName

logger = logging.getLogger(__name__)
database_path = join('.', 'battle', 'static', 'json')

# API
def armor(request, piece_id):
	piece = ArmorPiece.objects.get(id=piece_id)
	res = ArmorPieceDto(piece).toDictionnary()
	return JsonResponse(res)
# END

# EMPTY DB
def emptyClassesAndAttacks(request):
	Classe.objects.all().delete()
	Attack.objects.all().delete()
	AttackByClasse.objects.all().delete()

def emptyPlayersAndArmors(request):
	ArmorPiece.objects.all().delete()
	Player.objects.all().delete()
	PlayerArmor.objects.all().delete()

def emptyEnnemies(request):
	Ennemy.objects.all().delete()
	EnnemyAttack.objects.all().delete()

def emptyDb(request):
	emptyClassesAndAttacks(request)
	emptyPlayersAndArmors(request)
	emptyEnnemies(request)
	return HttpResponse("Everything has been deleted")
# END

# INIT DB
def initPlayersAndArmors(request):
	items_file = join(database_path, 'items.json')
	with open(items_file, 'r', encoding='utf-8') as f:
		data = json.load(f)
		for weight in data:
			for place in data[weight]:
				for piece in data[weight][place]:
					ArmorPiece.objects.create_armor_piece(piece['name'], piece['price'], place, weight, piece['defense'], piece['health'], piece['mana'], piece['energy'], piece['strength'], piece['agility'], piece['intellect'], piece['spirit'])

def initClassesAndAttacks(request):
	attacks_file = join(database_path, 'attacks.json')
	with open(attacks_file, 'r', encoding='utf-8') as f:
		data = json.load(f)
		for weight in data:
			for classname in data[weight]:
				classe_content = data[weight][classname]
				c = Classe.objects.create_classe(classname, weight, classe_content['health'])
				for attack in classe_content['attacks']:
					a = Attack.objects.create_attack(attack['name'], attack['damage'], attack['heal'], attack['mana'], attack['energy'], attack['critical'], attack['duration'], attack['target'], attack['cooldown'], attack['stat'], attack['symbol'], attack['acronym'])
					AttackByClasse.objects.create_attack_by_classe(c, a)

def initEnnemies(request):
	ennemies_file = join(database_path, 'ennemies.json')
	with open(ennemies_file, 'r', encoding='utf-8') as f:
		data = json.load(f)
		for e in data:
			ennemy = Ennemy.objects.create_ennemy(e['name'], e['level'], e['health'])
			for a in e['attacks']:
				attack = EnnemyAttack.objects.create_ennemy_attack(a['name'], a['damage'], a['heal'], a['critical'], a['duration'], a['cooldown'], a['target'], a['symbol'], a['acronym'], ennemy)

def initDb(request):
	initPlayersAndArmors(request)
	initClassesAndAttacks(request)
	initEnnemies(request)
	return HttpResponse("Database initialized")
# END

# REINIT DB
def reinitPlayersAndArmors(request):
	emptyPlayersAndArmors(request)
	initPlayersAndArmors(request)
	return HttpResponse("Armors deleted AND re-created")

def reinitClassesAndAttacks(request):
	emptyClassesAndAttacks(request)
	initClassesAndAttacks(request)
	return HttpResponse("Classes and Attacks deleted AND re-created")

def reinitEnnemies(request):
	emptyEnnemies(request)
	initEnnemies(request)
	return HttpResponse("Ennemies deleted AND re-created")

def reinitDb(request):
	emptyDb(request)
	fillDb(request)
	return HttpResponse("Everything has been deleted AND re-created")
# END
