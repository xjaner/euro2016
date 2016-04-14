# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django import forms
from django.shortcuts import render

from joc.models import Grup, Jugador, Equip, Partit, PronosticPartit, PronosticEquipGrup
from joc.utils import crea_partits, comprova_tercers, guarda_classificacio_grup


GOLS_CHOICES = (('-1', '-'), (0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7),
                (8, 8))


class PartitForm(forms.ModelForm):
    gols1 = forms.ChoiceField(choices=GOLS_CHOICES,
                              widget=forms.Select(attrs={"onChange": 'actualitza()'}))
    gols2 = forms.ChoiceField(choices=GOLS_CHOICES,
                              widget=forms.Select(attrs={"onChange": 'actualitza()'}))

    class Meta:
        model = PronosticPartit
        fields = ('gols1', 'gols2')


GrupForm = forms.modelformset_factory(PronosticPartit, form=PartitForm, extra=0)


GUARDA_PARTITS = set(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])
FASE_GRUPS = set(['A', 'B', 'C', 'D', 'E', 'F'])
CREA_PARTITS = set(['G', 'H', 'I', 'J'])
COMPROVAR_TERCERS = set(['G'])
TEXT_GRUP = {
    'A': 'Grup A',
    'B': 'Grup B',
    'C': 'Grup C',
    'D': 'Grup D',
    'E': 'Grup E',
    'F': 'Grup F',
    'G': 'Vuitens de final',
    'H': 'Quarts de final',
    'I': 'Semifinals',
    'J': 'Final',
}


@login_required
def pronostic(request):

    jugador = Jugador.objects.get(usuari=request.user)
    nom_grup = request.GET.get('grup', 'A')

    # Si és un POST, guardem els valors del formulari
    if request.method == 'POST':

        # Si s'han de guardar classificacions d'equips
        if nom_grup in GUARDA_PARTITS:
            grup_form = GrupForm(request.POST)
            if grup_form.is_valid():
                grup_form.save()
            else:
                # TODO: Falta crear una pàgina d'error i que em notifiqui!
                pass
            guarda_classificacio_grup(request, jugador)

        if nom_grup in CREA_PARTITS:
            crea_partits(request, jugador, nom_grup)

        if nom_grup in COMPROVAR_TERCERS:
            tercers_empatats = comprova_tercers(request, jugador)

            if tercers_empatats:
                return render(
                    request,
                    'joc/tercers.html',
                    {
                        'formset': grup_form,
                        'jugador': jugador,
                        'tercers_empatats': tercers_empatats,
                    }
                )

    grup = Grup.objects.get(nom=nom_grup)
    try:
        seguent_grup = Grup.objects.get(id=grup.id + 1).nom
    except Grup.DoesNotExist:
        seguent_grup = 'G'

    partits = Partit.objects.filter(grup=grup)

    # Creem els PronosticPartit que faltin
    for partit in partits:
        items = {}
        if nom_grup in FASE_GRUPS:
            items['equip1'] = partit.equip1
            items['equip2'] = partit.equip2

        PronosticPartit.objects.get_or_create(jugador=jugador, partit=partit, **items)

    grup_form = GrupForm(queryset=PronosticPartit.objects.filter(
        jugador=jugador, partit__grup__nom=grup))

    equips_classificacio = []
    deshabilita_submit = True
    template = 'grup.html'
    if nom_grup in FASE_GRUPS:

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
        'joc/{template}'.format(template=template),
        {
            'formset': grup_form,
            'equips_classificacio': sorted(equips_classificacio, key=lambda k: k.posicio),
            'height_banderes': 19,
            'width_banderes': 28,
            'border_banderes': 1,
            'grup': grup.nom,
            'seguent_grup': seguent_grup,
            'deshabilita_submit': deshabilita_submit,
            'jugador': jugador,
            'text_grup': TEXT_GRUP[nom_grup],
        }
    )
