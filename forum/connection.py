#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: cnicolas
# @Date:   2015-10-22 10:16:35
# @Last Modified by:   cnicolas
# @Last Modified time: 2015-11-25 16:22:10

import logging

from django.utils import timezone
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from forum.models import Profile, Post, UnreadPost
from forum.forms import SubscribeForm
from forum.views import myRender

logger = logging.getLogger(__name__)

# anonymous_required decorator
# https://tudorbarbu.ninja/django-anonymous_required-decorator/
# https://djangosnippets.org/snippets/1849/
def anonymous_required(view_function, redirect_to=None):
    return AnonymousRequired(view_function, redirect_to)

class AnonymousRequired(object):
    def __init__(self, view_function, redirect_to):
        if redirect_to is None:
            redirect_to = "/"
        self.view_function = view_function
        self.redirect_to = redirect_to

    def __call__(self, request, *args, **kwargs):
        if request.user is not None and request.user.is_authenticated():
            return redirect(self.redirect_to) 
        return self.view_function(request, *args, **kwargs)

""" --------------------------------- VIEWS --------------------------------- """

@anonymous_required
def subscribe(request):
	context = {"pagetitle": "Inscription"}
	if request.method == "GET":
		form = SubscribeForm()
		context['form'] = form
		return myRender(request, "subscribe.html", context)
	else:
		form = SubscribeForm(request.POST)
		context['form'] = form

		if form.is_valid():
			logger.debug("Subscription form is valid")

			username = form.cleaned_data['username']
			email = form.cleaned_data['email']
			password = form.cleaned_data['password']
			confirm = form.cleaned_data['confirm_password']

			if User.objects.filter(username=username).exists():
				context["error"] = "Le nom d'utilisateur existe déjà ! Ré-essayez !"
				logger.error("Username already present in database")
			elif User.objects.filter(email=email).exists():
				context["error"] = "L'email est déjà utilisé ! Ré-essayez !"
				logger.error("Email already present in database")
			elif confirm != password:
				context["error"] = "Les mots de passe ne correspondent pas ! Ré-essayez !"
				logger.error("Passwords does not match")
			else:
				user = User.objects.create_user(username=username, email=email, password=password)
				# login(request, user)
				logger.info("New user created : " + str(user))
				return redirect('forumindex')

		return myRender(request, "subscribe.html", context)

@anonymous_required
def connect(request, ref):
	if request.method == "POST":
		logger.debug("POST connect")
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)

		if user is not None:

			if user.is_active:
				login(request, user)
				logger.debug(str(user) + " has logged in")
				profiles = Profile.objects.filter(user=user)

				if profiles.exists():
					logger.debug(str(user) + " has a profile")
					profile = profiles[0]
					last_login_datetime = profile.previous_login
					posts = Post.objects.filter(~Q(profile=profile))

					for post in posts:
						date_creation_post = post.date_creation

						if last_login_datetime < date_creation_post:
							UnreadPost.objects.create_unread_post(profile, post)
					logger.debug("Unread posts initialized")

					if ref == '/forumError/':
						return redirect('index')
					return redirect(ref)

				else:
					logger.debug(str(user) + " has no profile, redirecting...")
					return redirect('profile')

			else:
				logger.debug(str(user) + " is not active")
				return HttpResponse(content="Compte désactivé")

		else:
			logger.debug("Bad authentication")
			return redirect('indexError')

	else:
		return redirect("index")

def indexError(request):
	context = {'pagetitle': 'Accueil', 'error': "Mauvais nom d'utilisateur ou mauvais mot de passe"}
	if request.user.is_authenticated():
		profiles = Profile.objects.filter(user=request.user)
		if profiles.exists():
			context['profile'] = profiles[0]
		else:
			logger.warn("Pas de profil")
	return myRender(request, 'index.html', context)

@login_required(login_url="/forum")
def disconnect(request, ref):
	try:
		profile = Profile.objects.get(user=request.user)
		profile.previous_login = timezone.now()
		profile.save()
	except ObjectDoesNotExist:
		pass
	logout(request)
	return redirect(ref)