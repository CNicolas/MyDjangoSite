#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Aku
# @Date:   2015-11-20 14:32:30
# @Last Modified by:   cnicolas
# @Last Modified time: 2015-11-25 12:04:38

import logging
import json

from os import listdir
from os.path import isfile, join
from django.http import HttpResponse, JsonResponse

from battle.models import ArmorPiece
from battle.dtos import ArmorPieceDto

def armor(request, piece_id):
	piece = ArmorPiece.objects.get(id=piece_id)
	res = ArmorPieceDto(piece).toDictionnary()
	return JsonResponse(res)

def fillDb(request):
	database_path = "./battle/static/database"
	listDirs = listdir(database_path)
	onlyfiles = [f for f in listDirs if isfile(join(database_path, f))]
	onlyfiles = ", ".join(onlyfiles)
	return HttpResponse(onlyfiles)