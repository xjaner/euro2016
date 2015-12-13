# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Equip',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom', models.CharField(max_length=128)),
                ('bandera', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Grup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Jugador',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pagat', models.BooleanField(default=False)),
                ('posicio', models.PositiveSmallIntegerField()),
                ('posicio_anterior', models.PositiveSmallIntegerField()),
                ('punts', models.PositiveSmallIntegerField()),
                ('punts_anterior', models.PositiveSmallIntegerField()),
                ('punts_resultats', models.PositiveSmallIntegerField()),
                ('punts_grups', models.PositiveSmallIntegerField()),
                ('punts_equips_encertats', models.PositiveSmallIntegerField()),
                ('usuari', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Partit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('diaihora', models.DateTimeField()),
                ('estadi', models.CharField(max_length=128)),
                ('equip1', models.ForeignKey(related_name='equip1', to='joc.Equip')),
                ('equip2', models.ForeignKey(related_name='equip2', to='joc.Equip')),
                ('grup', models.ForeignKey(to='joc.Grup')),
            ],
        ),
        migrations.CreateModel(
            name='PronosticEquipGrup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('posicio', models.PositiveSmallIntegerField()),
                ('punts', models.PositiveSmallIntegerField()),
                ('diferencia', models.PositiveSmallIntegerField()),
                ('favor', models.PositiveSmallIntegerField()),
                ('equip', models.ForeignKey(to='joc.Equip')),
                ('jugador', models.ForeignKey(to='joc.Jugador')),
            ],
        ),
        migrations.CreateModel(
            name='PronosticPartit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gols1', models.PositiveSmallIntegerField()),
                ('gols2', models.PositiveSmallIntegerField()),
                ('jugador', models.ForeignKey(to='joc.Jugador')),
                ('partit', models.ForeignKey(to='joc.Partit')),
            ],
        ),
        migrations.AddField(
            model_name='equip',
            name='grup',
            field=models.ForeignKey(to='joc.Grup'),
        ),
    ]
