#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: cnicolas
# @Date:   2015-11-10 16:55:44
# @Last Modified by:   cnicolas
# @Last Modified time: 2015-11-19 16:32:46

from django.conf.urls import url

from battle import views

urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name='battleindex'),

	url(r'^player/(?P<player_pseudo>\w{0,50})/$', views.player_view_pseudo, name='player'),

	url(r'^test/$', views.test, name='test'),
	url(r'^show/$', views.show, name='show'),
]
