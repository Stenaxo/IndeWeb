# Projet Crawler Web

## Description
Ce projet implémente un crawler web en Python. Le crawler télécharge des pages à partir d'une URL de départ, extrait les liens de ces pages, et continue le processus jusqu'à un certain nombre d'URLs. Le projet utilise le multithreading pour améliorer l'efficacité du crawling et stocke les données des URLs visitées dans une base de données SQLite.

## Fonctionnalités
- **Crawling Multi-threadé** : Permet de traiter plusieurs pages simultanément.
- **Respect des règles `robots.txt`** : Le crawler vérifie le fichier `robots.txt` des sites pour s'assurer qu'il est autorisé à les explorer.
- **Politesse du Crawler** : Attend un temps défini entre les requêtes pour ne pas surcharger les serveurs des sites web.
- **Stockage des Données** : Enregistre les URLs visitées et leur date de visite dans une base de données SQLite.
- **Analyse des Sitemaps** : Tente de lire le fichier `sitemap.xml` pour une découverte plus efficace des URLs.

## Structure du Projet
- `main.py` : Fichier principal pour lancer le crawler.
- `crawler.py` : Contient la logique principale du crawler.
- `database.py` : Gère la création de la base de données et l'enregistrement des URLs.
- `utils.py` : Fournit des fonctions utilitaires pour lire `robots.txt` et `sitemap.xml`, et pour extraire les liens des pages.
- `requirements.txt` : Liste les dépendances nécessaires pour exécuter le projet.

## Installation et Exécution

### Prérequis
- Python 3.x
- pip (gestionnaire de paquets Python)

### Installation des Dépendances
Exécutez la commande suivante pour installer les dépendances requises :
```
pip install -r requirements.txt
```

### Lancement du Crawler
Pour démarrer le crawler, exécutez :
```
python main.py
```

## Contributions
- Lorenzo MATHIEU
