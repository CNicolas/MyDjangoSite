#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: cnicolas
# @Date:   2015-10-22 11:41:58
# @Last Modified by:   cnicolas
# @Last Modified time: 2015-11-03 11:03:23

import dateutil.parser
import hashlib
import requests
import logging
import os

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from forum.models import Profile
from forum.forms import ProfileForm

logger = logging.getLogger(__name__)

@login_required(login_url="/forum")
def profile(request):
	if request.method == "GET":
		return profileGet(request)
	else:
		return profilePost(request)

def profileGet(request):
	profiles = Profile.objects.filter(user=request.user)
	imageurl = 'forum/profiles/Profil.jpg'
	if profiles:
		profile = profiles[0]
		form = ProfileForm(initial={'pseudo' : profile.pseudo, 'firstname' : profile.firstname, 'lastname' : profile.lastname, 'birthdate' : profile.birthdate})
		imageurl = profile.image.url if profile.image else 'forum/profiles/Profil.jpg'
		context = {'pagetitle': 'Profil'}
	else:
		form = ProfileForm()
		context = {"pagetitle": "Première connexion"}
	context['imageurl'] = imageurl
	context['form'] = form
	context['background_color'] = 'white'
	return render(request, "profile.html", context)

def profilePost(request):
	user = request.user
	form = ProfileForm(request.POST, request.FILES)

	if form.is_valid():
		profiles = Profile.objects.filter(user=user)
		context = {'pagetitle': 'Profil', 'success': "Votre profil a bien été mis à jour !", 'form': form, 'background_color': 'white'}

		if profiles.exists():
			profile = profiles[0]
			profile.pseudo = form.cleaned_data['pseudo']
			profile.firstname = form.cleaned_data['firstname']
			profile.lastname = form.cleaned_data['lastname']
			profile.birthdate = form.cleaned_data['birthdate']

			if form.cleaned_data['image'] is not None:
				form.cleaned_data['image'].name = profile.pseudo + '.' + form.cleaned_data['image'].name.split('.')[1].lower()
				profile.image = form.cleaned_data['image']

			profile.save()
		else:
			if Profile.objects.filter(pseudo=form.cleaned_data['pseudo']).exists():
				context = {'pagetitle': 'Première connexion', 'error': "Le pseudo est déjà utilisé", 'form': form}
				return render(request, "profile.html", context)
			else:
				profile = Profile.objects.create_profile(user, form.cleaned_data['pseudo'], form.cleaned_data['firstname'], form.cleaned_data['lastname'], form.cleaned_data['birthdate'], form.cleaned_data['image'])

		if profile.image:
			context['imageurl'] = profile.image.url
		else:
			context['imageurl'] = 'forum/profiles/Profil.jpg'
		return render(request, "profile.html", context)
		
	else:
		return redirect("profile")
