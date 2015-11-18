from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

class IndexView(TemplateView):
	template_name = 'battle/index.html'

	def get_context_data(self, **kwargs):
		context = super(IndexView, self).get_context_data(**kwargs)
		context['pagetitle'] = 'Battle For Midgard'
		return context