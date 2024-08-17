# Generated by Django 4.2.6 on 2024-08-17 18:34

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("trips", "0009_alter_trip_weekdays"),
    ]

    operations = [
        migrations.AlterField(
            model_name="trip",
            name="weekdays",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(
                    choices=[
                        ("Lundi", "Lundi"),
                        ("Mardi", "Mardi"),
                        ("Mercredi", "Mercredi"),
                        ("Jeudi", "Jeudi"),
                        ("Vendredi", "Vendredi"),
                        ("Samedi", "Samedi"),
                        ("Dimanche", "Dimanche"),
                    ],
                    max_length=255,
                ),
                blank=True,
                null=True,
                size=None,
            ),
        ),
    ]
