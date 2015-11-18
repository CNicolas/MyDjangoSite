#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: cnicolas
# @Date:   2015-10-29 11:20:22
# @Last Modified by:   cnicolas
# @Last Modified time: 2015-11-18 14:18:15

import logging

from django.shortcuts import render, redirect

from forum.views import myRender

logger = logging.getLogger(__name__)

def error_404(request):
	context = {'pagetitle': 'Page non trouvée', 'referer': request.META.HTTP_REFERER, 'message': "La page que vous cherchez n'éxiste pas !"}
	return myRender(request, 'error.html', context)

def error_500(request):
	context = {'pagetitle': 'Erreur serveur', 'message': "Une erreur côté serveur est apparue !"}
	return myRender(request, 'error.html', context)