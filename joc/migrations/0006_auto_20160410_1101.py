# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joc', '0005_auto_20160408_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partit',
            name='equip1',
            field=models.ForeignKey(related_name='equip1', to='joc.Equip', null=True),
        ),
        migrations.AlterField(
            model_name='partit',
            name='equip2',
            field=models.ForeignKey(related_name='equip2', to='joc.Equip', null=True),
        ),
    ]
