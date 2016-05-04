from django.views import generic

from joc.models import PronosticPartit


class ConsultaView(generic.ListView):
    template_name = 'joc/consulta.html'
    context_object_name = 'pronostics'

    def get_queryset(self):
        return PronosticPartit.objects.filter(jugador__usuari=self.request.user)
