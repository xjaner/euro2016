# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joc', '0011_auto_20160501_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partit',
            name='empat',
            field=models.PositiveSmallIntegerField(null=True),
        ),
    ]
