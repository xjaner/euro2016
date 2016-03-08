from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django import forms

from registration.supplements.base import RegistrationSupplementBase
from registration.forms import RegistrationForm


attrs_dict = {'class': 'required'}

class RegistrationSupplementForm(forms.Form):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs=dict(attrs_dict, maxlength=100)),
        label=_("First name"),
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs=dict(attrs_dict, maxlength=100)),
        label=_("Last name"),
    )

class RegistrationSupplement(RegistrationSupplementBase):
    form_class = RegistrationSupplementForm

    first_name = models.CharField(max_length=100, help_text="Please fill your first name")
    last_name = models.CharField(max_length=100, help_text="Please fill your last name")

    def __unicode__(self):
        # a summary of this supplement
        return "%s %s" % (self.first_name, self.last_name)
