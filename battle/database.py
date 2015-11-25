#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Aku
# @Date:   2015-11-20 14:32:30
# @Last Modified by:   cnicolas
# @Last Modified time: 2015-11-25 15:45:21

import logging
import json

from os import listdir
from os.path import isfile, join
from django.http import HttpResponse, JsonResponse

from battle.models import Classe, Attack, AttackByClasse, ArmorPiece, Player, PlayerArmor
from battle.dtos import ArmorPieceDto
from battle.utils import armorWeightByName

logger = logging.getLogger(__name__)

def armor(request, piece_id):
	piece = ArmorPiece.objects.get(id=piece_id)
	res = ArmorPieceDto(piece).toDictionnary()
	return JsonResponse(res)

def fillDb(request):
	database_path = join('.', 'battle', 'static', 'database')
	items_file = join(database_path, 'items.json')
	attacks_file = join(database_path, 'attacks.json')

	with open(items_file, 'r', encoding='utf-8') as f:
		data = json.load(f)
		for weight in data:
			for place in data[weight]:
				for piece in data[weight][place]:
					ArmorPiece.objects.create_armor_piece(piece['name'], piece['price'], place, weight, piece['defense'], piece['health'], piece['mana'], piece['energy'], piece['strength'], piece['agility'], piece['intellect'], piece['spirit'])

	with open(attacks_file, 'r', encoding='utf-8') as f:
		data = json.load(f)
		for weight in data:
			for classname in data[weight]:
				c = Classe.objects.create_classe(classname, weight, data[weight][classname]['health'])
				for attack in data[weight][classname]['attacks']:
					print(attack['name'], attack['damage'], attack['heal'], attack['mana'], attack['energy'], attack['critical'], attack['duration'], attack['target'])
					a = Attack.objects.create_attack(attack['name'], attack['damage'], attack['heal'], attack['mana'], attack['energy'], attack['critical'], attack['duration'], attack['target'])
					AttackByClasse.objects.create_attack_by_classe(c, a)


	return HttpResponse()

def emptyDb(request):
	Classe.objects.all().delete()
	Attack.objects.all().delete()
	AttackByClasse.objects.all().delete()
	ArmorPiece.objects.all().delete()
	Player.objects.all().delete()
	PlayerArmor.objects.all().delete()
	return HttpResponse()