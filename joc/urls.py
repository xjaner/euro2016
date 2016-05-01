from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views
from views.usuaris import UsuarisView

app_name = 'joc'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^pronostic$', views.pronostic, name='pronostic'),
    url(r'^consulta$', views.consulta, name='consulta'),
    url(r'^usuaris$', login_required(UsuarisView.as_view()), name='usuaris'),
    url(r'^entrada_admin$', views.entrada_admin, name='entrada_admin'),
    url(r'^pronostic_admin$', views.pronostic_admin, name='pronostic_admin'),
]
