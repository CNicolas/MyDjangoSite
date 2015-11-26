#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: cnicolas
# @Date:   2015-11-24 16:41:06
# @Last Modified by:   cnicolas
# @Last Modified time: 2015-11-24 16:45:53

import logging

from battle.models import Player, Ennemy
from battle.dtos import PlayerDto, EnnemyDto
from battle.utils import myRender

def fight(request):
    player1 = Player.objects.get(pseudo='Aku_Guerrier')
    ennemy1 = Ennemy.objects.get(name='Sephiroth')

    players = [PlayerDto(player1), PlayerDto(player1), PlayerDto(player1)]
    ennemies = [EnnemyDto(ennemy1)]
    context = {'pagetitle': 'Combat', 'players': players, 'ennemies': ennemies}
    return myRender(request, 'fight.html', context)
