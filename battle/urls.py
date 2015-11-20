#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: cnicolas
# @Date:   2015-11-10 16:55:44
# @Last Modified by:   Aku
# @Last Modified time: 2015-11-20 14:35:23

from django.conf.urls import url

from battle import views, database_requests

urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name='battleindex'),

	url(r'^player/(?P<player_pseudo>\w{0,50})/$', views.player_view, name='player'),

	url(r'^armor/(?P<piece_id>\d{0,50})/$', database_requests.armor, name='armor'),

	url(r'^test/$', views.test, name='test'),
	url(r'^show/$', views.show, name='show'),
]
