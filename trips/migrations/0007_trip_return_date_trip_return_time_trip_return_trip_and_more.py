# Generated by Django 4.2.6 on 2024-08-16 17:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("trips", "0006_remove_trip_end_date_remove_trip_end_time_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="trip",
            name="return_date",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="trip",
            name="return_time",
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="trip",
            name="return_trip",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="trip",
            name="trip_type",
            field=models.CharField(
                choices=[("regular", "Régulier"), ("one_time", "Ponctuel")],
                default="one_time",
                max_length=10,
            ),
        ),
        migrations.AddField(
            model_name="trip",
            name="weekdays",
            field=models.CharField(
                blank=True,
                choices=[
                    ("monday", "Lundi"),
                    ("tuesday", "Mardi"),
                    ("wednesday", "Mercredi"),
                    ("thursday", "Jeudi"),
                    ("friday", "Vendredi"),
                    ("saturday", "Samedi"),
                    ("sunday", "Dimanche"),
                ],
                max_length=50,
                null=True,
            ),
        ),
    ]
