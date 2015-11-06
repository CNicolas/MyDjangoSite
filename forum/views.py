#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: cnicolas
# @Date:   2015-10-21 09:40:15
# @Last Modified by:   cnicolas
# @Last Modified time: 2015-11-06 14:50:36

import logging
import os

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User

from forum.models import Profile, Theme, SubTheme, Subject, Post, UnreadPost
from forum.forms import ProfileForm

logger = logging.getLogger(__name__)

def index(request):
	context = {'pagetitle': 'Accueil'}
	if request.user.is_authenticated():
		profiles = Profile.objects.filter(user=request.user)
		if profiles.exists():
			context['profile'] = profiles[0]
		else:
			logger.error("Pas de profil")
	return render(request, 'index.html', context)

def fullDB(request):
	# t1 = Theme.objects.create_theme("Informations Générales")
	# t2 = Theme.objects.create_theme("Système Solaire")
	# t3 = Theme.objects.create_theme("Voie Lactée")
	# t4 = Theme.objects.create_theme("Autres Galaxies")
	# t5 = Theme.objects.create_theme("Extraterrestres et autres discussions peu conventionnelles")
	
	# st1 = SubTheme.objects.create_subtheme(t1, "A LIRE AVANT DE POSTER !")
	# st2 = SubTheme.objects.create_subtheme(t1, "Charte du forum")
	# st3 = SubTheme.objects.create_subtheme(t2, "Mercure")
	# st4 = SubTheme.objects.create_subtheme(t2, "Vénus")
	# st5 = SubTheme.objects.create_subtheme(t2, "Terre")
	# st6 = SubTheme.objects.create_subtheme(t2, "Mars")
	# st7 = SubTheme.objects.create_subtheme(t2, "Jupiter")
	# st8 = SubTheme.objects.create_subtheme(t2, "Saturne")
	# st9 = SubTheme.objects.create_subtheme(t2, "Uranus")
	# st10 = SubTheme.objects.create_subtheme(t2, "Neptune")
	# st11 = SubTheme.objects.create_subtheme(t5, "Actualités")
	# st12 = SubTheme.objects.create_subtheme(t5, "Martiens")
	# st13 = SubTheme.objects.create_subtheme(t5, "Contacts")
	# st14 = SubTheme.objects.create_subtheme(t5, "Aliens en tout genre")
	# st15 = SubTheme.objects.create_subtheme(t5, "Preuves potentielles d'existence")

	# s1 = Subject.objects.create_subject(st1, "Vos devoirs pour chaque post")
	# s2 = Subject.objects.create_subject(st5, "Réchauffement climatique")
	# s3 = Subject.objects.create_subject(st5, "Tremblement de Terre au Népal")
	# s4 = Subject.objects.create_subject(st5, "Fukushima")
	# s5 = Subject.objects.create_subject(st5, "Alignement de Jupiter et Vénus")
	# s6 = Subject.objects.create_subject(st5, "La glace du pôle nord")
	# s7 = Subject.objects.create_subject(st5, "Eruption d'Eyjafjallajökull en 2010")
	
	# profile_toto = Profile.objects.get(pseudo='Toto')
	# profile_titi = Profile.objects.get(pseudo='Titi')
	# p1 = Post.objects.create_post(s1, profile_toto, "Sérieux", "Soyez respectueux vis-à-vis des autres, et tout ira bien !")
	# p2 = Post.objects.create_post(s1, profile_titi, "", "Moi je veux pas, je fais comment ?")
	# p3 = Post.objects.create_post(s1, profile_toto, "Réponse à l'autre utilisateur", "C'est la même chose, tu ne pourras plus poster !")
	# p4 = Post.objects.create_post(s1, profile_titi, "Je veux pas mettre de titre", "Maieuh !")

	return HttpResponse(Subject.objects)

def test(request):
	theme = Theme.objects.get(title="Extraterrestres et autres discussions peu conventionnelles")
	SubTheme.objects.create_subtheme(theme, "Actualités")
	SubTheme.objects.create_subtheme(theme, "Martiens")
	SubTheme.objects.create_subtheme(theme, "Contacts")
	SubTheme.objects.create_subtheme(theme, "Aliens en tout genre")
	SubTheme.objects.create_subtheme(theme, "Preuves potentielles d'existence")
	return HttpResponse(SubTheme.objects)

def deleteForum(request):
	# Post.objects.all().delete()
	# Subject.objects.all().delete()
	# SubTheme.objects.all().delete()
	# Theme.objects.all().delete()
	# Profile.objects.all().delete()
	# UnreadPost.objects.all().delete()
	return HttpResponse(Profile.objects.get(pseudo='Toto').user.email)
