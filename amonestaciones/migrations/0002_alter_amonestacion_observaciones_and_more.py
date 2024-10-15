# Generated by Django 5.1.2 on 2024-10-13 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amonestaciones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amonestacion',
            name='observaciones',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='amonestacion',
            name='tarjeta',
            field=models.CharField(blank=True, choices=[('amarilla', 'amarilla'), ('roja', 'roja')], max_length=10, null=True),
        ),
    ]
