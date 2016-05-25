# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joc', '0014_auto_20160523_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jugador',
            name='punts',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='jugador',
            name='punts_anterior',
            field=models.SmallIntegerField(default=0),
        ),
    ]
