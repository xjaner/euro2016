# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joc', '0007_pronosticpartit_empat'),
    ]

    operations = [
        migrations.AddField(
            model_name='partit',
            name='empat',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='partit',
            name='gols1',
            field=models.SmallIntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='partit',
            name='gols2',
            field=models.SmallIntegerField(default=-1),
        ),
    ]
