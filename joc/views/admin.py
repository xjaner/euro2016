# -*- coding: utf-8 -*-
import datetime

from django.shortcuts import render
from django import forms
from django.contrib.admin.views.decorators import staff_member_required

from joc.models import Partit


GOLS_CHOICES = (('-1', '-'), (0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7),
                (8, 8))
EMPAT_CHOICES = ((1, 1), (2, 2))


class PartitAdminForm(forms.ModelForm):
    gols1 = forms.ChoiceField(choices=GOLS_CHOICES,
                              widget=forms.Select(attrs={"onChange": 'actualitza()'}))
    gols2 = forms.ChoiceField(choices=GOLS_CHOICES,
                              widget=forms.Select(attrs={"onChange": 'actualitza()'}))
    empat = forms.ChoiceField(choices=EMPAT_CHOICES,
                              widget=forms.RadioSelect,
                              required=False)

    class Meta:
        model = Partit
        fields = ('gols1', 'gols2', 'empat')


PartitsAdminForm = forms.modelformset_factory(
    Partit,
    form=PartitAdminForm,
    extra=0,
)


def actualitza_classificacio(request):
    pass


@staff_member_required
def entrada_admin(request):
    # Si és un POST, guardem els valors del formulari
    if request.method == 'POST':

        admin_form = PartitsAdminForm(request.POST)
        if admin_form.is_valid():
            admin_form.save()
        else:
            # TODO: Falta crear una pàgina d'error i que em notifiqui!
            pass

        try:
            actualitza_classificacio(request)
        except Exception:
            # TODO: Falta crear una pàgina d'error i que em notifiqui!
            pass

    admin_form = PartitsAdminForm(
        queryset=Partit.objects.filter(
            gols1=-1,
            diaihora__lt=datetime.datetime.now()-datetime.timedelta(minutes=105),
        )
    )

    return render(
        request,
        'joc/entrada_admin.html',
        {
            'formset': admin_form,
            'height_banderes': 19,
            'width_banderes': 28,
            'border_banderes': 1,
        }
    )
