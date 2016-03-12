from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django import forms

from registration.supplements.base import RegistrationSupplementBase
from registration.forms import RegistrationForm


class RegistrationSupplement(RegistrationSupplementBase):
    first_name = models.CharField(max_length=100, verbose_name=_("First name"))
    last_name = models.CharField(max_length=100, verbose_name=_("Last name"))

    def __unicode__(self):
        # a summary of this supplement
        return "%s %s" % (self.first_name, self.last_name)

    def save(self, *args, **kwargs):
        self.registration_profile.user.first_name = self.first_name
        self.registration_profile.user.last_name = self.last_name
        self.registration_profile.user.save()
        super(RegistrationSupplement, self).save(*args, **kwargs)
