#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: cnicolas
# @Date:   2015-10-21 09:40:15
# @Last Modified by:   cnicolas
# @Last Modified time: 2015-10-29 10:18:06

from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

from forum.storage import OverwriteStorage
from forum.managers import ProfileManager, ThemeManager, SubThemeManager, SubjectManager, PostManager

class Profile(models.Model):
	pseudo = models.CharField(max_length=100, default='', unique=True)
	firstname = models.CharField(max_length=100, default='')
	lastname = models.CharField(max_length=100, default='')
	birthdate = models.DateField(blank=True)
	image = models.ImageField(upload_to='forum/profiles/', default='profiles/Profil.jpg', storage=OverwriteStorage())

	user = models.ForeignKey(settings.AUTH_USER_MODEL)

	objects = ProfileManager()

	def __str__(self):
		return "Profile(pseudo={0}, firstname={1}, lastname={2}, birthdate={3}, image={4})".format(self.pseudo, self.firstname, self.lastname, self.birthdate, self.image)

class Theme(models.Model):
	title = models.CharField(max_length=100, unique=True)

	objects = ThemeManager()

	def __str__(self):
		return "Theme{id=%s, title=%s}" % (self.id, self.title)

class SubTheme(models.Model):
	title = models.CharField(max_length=100, unique=True)

	theme = models.ForeignKey(Theme)

	objects = SubThemeManager()

	def __str__(self):
		return "SubTheme{id=%s, theme=%s, title=%s}" % (self.id, self.theme, self.title)

class Subject(models.Model):
	title = models.CharField(max_length=100, unique=True)

	theme = models.ForeignKey(Theme)
	subtheme = models.ForeignKey(SubTheme)

	objects = SubjectManager()

	def __str__(self):
		return "Subject{id=%s, theme=%s, subtheme=%s, title=%s}" % (self.id, self.theme, self.subtheme, self.title)

class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	date_creation = models.DateTimeField(auto_now_add=True)
	date_modification = models.DateTimeField(auto_now=True)

	theme = models.ForeignKey(Theme)
	subtheme = models.ForeignKey(SubTheme)
	subject = models.ForeignKey(Subject)
	profile = models.ForeignKey(Profile)

	objects = PostManager()

	def __str__(self):
		#.strftime("%d/%b/%Y %H:%M:%S")
		return "Post(id={0}, theme={1}, subject={2}, profile={3}, title={4}, content={5}, date_creation={6}, date_modification={7})".format(self.id, self.theme, self.subtheme, self.subject, self.profile, self.title, self.content, str(self.date_creation), str(self.date_modification))
		# return "Post(id={0}, theme={1}, subject={2}, profile={3}, title={4})".format(self.id, self.theme, self.subtheme, self.subject, self.profile, self.title)
