from django.db import models
from django.contrib.auth.models import User

class Jugador(models.Model):
    usuari = models.OneToOneField(User)
    pagat = models.BooleanField(default=False)
    posicio = models.PositiveSmallIntegerField()
    posicio_anterior = models.PositiveSmallIntegerField()
    punts = models.PositiveSmallIntegerField()
    punts_anterior = models.PositiveSmallIntegerField()
    punts_resultats = models.PositiveSmallIntegerField()
    punts_grups = models.PositiveSmallIntegerField()
    punts_equips_encertats = models.PositiveSmallIntegerField()

class Equip(models.Model):
    nom = models.CharField(max_length=128)
    bandera = models.CharField(max_length=128)

class Grup(models.Model):
    equip1 = models.ForeignKey('Equip', related_name='equip1_grup')
    equip2 = models.ForeignKey('Equip', related_name='equip2_grup')
    equip3 = models.ForeignKey('Equip', related_name='equip3_grup')
    equip4 = models.ForeignKey('Equip', related_name='equip4_grup')

class Partit(models.Model):
    equip1 = models.ForeignKey('Equip', related_name='equip1')
    equip2 = models.ForeignKey('Equip', related_name='equip2')
    diaihora = models.DateTimeField()
    estadi = models.CharField(max_length=128)
    grup = models.ForeignKey('Grup')

class Resultat(models.Model):
    jugador = models.ForeignKey('Jugador')
    partit = models.ForeignKey('Partit')
    gols1 = models.PositiveSmallIntegerField()
    gols2 = models.PositiveSmallIntegerField()

    def empat(self):
        return self.gols1 == self.gols2
