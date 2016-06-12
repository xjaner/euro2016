from django.db.models import Q, F
from django.views import generic

from joc.models import Jugador


class ClassificacioView(generic.ListView):
    template_name = "joc/classificacio.html"

    def get_queryset(self):
        return Jugador.objects.filter(usuari__is_active=True).filter(~Q(usuari_id=1)).annotate(
            dif_pos=F('posicio_anterior') - F('posicio')).annotate(
            dif_punts=F('punts') - F('punts_anterior')).order_by('posicio')
