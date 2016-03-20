# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joc', '0002_auto_20160319_2334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pronosticequipgrup',
            name='diferencia',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='pronosticequipgrup',
            name='favor',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='pronosticequipgrup',
            name='posicio',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='pronosticequipgrup',
            name='punts',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
