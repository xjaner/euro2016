from django.db import models
from django.contrib.auth.models import User

class Jugador(models.Model):
    usuari = models.OneToOneField(User)
    pagat = models.BooleanField(default=False)
    posicio = models.PositiveSmallIntegerField()
    posicio_anterior = models.PositiveSmallIntegerField()
    punts = models.PositiveSmallIntegerField(default=0)
    punts_anterior = models.PositiveSmallIntegerField(default=0)
    punts_resultats = models.PositiveSmallIntegerField(default=0)
    punts_grups = models.PositiveSmallIntegerField(default=0)
    punts_equips_encertats = models.PositiveSmallIntegerField(default=0)

class Grup(models.Model):
    nom = models.CharField(max_length=32)

    def __unicode__(self):
        return self.nom

class Equip(models.Model):
    nom = models.CharField(max_length=128)
    bandera = models.CharField(max_length=128)
    grup = models.ForeignKey('Grup')

    def __unicode__(self):
        return self.nom

class PronosticEquipGrup(models.Model):
    jugador = models.ForeignKey(Jugador)
    equip = models.ForeignKey(Equip)
    posicio = models.PositiveSmallIntegerField(default=0)
    punts = models.PositiveSmallIntegerField(default=0)
    diferencia = models.SmallIntegerField(default=0)
    favor = models.PositiveSmallIntegerField(default=0)

class Partit(models.Model):
    equip1 = models.ForeignKey(Equip, related_name='equip1')
    equip2 = models.ForeignKey(Equip, related_name='equip2')
    diaihora = models.DateTimeField()
    estadi = models.CharField(max_length=128)
    grup = models.ForeignKey(Grup)

    def __unicode__(self):
        return u'[{pk}- {grup}] {equip1} - {equip2}'.format(
            pk=self.pk,
            grup=self.grup,
            equip1=self.equip1,
            equip2=self.equip2,
        )

class PronosticPartit(models.Model):
    jugador = models.ForeignKey(Jugador)
    partit = models.ForeignKey(Partit)
    gols1 = models.PositiveSmallIntegerField(default=0)
    gols2 = models.PositiveSmallIntegerField(default=0)

    def empat(self):
        return self.gols1 == self.gols2
