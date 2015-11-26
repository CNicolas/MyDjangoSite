from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from battle.managers import ClasseManager, AttackManager, AttackByClasseManager, ArmorPieceManager, PlayerManager, PlayerArmorManager, EnnemyManager, EnnemyAttackManager
from battle.utils import armorWeightByWeight

##### CLASS & ATTACKS #####
class Classe(models.Model):
	name = models.CharField(max_length=100, default='', unique=True)
	weight = models.CharField(max_length=100)
	health = models.SmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])

	objects = ClasseManager()

	def __str__(self):
		return "{0}(weight={1}, health={2})".format(self.name, self.weight, self.health)

class Attack(models.Model):
	name = models.CharField(max_length=100, default='Corps à Corps')
	damage = models.SmallIntegerField(default=0)
	heal = models.SmallIntegerField(default=0)
	mana = models.SmallIntegerField(default=0)
	energy = models.SmallIntegerField(default=0)
	critical = models.SmallIntegerField(default=10, validators=[MinValueValidator(0), MaxValueValidator(100)])
	duration = models.SmallIntegerField(default=1)
	cooldown = models.SmallIntegerField(default=1)
	target = models.SmallIntegerField(default=1)
	stat = models.CharField(max_length=100)

	objects = AttackManager()

	def __str__(self):
		return "Attack(name={0}, damage={1}, heal={2}, mana={3}, energy={4}, critical={5}, duration={6}, target={7}, stat={8})".format(self.name, self.damage, self.heal, self.mana, self.energy, self.critical, self.duration, self.target, self.stat)

class AttackByClasse(models.Model):
	classe = models.ForeignKey(Classe)
	attack = models.ForeignKey(Attack)

	objects = AttackByClasseManager()

	def __str__(self):
		return "AttackByClasse(classe={0}, attack={1})".format(self.classe.name, self.attack.name)

##### ARMOR #####
class ArmorPiece(models.Model):
	name = models.CharField(max_length=100, unique=True)
	place = models.CharField(max_length=100)
	weight = models.CharField(max_length=100)
	price = models.SmallIntegerField(default=10, validators=[MinValueValidator(10)])

	defense = models.SmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])
	health = models.SmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])
	mana = models.SmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])
	energy = models.SmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])
	strength = models.SmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
	agility = models.SmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
	intellect = models.SmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
	spirit = models.SmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])

	objects = ArmorPieceManager()

	def __str__(self):
		return "ArmorPiece(name={0}, place={1}, weight={2}, price={3}, defense={4}, health={5}, mana={6}, energy={7}, strength={8}, agility={9}, intellect={10}, spirit={11})".format(self.name, self.place, self.weight, self.price, self.defense, self.health, self.mana, self.energy, self.strength, self.agility, self.intellect, self.spirit)

##### PLAYER #####
class Player(models.Model):
	pseudo = models.CharField(max_length=100, default='', unique=True)
	level = models.SmallIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(20)])
	experience = models.SmallIntegerField(default=0, validators=[MinValueValidator(0)])
	health = models.SmallIntegerField(default=100, validators=[MinValueValidator(0)])
	mana = models.SmallIntegerField(default=100, validators=[MinValueValidator(0)])
	energy = models.SmallIntegerField(default=100, validators=[MinValueValidator(0)])
	strength = models.SmallIntegerField(default=10, validators=[MinValueValidator(8)])
	agility = models.SmallIntegerField(default=10, validators=[MinValueValidator(8)])
	intellect = models.SmallIntegerField(default=10, validators=[MinValueValidator(8)])
	spirit = models.SmallIntegerField(default=10, validators=[MinValueValidator(8)])

	classe = models.ForeignKey(Classe)

	objects = PlayerManager()

	def __str__(self):
		return "{0}, {1} {2}. health={3}, mana={4}, energy={5}".format(self.pseudo, self.level, self.classe, self.health, self.mana, self.energy)

class PlayerArmor(models.Model):
	player = models.ForeignKey(Player)
	armor = models.ForeignKey(ArmorPiece)

	objects = PlayerArmorManager()

##### ENNEMIES #####
class Ennemy(models.Model):
	name = models.CharField(max_length=100, default='Monstre', unique=True)
	level = models.SmallIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(20)])
	health = models.SmallIntegerField(default=100, validators=[MinValueValidator(0)])

	objects = EnnemyManager()

	def __str__(self):
		return "Ennemy(name={0}, level={1}, health={2})".format(self.name, self.level, self.health)

class EnnemyAttack(models.Model):
	name = models.CharField(max_length=100, default='Attaque')
	damage = models.SmallIntegerField(default=0)
	heal = models.SmallIntegerField(default=0)
	critical = models.SmallIntegerField(default=10, validators=[MinValueValidator(0), MaxValueValidator(100)])
	duration = models.SmallIntegerField(default=1)
	cooldown = models.SmallIntegerField(default=1)
	target = models.SmallIntegerField(default=1)

	ennemy = models.ForeignKey(Ennemy)

	objects = EnnemyAttackManager()

	def __str__(self):
		return "EnnemyAttack(name={0}, critical={1}, duration={2}, target={3})".format(self.name, self.critical, self.duration, self.target)
