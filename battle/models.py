from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from battle.managers import ClasseManager, AttackManager, AttackByClasseManager, ArmorCategoryManager, ArmorPieceManager, PlayerManager, PlayerArmorManager

##### CLASS & ATTACKS #####
class Classe(models.Model):
	name = models.CharField(max_length=100, default='', unique=True)
	armor_type = models.SmallIntegerField(default=2, validators=[MinValueValidator(1), MaxValueValidator(3)])

	objects = ClasseManager()

	def __str__(self):
		return "{0}".format(self.name)

class Attack(models.Model):
	name = models.CharField(max_length=100, default='', unique=True)
	damage = models.SmallIntegerField(default=0)
	heal = models.SmallIntegerField(default=0)
	mana = models.SmallIntegerField(default=0)
	target = models.SmallIntegerField(default=1)

	objects = AttackManager()

	def __str__(self):
		return "Attack(name={0}, damage={1}, heal={2}, mana={3}, target={4})".format(self.name, self.damage, self.heal, self.mana, self.target)

class AttackByClasse(models.Model):
	classe = models.ForeignKey(Classe)
	attack = models.ForeignKey(Attack)

	objects = AttackByClasseManager()

##### ARMOR #####
class ArmorCategory(models.Model):
	place = models.CharField(max_length=100)
	weight = models.SmallIntegerField(default=2, validators=[MinValueValidator(1), MaxValueValidator(3)])

	objects = ArmorCategoryManager()

	def __str__(self):
		if self.weight == 1:
			weight = "Light"
		elif self.weight == 2:
			weight = "Medium"
		else:
			weight = "Heavy"
		return "{0} ({1})".format(self.place, weight)

class ArmorPiece(models.Model):
	name = models.CharField(max_length=100, unique=True)
	price = models.SmallIntegerField(default=10, validators=[MinValueValidator(10)])

	defense = models.SmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])
	health = models.SmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])
	mana = models.SmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])
	strength = models.SmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
	agility = models.SmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
	intellect = models.SmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
	spirit = models.SmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])

	category = models.ForeignKey(ArmorCategory)

	objects = ArmorPieceManager()

	def __str__(self):
		return "ArmorPiece(name={0}, category={1})".format(self.name, self.category)

##### PLAYER #####
class Player(models.Model):
	pseudo = models.CharField(max_length=100, default='', unique=True)
	level = models.SmallIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(20)])
	experience = models.SmallIntegerField(default=0, validators=[MinValueValidator(0)])
	health = models.SmallIntegerField(default=100, validators=[MinValueValidator(0)])
	mana = models.SmallIntegerField(default=100, validators=[MinValueValidator(0)])
	strength = models.SmallIntegerField(default=10, validators=[MinValueValidator(8)])
	agility = models.SmallIntegerField(default=10, validators=[MinValueValidator(8)])
	intellect = models.SmallIntegerField(default=10, validators=[MinValueValidator(8)])
	spirit = models.SmallIntegerField(default=10, validators=[MinValueValidator(8)])

	classe = models.ForeignKey(Classe)

	objects = PlayerManager()

	def __str__(self):
		return "{0}, {1} {2}".format(self.pseudo, self.level, self.classe)

class PlayerArmor(models.Model):
	player = models.ForeignKey(Player)
	armor = models.ForeignKey(ArmorPiece)

	objects = PlayerArmorManager()

##### ENNEMIES #####