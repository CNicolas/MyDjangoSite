#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: cnicolas
# @Date:   2015-11-10 16:55:44
# @Last Modified by:   cnicolas
# @Last Modified time: 2015-11-26 13:38:08

from django.conf.urls import url

from battle import views, player, fight, database

urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name='battleindex'),

	url(r'^player/(?P<player_pseudo>\w{0,50})/$', player.player_view, name='player'),
	url(r'^shop/$', player.shop, name='shop'),
	url(r'^fight/$', fight.fight, name='fight'),

	url(r'^armor/(?P<piece_id>\d{0,50})/$', database.armor, name='armor'),
	url(r'^emptyDb/$', database.emptyDb, name='emptyDb'),
	url(r'^initDb/$', database.initDb, name='initDb'),
	url(r'^reinitDb/$', database.reinitDb, name='reinitDb'),
	url(r'^emptyAttacks/$', database.emptyClassesAndAttacks, name='emptyAttacks'),
	url(r'^initAttacks/$', database.initClassesAndAttacks, name='initAttacks'),
	url(r'^reinitAttacks/$', database.reinitClassesAndAttacks, name='reinitAttacks'),
	url(r'^emptyArmors/$', database.emptyPlayersAndArmors, name='emptyArmors'),
	url(r'^initArmors/$', database.initPlayersAndArmors, name='initArmors'),
	url(r'^reinitArmors/$', database.reinitPlayersAndArmors, name='reinitArmors'),
	url(r'^emptyEnnemies/$', database.emptyEnnemies, name='emptyEnnemies'),
	url(r'^initEnnemies/$', database.initEnnemies, name='initEnnemies'),
	url(r'^reinitEnnemies/$', database.reinitEnnemies, name='reinitEnnemies'),

	url(r'^test/$', views.test, name='test'),
	url(r'^show/$', views.show, name='show'),
]
