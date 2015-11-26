import logging

from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic import TemplateView

from battle.models import Classe, Attack, AttackByClasse, ArmorPiece, Player, PlayerArmor, Ennemy, EnnemyAttack
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
	classe = Classe.objects.filter(name='Guerrier')[0]
	aku = Player.objects.create_player("Aku_Guerrier", classe, 20, 0, 200, 100, 100, 20, 10, 10, 10)
	head = ArmorPiece.objects.filter(place='head', weight='heavy')[0]
	torso = ArmorPiece.objects.filter(place='torso', weight='heavy')[0]
	hand = ArmorPiece.objects.filter(place='hand', weight='heavy')[0]
	neck = ArmorPiece.objects.filter(place='neck', weight='heavy')[0]
	feet = ArmorPiece.objects.filter(place='feet', weight='heavy')[0]
	PlayerArmor.objects.create_player_armor(aku, head)
	PlayerArmor.objects.create_player_armor(aku, torso)
	PlayerArmor.objects.create_player_armor(aku, hand)
	PlayerArmor.objects.create_player_armor(aku, neck)
	PlayerArmor.objects.create_player_armor(aku, feet)
	return redirect('show')

def show(request):
	context = {
		'pagetitle': 'Show',
		'classes': Classe.objects.all(),
		'attacks': Attack.objects.all(),
		'attacksbyclass': AttackByClasse.objects.all(),
		'armorpieces': ArmorPiece.objects.all(),
		'players': Player.objects.all(),
		'playerarmors': PlayerArmor.objects.all(),
		'ennemies': Ennemy.objects.all(),
		'ennemyattacks': EnnemyAttack.objects.all()

	}
	return myRender(request, 'test.html', context)
