from django.contrib.auth.decorators import login_required
from django import forms
from django.shortcuts import render

from joc.models import Jugador, Partit, PronosticPartit

GOLS_CHOICES = ((0,0),(1,1),(2,2),(3,3),(4,4), (5,5), (6,6), (7,7), (8,8))
class PartitForm(forms.ModelForm):
    gols1 = forms.ChoiceField(choices=GOLS_CHOICES,
                              widget=forms.Select(attrs={"onChange":'refresh()'}))
    gols2 = forms.ChoiceField(choices=GOLS_CHOICES,
                              widget=forms.Select(attrs={"onChange":'refresh()'}))
    class Meta:
        model = PronosticPartit
        fields = ('gols1', 'gols2')


GrupForm = forms.modelformset_factory(PronosticPartit, form=PartitForm, extra=0)


@login_required
def pronostic(request):
    form = None
    grup = request.GET.get('grup', 'A')

    jugador = Jugador.objects.get(usuari=request.user)
    partits = Partit.objects.filter(grup__nom='A')

    # Creem els PronosticPartit que faltin
    for partit in partits:
        PronosticPartit.objects.get_or_create(jugador=jugador, partit=partit)

    grup_form = GrupForm(queryset=PronosticPartit.objects.filter(
        jugador=jugador, partit__grup__nom=grup))

    return render(
        request,
        'joc/grup.html',
        {
            'formset': grup_form,
            'height_banderes': 19,
            'width_banderes': 28,
            'border_banderes': 1,
        }
    )
