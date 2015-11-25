#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: cnicolas
# @Date:   2015-11-25 13:27:55
# @Last Modified by:   cnicolas
# @Last Modified time: 2015-11-25 14:09:16

import json

from django.shortcuts import render
from django.http import HttpResponse

armorWeightByName = {'light': 1, 'medium': 2, 'heavy': 3}
armorWeightByWeight = {1: 'light', 2: 'medium', 3: 'heavy'}

def myRender(request, template, context):
	return render(request, 'battle/' + template, context)
