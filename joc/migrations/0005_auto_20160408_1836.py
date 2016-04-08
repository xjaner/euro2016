# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joc', '0004_auto_20160402_0101'),
    ]

    operations = [
        migrations.AddField(
            model_name='pronosticpartit',
            name='equip1',
            field=models.ForeignKey(related_name='equip1_pronostic', to='joc.Equip', null=True),
        ),
        migrations.AddField(
            model_name='pronosticpartit',
            name='equip2',
            field=models.ForeignKey(related_name='equip2_pronostic', to='joc.Equip', null=True),
        ),
    ]
