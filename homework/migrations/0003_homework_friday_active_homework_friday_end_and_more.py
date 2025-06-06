# Generated by Django 4.2.11 on 2025-05-25 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0002_alter_homeworkschedule_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='homework',
            name='friday_active',
            field=models.BooleanField(default=False, verbose_name='Vendredi actif'),
        ),
        migrations.AddField(
            model_name='homework',
            name='friday_end',
            field=models.TimeField(blank=True, null=True, verbose_name='Vendredi retour'),
        ),
        migrations.AddField(
            model_name='homework',
            name='friday_start',
            field=models.TimeField(blank=True, null=True, verbose_name='Vendredi départ'),
        ),
        migrations.AddField(
            model_name='homework',
            name='monday_active',
            field=models.BooleanField(default=False, verbose_name='Lundi actif'),
        ),
        migrations.AddField(
            model_name='homework',
            name='monday_end',
            field=models.TimeField(blank=True, null=True, verbose_name='Lundi retour'),
        ),
        migrations.AddField(
            model_name='homework',
            name='monday_start',
            field=models.TimeField(blank=True, null=True, verbose_name='Lundi départ'),
        ),
        migrations.AddField(
            model_name='homework',
            name='saturday_active',
            field=models.BooleanField(default=False, verbose_name='Samedi actif'),
        ),
        migrations.AddField(
            model_name='homework',
            name='saturday_end',
            field=models.TimeField(blank=True, null=True, verbose_name='Samedi retour'),
        ),
        migrations.AddField(
            model_name='homework',
            name='saturday_start',
            field=models.TimeField(blank=True, null=True, verbose_name='Samedi départ'),
        ),
        migrations.AddField(
            model_name='homework',
            name='sunday_active',
            field=models.BooleanField(default=False, verbose_name='Dimanche actif'),
        ),
        migrations.AddField(
            model_name='homework',
            name='sunday_end',
            field=models.TimeField(blank=True, null=True, verbose_name='Dimanche retour'),
        ),
        migrations.AddField(
            model_name='homework',
            name='sunday_start',
            field=models.TimeField(blank=True, null=True, verbose_name='Dimanche départ'),
        ),
        migrations.AddField(
            model_name='homework',
            name='thursday_active',
            field=models.BooleanField(default=False, verbose_name='Jeudi actif'),
        ),
        migrations.AddField(
            model_name='homework',
            name='thursday_end',
            field=models.TimeField(blank=True, null=True, verbose_name='Jeudi retour'),
        ),
        migrations.AddField(
            model_name='homework',
            name='thursday_start',
            field=models.TimeField(blank=True, null=True, verbose_name='Jeudi départ'),
        ),
        migrations.AddField(
            model_name='homework',
            name='tuesday_active',
            field=models.BooleanField(default=False, verbose_name='Mardi actif'),
        ),
        migrations.AddField(
            model_name='homework',
            name='tuesday_end',
            field=models.TimeField(blank=True, null=True, verbose_name='Mardi retour'),
        ),
        migrations.AddField(
            model_name='homework',
            name='tuesday_start',
            field=models.TimeField(blank=True, null=True, verbose_name='Mardi départ'),
        ),
        migrations.AddField(
            model_name='homework',
            name='wednesday_active',
            field=models.BooleanField(default=False, verbose_name='Mercredi actif'),
        ),
        migrations.AddField(
            model_name='homework',
            name='wednesday_end',
            field=models.TimeField(blank=True, null=True, verbose_name='Mercredi retour'),
        ),
        migrations.AddField(
            model_name='homework',
            name='wednesday_start',
            field=models.TimeField(blank=True, null=True, verbose_name='Mercredi départ'),
        ),
    ]
