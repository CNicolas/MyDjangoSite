#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: cnicolas
# @Date:   2015-10-27 15:30:06
# @Last Modified by:   cnicolas
# @Last Modified time: 2015-11-06 14:56:28

from forum.models import Profile, Theme, SubTheme, Subject, Post

class ProfileDto:
	def __init__(self, profile):
		self.profile = profile
		self.id = profile.id
		self.pseudo = profile.pseudo
		self.firstname = profile.firstname
		self.lastname = profile.lastname
		self.birthdate = profile.birthdate
		self.image = profile.image
		self.email = profile.user.email

		self.creation = profile.user.date_joined
		self.last_login = profile.user.last_login
		self.logged = profile.user.is_authenticated()

		posts = Post.objects.filter(profile=profile)
		self.posts_number = len(posts)
		self.last_posts = list(posts)[:3]

class ThemeDto:
	def __init__(self, theme, subthemes=None):
		self.theme = theme
		self.id = theme.id
		self.title = theme.title
		if subthemes:
			self.subthemes = subthemes
		else:
			self.subthemes = SubTheme.objects.filter(theme=theme)
	def __str__(self):
		return str(self.theme)

class SubThemeDto:
	def __init__(self, subtheme, subjects=None):
		self.subtheme = subtheme
		self.id = subtheme.id
		self.title = subtheme.title
		self.theme = subtheme.theme
		if subjects:
			self.subjects = subjects
		else:
			self.subjects = Subject.objects.filter(subtheme=subtheme)
	def __str__(self):
		return str(self.subtheme)

class SubjectDto:
	def __init__(self, subject):
		self.subject = subject
		self.id = subject.id
		self.title = subject.title
		self.theme = subject.theme
		self.subtheme = subject.subtheme
		self.posts = Post.objects.filter(subject=subject)
		self.newpost = 0
	def __str__(self):
		return str(self.subject)

class PostDto:
	def __init__(self, post):
		self.post = post
		self.id = post.id
		self.title = post.title
		self.content = post.content
		self.date_creation = post.date_creation
		self.date_modification = post.date_modification
		self.theme = post.theme
		self.subtheme = post.subtheme
		self.subject = post.subject
		self.profile = post.profile
		self.imageurl = '/' + post.profile.image.url
	def __str__(self):
		return str(self.post)