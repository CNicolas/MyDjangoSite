#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: cnicolas
# @Date:   2015-10-29 11:20:22
# @Last Modified by:   cnicolas
# @Last Modified time: 2015-10-29 11:32:03

import logging

from django.shortcuts import render, redirect

logger = logging.getLogger(__name__)

def error_404(request):
	context = {'pagetitle': 'Page non trouvée', 'referer': request.META.HTTP_REFERER, 'message': "La page que vous cherchez n'éxiste pas !"}
	return render(request, 'error.html', context)

def error_500(request):
	context = {'pagetitle': 'Erreur serveur', 'message': "Une erreur côté serveur est apparue !"}
	return render(request, 'error.html', context)