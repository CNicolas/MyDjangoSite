#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: cnicolas
# @Date:   2015-10-23 14:31:11
# @Last Modified by:   cnicolas
# @Last Modified time: 2015-11-03 16:55:56

import logging

from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from forum.models import Profile, Theme, SubTheme, Subject, Post
from forum.dto import ThemeDto, SubThemeDto, SubjectDto, PostDto
from forum.forms import AddSubjectForm, AddPostForm

logger = logging.getLogger(__name__)

def forum(request):
	context = {'pagetitle': "Forum", 'background_color': 'white'}

	themes = Theme.objects.all()
	theme_dtos = []
	for theme in themes:		
		subthemes = SubTheme.objects.filter(theme=theme)
		subtheme_dtos = []
		for subtheme in subthemes:			
			subjects = Subject.objects.filter(subtheme=subtheme)
			subjects_dtos = [SubjectDto(subject) for subject in subjects]
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
				context['success'] = "Rien ne s'est passé, bravo !"
			else:
				context['error'] = 'Une erreur est apparue avec le formulaire ! '
		else:
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
			form = AddSubjectForm()
			context = {'pagetitle': subtheme.title, 'subtheme': SubThemeDto(subtheme), 'form': form}
			return render(request, 'addsubject.html', context)
		else:
			form = AddSubjectForm(request.POST)
			if form.is_valid():
				Subject.objects.create_subject(subtheme, form.cleaned_data['title'])
				return redirect('forum')
			else:
				context = {'pagetitle': 'Edition du sujet', 'subtheme': subtheme, 'form': form, 'error': "Le titre n'est pas valable"}
	except ObjectDoesNotExist:
		return redirect('forum')