# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joc', '0006_auto_20160410_1101'),
    ]

    operations = [
        migrations.AddField(
            model_name='pronosticpartit',
            name='empat',
            field=models.PositiveSmallIntegerField(null=True),
        ),
    ]
