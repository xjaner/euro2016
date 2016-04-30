from django.conf.urls import url

from . import views

app_name = 'joc'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^pronostic$', views.pronostic, name='pronostic'),
    url(r'^consulta$', views.consulta, name='consulta'),
    url(r'^usuaris$', views.usuaris, name='usuaris'),
    url(r'^entrada_admin$', views.entrada_admin, name='entrada_admin'),
]
