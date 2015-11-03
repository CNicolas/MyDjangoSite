#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: cnicolas
# @Date:   2015-10-22 10:16:35
# @Last Modified by:   cnicolas
# @Last Modified time: 2015-11-03 10:57:36

import logging

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from forum.models import Profile
from forum.forms import SubscribeForm

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
		return render(request, "subscribe.html", context)
	else:
		form = SubscribeForm(request.POST)
		context['form'] = form
		logger.debug(form)

		username = request.POST.get("username")
		email = request.POST.get("email")
		password = request.POST.get("password")
		confirm = request.POST.get("confirm-password")

		if User.objects.filter(username=username).exists():
			context["error"] = "Le nom d'utilisateur existe déjà ! Ré-essayez !"
			logger.error("Username already present in database")
		elif User.objects.filter(email=email).exists():
			context["error"] = "L'email est déjà utilisé ! Ré-essayez !"
			logger.error("Email already present in database")
		elif confirm != password:
			context["error"] = "Les mots de passes ne correspondent pas ! Ré-essayez !"
			logger.error("Passwords does not match")
		else:
			user = User.objects.create_user(username=username, email=email, password=password)
			login(request, user)
			return redirect("index")

		return render(request, "subscribe.html", context)

@anonymous_required
def connect(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				profiles = Profile.objects.filter(user=user)
				if profiles.exists():
					return redirect("index")
				else:
					return redirect("profile")
			else:
				return HttpResponse(content="Compte désactivé")
		else:
			return HttpResponse(content="Bad Login !")
	return redirect("index")

@login_required(login_url="/forum")
def disconnect(request):
	logout(request)
	return redirect("index")