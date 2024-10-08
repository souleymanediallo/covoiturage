# Generated by Django 4.2.6 on 2024-08-16 23:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("trips", "0007_trip_return_date_trip_return_time_trip_return_trip_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="trip",
            name="weekdays",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Lundi", "Lundi"),
                    ("Mardi", "Mardi"),
                    ("Mercredi", "Mercredi"),
                    ("Jeudi", "Jeudi"),
                    ("Vendredi", "Vendredi"),
                    ("Samedi", "Samedi"),
                    ("Dimanche", "Dimanche"),
                ],
                max_length=50,
                null=True,
            ),
        ),
    ]
