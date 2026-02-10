# COVOITURAGE

Site en production : [covoiturage.sn](https://www.covoiturage.sn/)

## Description
Covoiturage.sn est la plateforme de référence pour le covoiturage au Sénégal.
Elle permet aux conducteurs et passagers de publier et rechercher des trajets
à travers tout le pays (Dakar, Thiès, Saint-Louis, Ziguinchor, Touba, etc.),
qu'il s'agisse de trajets ponctuels ou de trajets domicile-travail réguliers.

## Contexte du projet
Ce projet répond à un besoin concret de mobilité partagée au Sénégal,
en proposant une alternative économique et écologique aux transports traditionnels.
La plateforme est utilisée en production par des conducteurs et passagers réels.

## Fonctionnalités principales
- Recherche de trajets par ville de départ et d'arrivée
- Publication de trajets ponctuels (aller simple / aller-retour)
- Publication de trajets domicile-travail récurrents
- Gestion des places disponibles et tarification en FCFA
- Système d'inscription et d'authentification des utilisateurs
- Profils conducteur et passager
- Blog : actualités, conseils et bons plans (assurance, écologie, tourisme, etc.)
- Pages destinations pour le référencement SEO
- Interface responsive (Bootstrap 5)
- Stockage des médias sur AWS S3

## Stack technique
- **Langage** : Python 3.12+
- **Framework** : Django 5.x
- **Base de données** : PostgreSQL
- **Frontend** : Bootstrap 5, HTML5, CSS3, JavaScript
- **Stockage média** : AWS S3
- **Hébergement** : OVH Cloud (Ubuntu)
- **Serveur web** : Nginx + Gunicorn

## Architecture & bonnes pratiques
- Séparation des responsabilités (apps Django)
- Variables d'environnement pour les données sensibles
- Configuration production sécurisée
- Déploiement Linux (Ubuntu) avec Nginx et Gunicorn
- Slugs et UUIDs pour des URLs propres et sécurisées

## Installation locale (développement)

```bash
git clone git@github.com:souleymanediallo/covoiturage.git
cd covoiturage
python -m venv venv
source venv/bin/activate
```

## Base de données

Créer une base de données PostgreSQL et configurer les variables d'environnement pour la connexion.
```bash
createdb covoiturage_db
```

Créer un fichier `.env` à la racine du projet et renseigner vos variables d'environnement :
```bash
touch .env
```

Exemple de variables :
```
SECRET_KEY=your-secret-key
DEBUG=True
DATABASE_URL=postgres
AWS_ACCESS_KEY_ID=xxx
AWS_SECRET_ACCESS_KEY=xxx
AWS_STORAGE_BUCKET_NAME=xxx
```

Installer les dépendances du projet et démarrer le serveur de développement :
```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Déploiement

L'application est hébergée en production sur pythonanywhere et sera déployée sur OVH Cloud (Ubuntu) avec :

- Gunicorn comme serveur d'application
- Nginx comme reverse proxy
- PostgreSQL comme base de données
- Stockage des médias sur AWS S3
- Certificat SSL (Let's Encrypt)

> **Note** : Migration en cours depuis PythonAnywhere vers OVH Cloud.

## Améliorations possibles
- Tests automatisés (pytest / Django TestCase)
- Système de notifications (email / SMS)
- Intégration d'un paiement mobile (Wave, Orange Money)
- Application mobile (React Native / Flutter)
- Système d'avis et de notation entre utilisateurs
- Calcul d'empreinte carbone économisée

## Auteur
**Souleymane Diallo** — Réalisation & Développement

## Licence
Ce projet est sous licence MIT.

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Django](https://img.shields.io/badge/Django-5.x-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-blue)
![License](https://img.shields.io/badge/License-MIT-yellow)
