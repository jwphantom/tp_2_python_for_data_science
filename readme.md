# Analytical Town - Application de classification des villes du Cameroun

Bienvenue dans l'application Analytical Town, une application web Flask conçue pour classer les villes du Cameroun, notamment Yaoundé, Douala, Bafoussam, et Garoua.

## Structure du projet

Le projet est organisé de la manière suivante :

app/
    init.py
    ###autres fichiers

    routes/
        init.py
        ###autres fichiers
    
    models/
        init.py
        ###autres fichiers

    templates/
        ###fichiers de vue

    utils/
        ### fichier de fonction

    database.py

    error.py

    config.py

run.py



- Le dossier `app` contient le code de l'application Flask.
- Le sous-dossier `routes` contient les fichiers de routage de l'application.
- Le sous-dossier `models` contient les modèles de données.
- Le sous-dossier `templates` contient les vues des routes.
- Le sous-dossier `utils` contient des fonctions statique.
- `database.py` contient la configuration de la base de donnée.
- `error.py` contient la gestion des erreurs web.
- `config.py` contient la configuration de l'application.
- `run.py` est le point d'entrée de l'application.

## Configuration de la base de données (Institut Saint Jean)

Pour que l'application fonctionne correctement, vous devez configurer la base de données. Utilisez les informations suivantes :

- Hôte : 192.145.239.38
- Nom de la base de données : ossute5_pointsinterest
- Utilisateur : ossute5_master2
- Mot de passe : ISJ_datascience+2023

Assurez-vous que ces informations sont correctement configurées dans le fichier `config.py`.

## Installation des dépendances

Avant de lancer l'application, assurez-vous d'installer les dépendances nécessaires en utilisant `pip` et le fichier `requirements.txt`. Exécutez la commande suivante à la racine de votre projet :

```shell
pip install -r requirements.txt
```

## Lancement de l'application

```shell
flask --app run run 
```

## Usage

L'application vous permet de classer les villes du Cameroun. Utilisez l'interface utilisateur pour interagir avec l'application et effectuer la classification des villes.


## Usage
- James Olongo (https://github.com/jwphantom)


## Licence

Ce projet est sous licence MIT
