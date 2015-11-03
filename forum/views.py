#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: cnicolas
# @Date:   2015-10-21 09:40:15
# @Last Modified by:   cnicolas
# @Last Modified time: 2015-10-29 16:53:22

import logging
import os

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User

from forum.models import Profile, Theme, SubTheme, Subject, Post
from forum.forms import ProfileForm

logger = logging.getLogger(__name__)

def index(request):
	context = {'pagetitle': 'Accueil', 'background_color': 'white'}
	if request.user.is_authenticated():
		profiles = Profile.objects.filter(user=request.user)
		if profiles.exists():
			context['profile'] = profiles[0]
		else:
			logger.error("Pas de profile")
	return render(request, 'index.html', context)

def test(request):
	# t1 = Theme.objects.create_theme("Informations Générales")
	# t2 = Theme.objects.create_theme("Système Solaire")
	# Theme.objects.create_theme("Voie Lactée")
	# Theme.objects.create_theme("Autres Galaxies")
	# Theme.objects.create_theme("Extraterrestres et autres discussions peu conventionnelles")
	
	# st1 = SubTheme.objects.create_subtheme(t1, "A LIRE AVANT DE POSTER !")
	# SubTheme.objects.create_subtheme(t1, "Charte du forum")
	# SubTheme.objects.create_subtheme(t2, "Mercure")
	# SubTheme.objects.create_subtheme(t2, "Vénus")
	# st5 = SubTheme.objects.create_subtheme(t2, "Terre")
	# SubTheme.objects.create_subtheme(t2, "Mars")
	# SubTheme.objects.create_subtheme(t2, "Jupiter")
	# SubTheme.objects.create_subtheme(t2, "Saturne")
	# SubTheme.objects.create_subtheme(t2, "Uranus")
	# SubTheme.objects.create_subtheme(t2, "Neptune")

	# s1 = Subject.objects.create_subject(st1, "Vos devoirs pour chaque post")
	# Subject.objects.create_subject(st5, "Réchauffement climatique")
	# Subject.objects.create_subject(st5, "Tremblement de Terre au Népal")
	# Subject.objects.create_subject(st5, "Fukushima")
	# Subject.objects.create_subject(st5, "Alignement de Jupiter et Vénus")
	# Subject.objects.create_subject(st5, "La glace du pôle nord")
	# Subject.objects.create_subject(st5, "Eruption d'Eyjafjallajökull en 2010")

	# s1 = Subject.objects.get(title="Vos devoirs pour chaque post")
	# profile_toto = Profile.objects.get(pseudo='Toto')
	# profile_titi = Profile.objects.get(pseudo='Titi')
	# Post.objects.create_post(s1, profile_toto, "Sérieux", "Soyez respectueux vis-à-vis des autres, et tout ira bien !")
	# Post.objects.create_post(s1, profile_titi, "", "Moi je veux pas, je fais comment ?")
	# Post.objects.create_post(s1, profile_toto, "Réponse à l'autre utilisateur", "C'est la même chose, tu ne pourras plus poster !")
	# Post.objects.create_post(s1, profile_titi, "Je veux pas mettre de titre", "Maieuh !")

	return HttpResponse(Subject.objects)
	# return HttpResponse(str(Theme.objects) + str(SubTheme.objects) + str(Subject.objects) + str(Post.objects))

def deleteForum(request):
	# Post.objects.all().delete()
	# Subject.objects.all().delete()
	# SubTheme.objects.all().delete()
	# Theme.objects.all().delete()
	# Profile.objects.all().delete()
	return HttpResponse(Profile.objects)
