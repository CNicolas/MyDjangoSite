#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: cnicolas
# @Date:   2015-10-27 15:30:06
# @Last Modified by:   cnicolas
# @Last Modified time: 2015-11-03 10:30:58

from forum.models import Profile, Theme, SubTheme, Subject, Post

class ThemeDto:
	def __init__(self, theme, subthemes=None):
		self.theme = theme
		self.id = theme.id
		self.title = theme.title
		if subthemes:
			self.subthemes = subthemes
		else:
			self.subthemes = SubTheme.objects.filter(theme=theme)

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

class SubjectDto:
	def __init__(self, subject):
		self.subject = subject
		self.id = subject.id
		self.title = subject.title
		self.theme = subject.theme
		self.subtheme = subject.subtheme
		self.posts = Post.objects.filter(subject=subject)

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