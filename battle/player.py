#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: cnicolas
# @Date:   2015-11-24 16:41:06
# @Last Modified by:   cnicolas
# @Last Modified time: 2015-11-24 16:45:53

import logging

from battle.models import Player
from battle.dtos import PlayerDto
from battle.utils import myRender

logger = logging.getLogger(__name__)

def player_view(request, player_pseudo):
	player = Player.objects.get(pseudo=player_pseudo)
	context = {'pagetitle': 'Joueur', 'player': PlayerDto(player)}
	return myRender(request, 'player.html', context)

def shop(request):
	context = {'pagetitle': 'Magasin'}
	return myRender(request, 'shop.html', context)
