# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django import forms
from django.shortcuts import render
from django.conf import settings

from joc.models import Grup, Jugador, Equip, Partit, PronosticPartit, PronosticEquipGrup

GOLS_CHOICES = (('-1', '-'), (0,0),(1,1),(2,2),(3,3),(4,4), (5,5), (6,6), (7,7), (8,8))
class PartitForm(forms.ModelForm):
    gols1 = forms.ChoiceField(choices=GOLS_CHOICES,
                              widget=forms.Select(attrs={"onChange":'actualitza()'}))
    gols2 = forms.ChoiceField(choices=GOLS_CHOICES,
                              widget=forms.Select(attrs={"onChange":'actualitza()'}))
    class Meta:
        model = PronosticPartit
        fields = ('gols1', 'gols2')


GrupForm = forms.modelformset_factory(PronosticPartit, form=PartitForm, extra=0)


def guarda_classificacio_grup(request, jugador):
    for i in range(settings.EQUIPS_PER_GRUP):
        equip = Equip.objects.get(pk=int(request.POST['id%d' % (i)]))
        pronostic_equip = PronosticEquipGrup.objects.get(jugador=jugador,
                                                         equip=equip)
        pronostic_equip.posicio = i + 1
        pronostic_equip.punts = int(request.POST['p%d' % (i)])
        pronostic_equip.diferencia = int(request.POST['d%d' % (i)])
        pronostic_equip.favor = int(request.POST['g%d' % (i)])
        pronostic_equip.save()



@login_required
def pronostic(request):

    jugador = Jugador.objects.get(usuari=request.user)

    # Si és un POST, guardem els valors del formulari
    if request.method == 'POST':
        grup_form = GrupForm(request.POST)
        if grup_form.is_valid():
            grup_form.save()
        else:
            # TODO: No sé què fer en aquest cas!
            pass

        guarda_classificacio_grup(request, jugador)

    form = None
    nom_grup = request.GET.get('grup', 'A')
    grup = Grup.objects.get(nom=nom_grup)
    try:
        seguent_grup = Grup.objects.get(id=grup.id + 1).nom
    except Grup.DoesNotExist:
        seguent_grup = 'G'

    partits = Partit.objects.filter(grup=grup)

    # Creem els PronosticPartit que faltin
    for partit in partits:
        PronosticPartit.objects.get_or_create(jugador=jugador, partit=partit)

    grup_form = GrupForm(queryset=PronosticPartit.objects.filter(
        jugador=jugador, partit__grup__nom=grup))

    # Creem els PronosticEquipGrup que faltin
    equips_classificacio = []
    deshabilita_submit = True
    for equip in Equip.objects.filter(grup__nom=grup):
        equip_classificacio, _ = PronosticEquipGrup.objects.get_or_create(jugador=jugador,
                                                                          equip=equip)
        equips_classificacio.append(equip_classificacio)
        if equip_classificacio.posicio != 0:
            deshabilita_submit = False

    return render(
        request,
        'joc/grup.html',
        {
            'formset': grup_form,
            'equips_classificacio': sorted(equips_classificacio, key=lambda k: k.posicio),
            'height_banderes': 19,
            'width_banderes': 28,
            'border_banderes': 1,
            'seguent_grup': seguent_grup,
            'deshabilita_submit': deshabilita_submit,
        }
    )
