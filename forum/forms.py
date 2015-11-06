#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: cnicolas
# @Date:   2015-10-28 11:40:47
# @Last Modified by:   cnicolas
# @Last Modified time: 2015-11-04 15:55:13

import logging

from django import forms

logger = logging.getLogger(__name__)

class SubscribeForm(forms.Form):
	username = forms.CharField(label="Nom d'utilisateur", max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'validate', 'length': '100', 'required': 'required'}))
	email = forms.CharField(label='E-Mail', max_length=200, required=True, widget=forms.EmailInput(attrs={'class': 'validate', 'length': '200', 'required': 'required'}))
	password = forms.CharField(label='Mot de Passe', max_length=100, required=True, widget=forms.PasswordInput(attrs={'class': 'validate', 'length': '100', 'required': 'required'}))
	confirm_password = forms.CharField(label='Confirmez le mot de passe', required=True, max_length=100, widget=forms.PasswordInput(attrs={'class': 'validate', 'length': '100', 'required': 'required'}))

class ImageForm(forms.Form):
	image = forms.ImageField(label='Insérez une image')

class ProfileForm(forms.Form):
	pseudo = forms.CharField(label='Pseudo', max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'validate', 'length': '100', 'required': 'required'}))
	firstname = forms.CharField(label='Prénom', max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'validate', 'length': '100', 'required': 'required'}))
	lastname = forms.CharField(label='Nom', max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'validate', 'length': '100', 'required': 'required'}))
	birthdate = forms.DateField(required=False, widget=forms.DateInput(attrs={'class': 'datepicker', 'length': '100', 'placeholder': 'Date de naissance'}))
	image = forms.ImageField(required=False)

class AddSubjectForm(forms.Form):
	title = forms.CharField(label='Titre', max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'validate', 'length': '100', 'required': 'required'}))

class AddPostForm(forms.Form):
	title = forms.CharField(label='Titre', max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'validate', 'length': '100'}))
	content = forms.CharField(label='Contenu', required=True, widget=forms.Textarea())