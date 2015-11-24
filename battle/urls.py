#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: cnicolas
# @Date:   2015-11-10 16:55:44
# @Last Modified by:   cnicolas
# @Last Modified time: 2015-11-24 16:45:17

from django.conf.urls import url

from battle import views, player, database_requests

urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name='battleindex'),

	url(r'^player/(?P<player_pseudo>\w{0,50})/$', player.player_view, name='player'),
	url(r'^shop/$', player.shop, name='shop'),

	url(r'^armor/(?P<piece_id>\d{0,50})/$', database_requests.armor, name='armor'),

	url(r'^test/$', views.test, name='test'),
	url(r'^show/$', views.show, name='show'),
]
