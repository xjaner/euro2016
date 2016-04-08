from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from joc.models import Jugador


@login_required
def index(request):
    jugador = Jugador.objects.get(usuari=request.user)
    return render(
        request,
        'joc/index.html',
        {
            'jugador': jugador,
        }
    )
