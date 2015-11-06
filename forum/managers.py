#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: cnicolas
# @Date:   2015-10-21 09:40:15
# @Last Modified by:   cnicolas
# @Last Modified time: 2015-11-05 10:06:34

from django.db import models

def managerToString(manager):
	objects = manager.all()
	if not objects:
		return "[]"
	res = "[ "
	for obj in objects:
		res += str(obj) + ", "
	res = res[:-2] + " ]"
	return res

class ProfileManager(models.Manager):
	def create_profile(self, user, pseudo, firstname, lastname, birthdate, image=None, previous_login=None):
		profile = self.create(user=user, pseudo=pseudo, firstname=firstname, lastname=lastname, birthdate=birthdate, image=image, previous_login=previous_login)
		return profile

	def __str__(self):
		return managerToString(self)

class ThemeManager(models.Manager):
	def create_theme(self, title):
		theme = self.create(title=title)
		return theme

	def __str__(self):
		return managerToString(self)

class SubThemeManager(models.Manager):
	def create_subtheme(self, theme, title):
		subtheme = self.create(theme=theme, title=title)
		return subtheme

	def __str__(self):
		return managerToString(self)

class SubjectManager(models.Manager):
	def create_subject(self, subtheme, title):
		subject = self.create(theme=subtheme.theme, subtheme=subtheme, title=title)
		return subject

	def __str__(self):
		return managerToString(self)

class PostManager(models.Manager):
	def create_post(self, subject, profile, title, content):
		post = self.create(theme=subject.subtheme.theme, subtheme=subject.subtheme, subject=subject, profile=profile, title=title, content=content)
		return post

	def __str__(self):
		return managerToString(self)

class UnreadPostManager(models.Manager):
	def create_unread_post(self, profile, post):
		unread_post = self.create(profile=profile, post=post, subject=post.subject)
		return unread_post

	def __str__(self):
		return managerToString(self)