# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joc', '0013_auto_20160517_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jugador',
            name='posicio',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='jugador',
            name='posicio_anterior',
            field=models.SmallIntegerField(),
        ),
    ]
