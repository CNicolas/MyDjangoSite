#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: cnicolas
# @Date:   2015-10-23 14:31:11
# @Last Modified by:   cnicolas
# @Last Modified time: 2015-11-06 13:58:51

import logging

from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from forum.models import Profile, Theme, SubTheme, Subject, Post, UnreadPost
from forum.dto import ThemeDto, SubThemeDto, SubjectDto, PostDto
from forum.forms import AddSubjectForm, AddPostForm

logger = logging.getLogger(__name__)

def forum(request):
	context = {'pagetitle': "Forum"}

	themes = Theme.objects.all()
	theme_dtos = []

	for theme in themes:
		subthemes = SubTheme.objects.filter(theme=theme)
		subtheme_dtos = []

		for subtheme in subthemes:
			subjects = Subject.objects.filter(subtheme=subtheme)
			subjects_dtos = [SubjectDto(subject) for subject in subjects]

			if request.user.is_authenticated():
				profile = Profile.objects.get(user=request.user)
				last_login_datetime = profile.previous_login
				
				for subject in subjects_dtos:
					unread_posts = UnreadPost.objects.filter(profile=profile, subject=subject.subject)
					subject.newpost = len(unread_posts)

			subtheme_dtos.append(SubThemeDto(subtheme, subjects_dtos))

		theme_dtos.append(ThemeDto(theme, subtheme_dtos))

	context['themes'] = theme_dtos

	return render(request, 'forum.html', context)

def subject(request, subject_id):
	try:
		subject = Subject.objects.get(id=subject_id)
		context = {'pagetitle': subject.title, 'subject': subject}

		if request.method == 'POST':
			form = AddPostForm(request.POST)

			if form.is_valid():
				profile = Profile.objects.get(user=request.user)
				title = form.cleaned_data['title']
				content = form.cleaned_data['content']
				Post.objects.create_post(subject, profile, title, content)
				
				logger.info(post.title + ' created')

				form = AddPostForm()


			else:
				error_list = []

				for e in dict(form.errors):
					error_list.append('Le champ ' + form[e].label + ' a une erreur : ' + form.errors[e].as_text()[2:])
				context['error'] = '\n'.join(error_list)

		else:
			
			if request.user.is_authenticated():
				profile = Profile.objects.get(user=request.user)
				UnreadPost.objects.filter(profile=profile, subject=subject).delete()
				logger.debug('UnreadPosts of ' + subject.title + ' deleted for ' + profile.pseudo)

			form = AddPostForm()

		posts = Post.objects.filter(subject=subject)
		posts_dtos = [PostDto(post) for post in posts]
		context['posts'] = posts_dtos
		context['form'] = form

		return render(request, "subject.html", context)

	except ObjectDoesNotExist:
		return redirect('forum')

@login_required(login_url="/forum")
def addsubject(request, subtheme_id):
	try:
		subtheme = SubTheme.objects.get(id=subtheme_id)

		if request.method == 'GET':
			logger.debug("GET addsubject")
			form = AddSubjectForm()
			context = {'pagetitle': subtheme.title, 'subtheme': SubThemeDto(subtheme), 'form': form}
			return render(request, 'addsubject.html', context)

		else:
			logger.debug('POST addsubject')
			form = AddSubjectForm(request.POST)

			if form.is_valid():

				try:
					Subject.objects.get(subtheme=subtheme, title=form.cleaned_data['title'])
					context = {'pagetitle': subtheme.title, 'subtheme': SubThemeDto(subtheme), 'form': form, 'error': "Le sujet existe déjà"}

				except ObjectDoesNotExist:
					subject = Subject.objects.create_subject(subtheme, form.cleaned_data['title'])
					logger.info(subject.title + " created")
					return redirect('forum')

			else:
				context = {'pagetitle': subtheme.title, 'subtheme': SubThemeDto(subtheme), 'form': form, 'error': "Le titre n'est pas valable"}

			return render(request, 'addsubject.html', context)

	except ObjectDoesNotExist:
		return redirect('forum')