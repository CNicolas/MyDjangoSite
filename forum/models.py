#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: cnicolas
# @Date:   2015-10-21 09:40:15
# @Last Modified by:   cnicolas
# @Last Modified time: 2015-11-19 14:20:58

from django.db import models
from django.conf import settings

from forum.storage import OverwriteStorage
from forum.managers import ProfileManager, ThemeManager, SubThemeManager, SubjectManager, PostManager, UnreadPostManager

class Profile(models.Model):
	pseudo = models.CharField(max_length=100, default='', unique=True)
	firstname = models.CharField(max_length=100, default='')
	lastname = models.CharField(max_length=100, default='')
	birthdate = models.DateField(blank=True)
	image = models.ImageField(upload_to='forum/profiles/', default='profiles/Profil.jpg', storage=OverwriteStorage())
	previous_login = models.DateTimeField(blank=True)

	user = models.ForeignKey(settings.AUTH_USER_MODEL)

	objects = ProfileManager()

	def __str__(self):
		return "Profile(pseudo={0}, firstname={1}, lastname={2}, birthdate={3}, image={4}, previous_login={5})".format(self.pseudo, self.firstname, self.lastname, self.birthdate, self.image, self.previous_login)

class Theme(models.Model):
	title = models.CharField(max_length=100, unique=True)

	objects = ThemeManager()

	def __str__(self):
		return "Theme(id={0}, title={1})".format(self.id, self.title)

class SubTheme(models.Model):
	title = models.CharField(max_length=100, unique=True)

	theme = models.ForeignKey(Theme)

	objects = SubThemeManager()

	def __str__(self):
		return "SubTheme(id={0}, theme={1}, title={2})".format(self.id, self.theme, self.title)

class Subject(models.Model):
	title = models.CharField(max_length=100, unique=True)

	theme = models.ForeignKey(Theme)
	subtheme = models.ForeignKey(SubTheme)

	objects = SubjectManager()

	def __str__(self):
		return "Subject(id={0}, theme={1}, subtheme={2}, title={3})".format(self.id, self.theme, self.subtheme, self.title)

class Post(models.Model):
	title = models.CharField(max_length=100, default='')
	content = models.TextField()
	date_creation = models.DateTimeField(auto_now_add=True)
	date_modification = models.DateTimeField(auto_now=True)

	theme = models.ForeignKey(Theme)
	subtheme = models.ForeignKey(SubTheme)
	subject = models.ForeignKey(Subject)
	profile = models.ForeignKey(Profile)

	objects = PostManager()

	def __str__(self):
		return "Post(id={0}, theme={1}, subject={2}, profile={3}, title={4}, content={5}, date_creation={6}, date_modification={7})".format(self.id, self.theme, self.subtheme, self.subject, self.profile, self.title, self.content, str(self.date_creation), str(self.date_modification))

class UnreadPost(models.Model):
	profile = models.ForeignKey(Profile)
	post = models.ForeignKey(Post)
	subject = models.ForeignKey(Subject)

	objects = UnreadPostManager()

	def __str__(self):
		return "UnreadSubject(id={0}, profile={1}, post={2}, subject={3})".format(self.id, self.profile, self.post, self.subject)