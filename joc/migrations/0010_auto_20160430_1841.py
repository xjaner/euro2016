# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joc', '0009_auto_20160430_1840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partit',
            name='empat',
            field=models.PositiveSmallIntegerField(default=None, null=True, blank=True),
        ),
    ]
