# Generated by Django 3.1.2 on 2020-10-09 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20201008_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='photos/souleymane.png', null=True, upload_to='photos'),
        ),
    ]
