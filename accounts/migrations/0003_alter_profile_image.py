# Generated by Django 4.2.6 on 2024-08-26 18:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0002_alter_profile_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="image",
            field=models.ImageField(
                blank=True,
                default="profile_pics/user.png",
                null=True,
                upload_to="profile_pics/%Y/",
            ),
        ),
    ]
