# Generated by Django 4.2.6 on 2024-11-08 14:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("trips", "0015_rename_cabin_baggage_12kg_trip_cabin_baggage_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="trip",
            name="role",
            field=models.CharField(
                choices=[("driver", "Conducteur"), ("passenger", "Passager")],
                default="driver",
                max_length=10,
            ),
        ),
        migrations.AlterField(
            model_name="trip",
            name="end_city",
            field=models.CharField(
                choices=[
                    ("Almadies", "Almadies"),
                    ("Aéroport AIBD", "Aéroport AIBD"),
                    ("Bambilor", "Bambilor"),
                    ("Bargny", "Bargny"),
                    ("Ben Baraque", "Ben Baraque"),
                    ("Ben Tally", "Ben Tally"),
                    ("Bignona", "Bignona"),
                    ("Castor", "Castor"),
                    ("Centre Cutlure de Diamniadio", "Centre Cutlure de Diamniadio"),
                    ("Colobane", "Colobane"),
                    ("Dakar", "Dakar"),
                    ("Derklé", "Derklé"),
                    ("Diamniadio", "Diamniadio"),
                    ("Dieuppeul", "Dieuppeul"),
                    ("Diourbel", "Diourbel"),
                    ("Fann", "Fann"),
                    ("Fass", "Fass"),
                    ("Fatick", "Fatick"),
                    ("Goudomp", "Goudomp"),
                    ("Grand Dakar", "Grand Dakar"),
                    ("Grand Yoff", "Grand Yoff"),
                    ("Guinguinéo", "Guinguinéo"),
                    ("Guédiawaye", "Guédiawaye"),
                    ("HLM", "HLM"),
                    ("Hann", "Hann"),
                    ("Kaffrine", "Kaffrine"),
                    ("Kanel", "Kanel"),
                    ("Kaolack", "Kaolack"),
                    ("Keur Massar", "Keur Massar"),
                    ("Keur Ndiaye Lo", "Keur Ndiaye Lo"),
                    ("Kolda", "Kolda"),
                    ("Koumpentoum", "Koumpentoum"),
                    ("Koungheul", "Koungheul"),
                    ("Kounoune", "Kounoune"),
                    ("Kédougou", "Kédougou"),
                    ("Lac Rose", "Lac Rose"),
                    ("Liberté 5", "Liberté 5"),
                    ("Liberté 6", "Liberté 6"),
                    ("Louga", "Louga"),
                    ("Malika", "Malika"),
                    ("Matam", "Matam"),
                    ("Mbacké", "Mbacké"),
                    ("Mbour", "Mbour"),
                    ("Mermoz", "Mermoz"),
                    ("Médina", "Médina"),
                    ("Médina Coura", "Médina Coura"),
                    ("Médina Gounass", "Médina Gounass"),
                    ("Mékhé", "Mékhé"),
                    ("Ngor", "Ngor"),
                    ("Nioro du Rip", "Nioro du Rip"),
                    ("Nord Foire", "Nord Foire"),
                    ("Ouakam", "Ouakam"),
                    ("Ourossogui", "Ourossogui"),
                    ("Palais de Justice", "Palais de Justice"),
                    ("Parcelles Assainies", "Parcelles Assainies"),
                    ("Petersen", "Petersen"),
                    ("Pikine", "Pikine"),
                    ("Plateau", "Plateau"),
                    ("Point E", "Point E"),
                    ("Port Autonome de Dakar", "Port Autonome de Dakar"),
                    ("Richard-Toll", "Richard-Toll"),
                    ("Rufisque", "Rufisque"),
                    ("Saint-Louis", "Saint-Louis"),
                    ("Sandaga", "Sandaga"),
                    ("Sangalkam", "Sangalkam"),
                    ("Sicap Amitié", "Sicap Amitié"),
                    ("Sicap Baobab", "Sicap Baobab"),
                    ("Sicap Karack", "Sicap Karack"),
                    ("Sicap Liberté", "Sicap Liberté"),
                    ("Sicap Mbao", "Sicap Mbao"),
                    ("Sicap Mermoz", "Sicap Mermoz"),
                    ("Sicap Rue 10", "Sicap Rue 10"),
                    ("Sicap Sacré Coeur", "Sicap Sacré Coeur"),
                    ("Sokone", "Sokone"),
                    ("Stade Alassane Djigo", "Stade Alassane Djigo"),
                    ("Stade Amadou Barry", "Stade Amadou Barry"),
                    ("Stade Caroline Faye", "Stade Caroline Faye"),
                    ("Stade Dakar Arena", "Stade Dakar Arena"),
                    ("Stade Demba Diop", "Stade Demba Diop"),
                    ("Stade Iba Mar Diop", "Stade Iba Mar Diop"),
                    ("Stade Léopold Sédar Senghor", "Stade Léopold Sédar Senghor"),
                    ("Sédhiou", "Sédhiou"),
                    ("Tambacounda", "Tambacounda"),
                    ("Thiaroye", "Thiaroye"),
                    ("Thies", "Thies"),
                    ("Tivaouane", "Tivaouane"),
                    ("Touba", "Touba"),
                    ("Vélingara", "Vélingara"),
                    ("Yeumbeul", "Yeumbeul"),
                    ("Yoff", "Yoff"),
                    ("Ziguinchor", "Ziguinchor"),
                ],
                max_length=100,
            ),
        ),
        migrations.AlterField(
            model_name="trip",
            name="start_city",
            field=models.CharField(
                choices=[
                    ("Almadies", "Almadies"),
                    ("Aéroport AIBD", "Aéroport AIBD"),
                    ("Bambilor", "Bambilor"),
                    ("Bargny", "Bargny"),
                    ("Ben Baraque", "Ben Baraque"),
                    ("Ben Tally", "Ben Tally"),
                    ("Bignona", "Bignona"),
                    ("Castor", "Castor"),
                    ("Centre Cutlure de Diamniadio", "Centre Cutlure de Diamniadio"),
                    ("Colobane", "Colobane"),
                    ("Dakar", "Dakar"),
                    ("Derklé", "Derklé"),
                    ("Diamniadio", "Diamniadio"),
                    ("Dieuppeul", "Dieuppeul"),
                    ("Diourbel", "Diourbel"),
                    ("Fann", "Fann"),
                    ("Fass", "Fass"),
                    ("Fatick", "Fatick"),
                    ("Goudomp", "Goudomp"),
                    ("Grand Dakar", "Grand Dakar"),
                    ("Grand Yoff", "Grand Yoff"),
                    ("Guinguinéo", "Guinguinéo"),
                    ("Guédiawaye", "Guédiawaye"),
                    ("HLM", "HLM"),
                    ("Hann", "Hann"),
                    ("Kaffrine", "Kaffrine"),
                    ("Kanel", "Kanel"),
                    ("Kaolack", "Kaolack"),
                    ("Keur Massar", "Keur Massar"),
                    ("Keur Ndiaye Lo", "Keur Ndiaye Lo"),
                    ("Kolda", "Kolda"),
                    ("Koumpentoum", "Koumpentoum"),
                    ("Koungheul", "Koungheul"),
                    ("Kounoune", "Kounoune"),
                    ("Kédougou", "Kédougou"),
                    ("Lac Rose", "Lac Rose"),
                    ("Liberté 5", "Liberté 5"),
                    ("Liberté 6", "Liberté 6"),
                    ("Louga", "Louga"),
                    ("Malika", "Malika"),
                    ("Matam", "Matam"),
                    ("Mbacké", "Mbacké"),
                    ("Mbour", "Mbour"),
                    ("Mermoz", "Mermoz"),
                    ("Médina", "Médina"),
                    ("Médina Coura", "Médina Coura"),
                    ("Médina Gounass", "Médina Gounass"),
                    ("Mékhé", "Mékhé"),
                    ("Ngor", "Ngor"),
                    ("Nioro du Rip", "Nioro du Rip"),
                    ("Nord Foire", "Nord Foire"),
                    ("Ouakam", "Ouakam"),
                    ("Ourossogui", "Ourossogui"),
                    ("Palais de Justice", "Palais de Justice"),
                    ("Parcelles Assainies", "Parcelles Assainies"),
                    ("Petersen", "Petersen"),
                    ("Pikine", "Pikine"),
                    ("Plateau", "Plateau"),
                    ("Point E", "Point E"),
                    ("Port Autonome de Dakar", "Port Autonome de Dakar"),
                    ("Richard-Toll", "Richard-Toll"),
                    ("Rufisque", "Rufisque"),
                    ("Saint-Louis", "Saint-Louis"),
                    ("Sandaga", "Sandaga"),
                    ("Sangalkam", "Sangalkam"),
                    ("Sicap Amitié", "Sicap Amitié"),
                    ("Sicap Baobab", "Sicap Baobab"),
                    ("Sicap Karack", "Sicap Karack"),
                    ("Sicap Liberté", "Sicap Liberté"),
                    ("Sicap Mbao", "Sicap Mbao"),
                    ("Sicap Mermoz", "Sicap Mermoz"),
                    ("Sicap Rue 10", "Sicap Rue 10"),
                    ("Sicap Sacré Coeur", "Sicap Sacré Coeur"),
                    ("Sokone", "Sokone"),
                    ("Stade Alassane Djigo", "Stade Alassane Djigo"),
                    ("Stade Amadou Barry", "Stade Amadou Barry"),
                    ("Stade Caroline Faye", "Stade Caroline Faye"),
                    ("Stade Dakar Arena", "Stade Dakar Arena"),
                    ("Stade Demba Diop", "Stade Demba Diop"),
                    ("Stade Iba Mar Diop", "Stade Iba Mar Diop"),
                    ("Stade Léopold Sédar Senghor", "Stade Léopold Sédar Senghor"),
                    ("Sédhiou", "Sédhiou"),
                    ("Tambacounda", "Tambacounda"),
                    ("Thiaroye", "Thiaroye"),
                    ("Thies", "Thies"),
                    ("Tivaouane", "Tivaouane"),
                    ("Touba", "Touba"),
                    ("Vélingara", "Vélingara"),
                    ("Yeumbeul", "Yeumbeul"),
                    ("Yoff", "Yoff"),
                    ("Ziguinchor", "Ziguinchor"),
                ],
                max_length=100,
            ),
        ),
    ]