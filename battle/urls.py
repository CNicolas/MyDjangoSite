#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: cnicolas
# @Date:   2015-11-10 16:55:44
# @Last Modified by:   cnicolas
# @Last Modified time: 2015-11-18 14:23:45

from django.conf.urls import url

from battle import views

urlpatterns = [
	# url(r'^$', views.index, name='battleindex'),
	url(r'^$', views.IndexView.as_view(), name='battleindex'),
]
