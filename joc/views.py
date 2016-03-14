from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django import forms
from joc.models import Jugador, Partit, PronosticPartit


class GrupForm(forms.ModelForm):
    gols1 = forms.IntegerField(min_value=0, max_value=8)
    gols2 = forms.IntegerField(min_value=0, max_value=8)
    class Meta:
        model = PronosticPartit
        fields = ('gols1', 'gols2', 'partit')

@login_required
def index(request):
    return render(request, 'joc/index.html')

@login_required
def pronostic(request):
    form = None
    if request.method == "GET":
        jugador = Jugador.objects.get(usuari=request.user)
        partit = Partit.objects.get(pk=1)
        pronostic_partit = PronosticPartit.objects.create(
            jugador=jugador, partit=partit)
        form = GrupForm(instance=pronostic_partit)
    return render(request, 'joc/grup.html', {'form': form})

@login_required
def consulta(request):
    return render(request, 'joc/index.html')

@login_required
def usuaris(request):
    return render(request, 'joc/index.html')
