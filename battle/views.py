import logging

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

from battle.models import Classe, Attack, AttackByClasse, ArmorCategory, ArmorPiece, Player, PlayerArmor

logger = logging.getLogger(__name__)

class IndexView(TemplateView):
	template_name = 'battle/index.html'

	def get_context_data(self, **kwargs):
		context = super(IndexView, self).get_context_data(**kwargs)
		context['pagetitle'] = 'Bataille pour Eorzea'
		return context

class PlayerView(TemplateView):
	template_name = 'battle/player.html'

	def get(self, request, *args, **kwargs):
		logger.info(kwargs)
		return super(PlayerView, self).get(request, *args, **kwargs)

	def get_context_data(self, **kwargs):
		context = super(TestView, self).get_context_data(**kwargs)
		context['pagetitle'] = 'Test'
		context['player'] = Player.objects.all()
		return context

#####################################################################################################

def myRender(request, template, context):
	return render(request, 'battle/' + template, context)

def player_view_pseudo(request, player_pseudo):
	player = Player.objects.get(pseudo=player_pseudo)
	context = {'pagetitle': 'Joueur', 'player': player}
	return myRender(request, 'player.html', context)

def deleteContent():
	Classe.objects.all().delete()
	Attack.objects.all().delete()
	AttackByClasse.objects.all().delete()
	ArmorCategory.objects.all().delete()
	ArmorPiece.objects.all().delete()
	Player.objects.all().delete()
	PlayerArmor.objects.all().delete()

def test(request):
	# deleteContent()
	
	warrior = Classe.objects.create_classe("Guerrier")
	wizard = Classe.objects.create_classe("Mage")
	healer = Classe.objects.create_classe("Prêtre")
	thief = Classe.objects.create_classe("Assassin")

	cac = Attack.objects.create_attack("Attaque CaC", 10, 0, 0, 1)
	fire = Attack.objects.create_attack("Feu", 20, 0, 10, 1)
	heal = Attack.objects.create_attack("Soin", 0, 10, 10, 1)
	arrow = Attack.objects.create_attack("Flêche", 15, 0, 0, 1)

	AttackByClasse.objects.create_attack_by_classe(warrior, cac)
	AttackByClasse.objects.create_attack_by_classe(wizard, fire)
	AttackByClasse.objects.create_attack_by_classe(healer, heal)
	AttackByClasse.objects.create_attack_by_classe(thief, arrow)
	
	light_hat = ArmorCategory.objects.create_armor_category("Chapeau", 1)
	medium_hat = ArmorCategory.objects.create_armor_category("Casque", 2)
	heavy_hat = ArmorCategory.objects.create_armor_category("Heaume", 3)
	light_torso = ArmorCategory.objects.create_armor_category("Robe", 1)
	medium_torso = ArmorCategory.objects.create_armor_category("Torse", 2)
	heavy_torso = ArmorCategory.objects.create_armor_category("Plastron", 3)

	god_helmet = ArmorPiece.objects.create_armor_piece("Heaume des Dieux", 1000000000, 10, 10, 10, 5, 5, 5, 5, heavy_hat)
	god_robe = ArmorPiece.objects.create_armor_piece("Robe des Dieux", 1000000000, 10, 10, 10, 5, 5, 5, 5, light_torso)
	god_hat = ArmorPiece.objects.create_armor_piece("Chapeau des Dieux", 1000000000, 10, 10, 10, 5, 5, 5, 5, medium_hat)

	aku_warrior = Player.objects.create_player("Aku_Guerrier", warrior, 20, 0, 1000, 1000, 20, 10, 10, 10)
	aku_wizard = Player.objects.create_player("Aku_Mage", wizard, 20, 0, 1000, 1000, 10, 10, 20, 10)
	aku_healer = Player.objects.create_player("Aku_Prêtre", healer, 20, 0, 1000, 1000, 10, 10, 10, 20)
	aku_thief = Player.objects.create_player("Aku_Assassin", thief, 20, 0, 1000, 1000, 10, 20, 10, 10)

	PlayerArmor.objects.create_player_armor(aku_warrior, god_helmet)
	PlayerArmor.objects.create_player_armor(aku_wizard, god_robe)
	PlayerArmor.objects.create_player_armor(aku_healer, god_robe)
	PlayerArmor.objects.create_player_armor(aku_thief, god_hat)

	context = {
		'pagetitle': 'Test',
		'classes': Classe.objects.all(),
		'attacks': Attack.objects.all(),
		'attacksbyclass': AttackByClasse.objects.all(),
		'armorcategories': ArmorCategory.objects.all(),
		'armorpieces': ArmorPiece.objects.all(),
		'players': Player.objects.all(),
		'playerarmors': PlayerArmor.objects.all(),

	}
	return myRender(request, 'test.html', context)

def show(request):
	# return HttpResponse(Classe.objects.all())
	context = {
		'pagetitle': 'Show',
		'classes': Classe.objects.all(),
		'attacks': Attack.objects.all(),
		'attacksbyclass': AttackByClasse.objects.all(),
		'armorcategories': ArmorCategory.objects.all(),
		'armorpieces': ArmorPiece.objects.all(),
		'players': Player.objects.all(),
		'playerarmors': PlayerArmor.objects.all(),

	}
	return myRender(request, 'test.html', context)