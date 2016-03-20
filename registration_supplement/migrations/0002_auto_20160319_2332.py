# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration_supplement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrationsupplement',
            name='first_name',
            field=models.CharField(max_length=100, verbose_name='First name'),
        ),
        migrations.AlterField(
            model_name='registrationsupplement',
            name='last_name',
            field=models.CharField(max_length=100, verbose_name='Last name'),
        ),
    ]
