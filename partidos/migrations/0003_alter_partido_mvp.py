# Generated by Django 5.1.2 on 2024-10-13 12:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jugadores', '0001_initial'),
        ('partidos', '0002_alter_partido_equipo_local'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partido',
            name='mvp',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mvps', to='jugadores.jugador'),
        ),
    ]
