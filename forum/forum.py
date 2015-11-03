#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: cnicolas
# @Date:   2015-10-23 14:31:11
# @Last Modified by:   cnicolas
# @Last Modified time: 2015-11-03 11:06:40

import logging

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from forum.models import Profile, Theme, SubTheme, Subject, Post
from forum.dto import ThemeDto, SubThemeDto, SubjectDto, PostDto
from forum.forms import SubjectForm

logger = logging.getLogger(__name__)

def forum(request):
	context = {"pagetitle": "Forum", 'background_color': 'white'}

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
	context["themes"] = theme_dtos

	return render(request, "forum.html", context)

def subject(request, subject_id):
	subject = Subject.objects.filter(id=subject_id)
	if subject:
		subject = subject[0]
		posts = Post.objects.filter(subject=subject)
		posts_dtos = [PostDto(post) for post in posts]
		context = {"pagetitle": subject.title, "posts": posts_dtos, 'background_color': 'white'}
		return render(request, "subject.html", context)
	else:
		return redirect("forum")

@login_required(login_url="/forum")
def addsubject(request, subtheme_id):
	subtheme = SubTheme.objects.get(id=subtheme_id)
	if request.method == 'GET':
		form = SubjectForm()
		context = {'pagetitle': 'Edition du sujet', 'subtheme': subtheme, 'form': form}
		return render(request, 'addsubject.html', context)
	else:
		form = SubjectForm(request.POST)
		if form.is_valid():
			Subject.objects.create_subject(subtheme, form.cleaned_data['title'])
			return redirect('forum')
		else:
			context = {'pagetitle': 'Edition du sujet', 'subtheme': subtheme, 'form': form, 'error': "Le titre n'est pas valable"}