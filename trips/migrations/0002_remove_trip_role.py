# Generated by Django 4.2.6 on 2024-05-12 15:00

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("trips", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="trip",
            name="role",
        ),
    ]
