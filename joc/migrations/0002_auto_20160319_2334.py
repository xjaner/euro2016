# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joc', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jugador',
            name='punts',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='jugador',
            name='punts_anterior',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='jugador',
            name='punts_equips_encertats',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='jugador',
            name='punts_grups',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='jugador',
            name='punts_resultats',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='pronosticpartit',
            name='gols1',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='pronosticpartit',
            name='gols2',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
