# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistrationSupplement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(help_text='Please fill your first name', max_length=100)),
                ('last_name', models.CharField(help_text='Please fill your last name', max_length=100)),
                ('registration_profile', models.OneToOneField(related_name='_registration_supplement_registrationsupplement_supplement', editable=False, to='registration.RegistrationProfile', verbose_name='registration profile')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
