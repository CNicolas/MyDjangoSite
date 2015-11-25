import logging

from django.http import HttpResponse
from django.views.generic import TemplateView

from battle.models import Classe, Attack, AttackByClasse, ArmorPiece, Player, PlayerArmor
from battle.dtos import PlayerDto
from battle.utils import myRender

logger = logging.getLogger(__name__)

class IndexView(TemplateView):
	template_name = 'battle/index.html'

	def get_context_data(self, **kwargs):
		context = super(IndexView, self).get_context_data(**kwargs)
		context['pagetitle'] = 'Bataille pour Eorzea'
		return context

#####################################################################################################

def test(request):
	return myRender(request, 'test.html', context)

def show(request):
	# return HttpResponse(Classe.objects.all())
	# heavy_torso = ArmorCategory.objects.filter(place="torso", weight=3)[0]
	# god_armor = ArmorPiece.objects.filter(name="Cuirasse des Dieux")[0]
	# aku_warrior = Player.objects.filter(pseudo="Aku_Guerrier")[0]

	context = {
		'pagetitle': 'Show',
		'classes': Classe.objects.all(),
		'attacks': Attack.objects.all(),
		'attacksbyclass': AttackByClasse.objects.all(),
		'armorpieces': ArmorPiece.objects.all(),
		'players': Player.objects.all(),
		'playerarmors': PlayerArmor.objects.all(),

	}
	return myRender(request, 'test.html', context)