# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joc', '0003_auto_20160320_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pronosticpartit',
            name='gols1',
            field=models.SmallIntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='pronosticpartit',
            name='gols2',
            field=models.SmallIntegerField(default=-1),
        ),
    ]
