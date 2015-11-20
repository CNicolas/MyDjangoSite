#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Aku
# @Date:   2015-11-20 14:32:30
# @Last Modified by:   Aku
# @Last Modified time: 2015-11-20 14:45:33

import logging
import json

from django.http import HttpResponse, JsonResponse

from battle.models import ArmorPiece
from battle.dtos import ArmorPieceDto

def armor(request, piece_id):
	piece = ArmorPiece.objects.get(id=piece_id)
	res = ArmorPieceDto(piece).toDictionnary()
	return JsonResponse(res)