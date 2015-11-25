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

def deleteContent():
	Classe.objects.all().delete()
	Attack.objects.all().delete()
	AttackByClasse.objects.all().delete()
	ArmorCategory.objects.all().delete()
	ArmorPiece.objects.all().delete()
	Player.objects.all().delete()
	PlayerArmor.objects.all().delete()

def test(request):
	deleteContent()
	
	warrior = Classe.objects.create_classe("Guerrier", 3, 100)
	wizard = Classe.objects.create_classe("Mage", 1, 0)
	healer = Classe.objects.create_classe("Prêtre", 1, 20)
	thief = Classe.objects.create_classe("Assassin", 2, 0)

	cac = Attack.objects.create_attack("Attaque CaC", 10, 0, 0, 10, 1, 1)
	fire = Attack.objects.create_attack("Feu", 20, 0, 10, 0, 1, 1)
	heal = Attack.objects.create_attack("Soin", 0, 10, 10, 0, 1, 1)
	arrow = Attack.objects.create_attack("Flêche", 15, 0, 0, 10, 1, 1)

	AttackByClasse.objects.create_attack_by_classe(warrior, cac)
	AttackByClasse.objects.create_attack_by_classe(wizard, fire)
	AttackByClasse.objects.create_attack_by_classe(healer, heal)
	AttackByClasse.objects.create_attack_by_classe(thief, arrow)
	
	god_light_head = ArmorPiece.objects.create_armor_piece("Capuchon des Dieux", "head", 1, 1000000000, 10, 10, 10, 5, 5, 5, 5, light_head)
	god_light_torso = ArmorPiece.objects.create_armor_piece("Robe des Dieux", "torso", 1, 1000000000, 10, 10, 10, 5, 5, 5, 5, light_torso)
	god_light_hand = ArmorPiece.objects.create_armor_piece("Gants des Dieux", "hand", 1, 1000000000, 10, 10, 10, 5, 5, 5, 5, light_hand)
	god_light_neck = ArmorPiece.objects.create_armor_piece("Collier des Dieux", "neck", 1, 1000000000, 10, 10, 10, 5, 5, 5, 5, light_neck)
	god_light_feet = ArmorPiece.objects.create_armor_piece("Chaussons des Dieux", "feet", 1, 1000000000, 10, 10, 10, 5, 5, 5, 5, light_feet)

	god_medium_head = ArmorPiece.objects.create_armor_piece("Chapeau des Dieux", "head", 2, 1000000000, 10, 10, 10, 5, 5, 5, 5, medium_head)
	god_medium_torso = ArmorPiece.objects.create_armor_piece("Tunique des Dieux", "torso", 2, 1000000000, 10, 10, 10, 5, 5, 5, 5, medium_torso)
	god_medium_hand = ArmorPiece.objects.create_armor_piece("Mitaines des Dieux", "hand", 2, 1000000000, 10, 10, 10, 5, 5, 5, 5, medium_hand)
	god_medium_neck = ArmorPiece.objects.create_armor_piece("Chaine des Dieux", "neck", 2, 1000000000, 10, 10, 10, 5, 5, 5, 5, medium_neck)
	god_medium_feet = ArmorPiece.objects.create_armor_piece("Bottes des Dieux", "feet", 2, 1000000000, 10, 10, 10, 5, 5, 5, 5, medium_feet)

	god_heavy_head = ArmorPiece.objects.create_armor_piece("Heaume des Dieux", "head", 3, 1000000000, 10, 10, 10, 5, 5, 5, 5, heavy_head)
	god_heavy_torso = ArmorPiece.objects.create_armor_piece("Cuirasse des Dieux", "torso", 3, 1000000000, 10, 10, 10, 5, 5, 5, 5, heavy_torso)
	god_heavy_hand = ArmorPiece.objects.create_armor_piece("Gantelets des Dieux", "hand", 3, 1000000000, 10, 10, 10, 5, 5, 5, 5, heavy_hand)
	god_heavy_neck = ArmorPiece.objects.create_armor_piece("Gorgerin des Dieux", "neck", 3, 1000000000, 10, 10, 10, 5, 5, 5, 5, heavy_neck)
	god_heavy_feet = ArmorPiece.objects.create_armor_piece("Cuissardes des Dieux", "feet", 3, 1000000000, 10, 10, 10, 5, 5, 5, 5, heavy_feet)
	
	aku_warrior = Player.objects.create_player("Aku_Guerrier", warrior, 20, 0, 1000, 1000, 20, 10, 10, 10)
	aku_wizard = Player.objects.create_player("Aku_Mage", wizard, 20, 0, 1000, 1000, 10, 10, 20, 10)
	aku_healer = Player.objects.create_player("Aku_Prêtre", healer, 20, 0, 1000, 1000, 10, 10, 10, 20)
	aku_thief = Player.objects.create_player("Aku_Assassin", thief, 20, 0, 1000, 1000, 10, 20, 10, 10)

	PlayerArmor.objects.create_player_armor(aku_warrior, god_heavy_head)
	PlayerArmor.objects.create_player_armor(aku_warrior, god_heavy_torso)
	PlayerArmor.objects.create_player_armor(aku_warrior, god_heavy_hand)
	PlayerArmor.objects.create_player_armor(aku_warrior, god_heavy_neck)
	PlayerArmor.objects.create_player_armor(aku_warrior, god_heavy_feet)

	PlayerArmor.objects.create_player_armor(aku_wizard, god_light_head)
	PlayerArmor.objects.create_player_armor(aku_wizard, god_light_torso)
	PlayerArmor.objects.create_player_armor(aku_wizard, god_light_hand)
	PlayerArmor.objects.create_player_armor(aku_wizard, god_light_neck)
	PlayerArmor.objects.create_player_armor(aku_wizard, god_light_feet)

	PlayerArmor.objects.create_player_armor(aku_healer, god_light_head)
	PlayerArmor.objects.create_player_armor(aku_healer, god_light_torso)
	PlayerArmor.objects.create_player_armor(aku_healer, god_light_hand)
	PlayerArmor.objects.create_player_armor(aku_healer, god_light_neck)
	PlayerArmor.objects.create_player_armor(aku_healer, god_light_feet)

	PlayerArmor.objects.create_player_armor(aku_thief, god_medium_head)
	PlayerArmor.objects.create_player_armor(aku_thief, god_medium_torso)
	PlayerArmor.objects.create_player_armor(aku_thief, god_medium_hand)
	PlayerArmor.objects.create_player_armor(aku_thief, god_medium_neck)
	PlayerArmor.objects.create_player_armor(aku_thief, god_medium_feet)

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
	# heavy_torso = ArmorCategory.objects.filter(place="torso", weight=3)[0]
	# god_armor = ArmorPiece.objects.filter(name="Cuirasse des Dieux")[0]
	# aku_warrior = Player.objects.filter(pseudo="Aku_Guerrier")[0]

	a = [a.critical for a in Attack.objects.all()]
	print(a)

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