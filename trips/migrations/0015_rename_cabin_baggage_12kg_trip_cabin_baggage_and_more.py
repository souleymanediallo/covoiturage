# Generated by Django 4.2.6 on 2024-08-23 15:45

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("trips", "0014_trip_cabin_baggage_12kg_trip_checked_baggage_23kg"),
    ]

    operations = [
        migrations.RenameField(
            model_name="trip",
            old_name="cabin_baggage_12kg",
            new_name="cabin_baggage",
        ),
        migrations.RenameField(
            model_name="trip",
            old_name="checked_baggage_23kg",
            new_name="checked_baggage",
        ),
    ]
