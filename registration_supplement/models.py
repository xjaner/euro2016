from __future__ import unicode_literals
from django.db import models
from registration.supplements.base import RegistrationSupplementBase


class RegistrationSupplement(RegistrationSupplementBase):

    first_name = models.CharField(max_length=100, help_text="Please fill your first name")
    last_name = models.CharField(max_length=100, help_text="Please fill your last name")

    def __unicode__(self):
        # a summary of this supplement
        return "%s %s" % (self.first_name, self.last_name)
