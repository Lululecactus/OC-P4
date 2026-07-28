# Logiciel de gestion de tournoi d'échecs

Application Python en ligne de commande pour gérer les tournois
d'échecs d'un club local. Fonctionne entièrement hors ligne,
sans connexion internet ni base de données externe.

## Prérequis

- Python 3.10 ou supérieur

## Installation

1. Cloner le repository :

```
git clone https://github.com/Lululecactus/OC-P4.git
cd chess_tournament
```

2. Créer et activer l'environnement virtuel :

```
python3 -m venv venv
source venv/bin/activate
```

3. Installer les dépendances :

```
pip3 install -r requirements.txt
```

## Lancer le programme

```
python3 main.py
```

## Navigation

```
Menu principal
├── 1. Joueurs
│   ├── 1. Ajouter un joueur
│   └── 2. Lister les joueurs
├── 2. Tournois
│   ├── 1. Créer un tournoi
│   ├── 2. Charger un tournoi existant
│   ├── 3. Inscrire des joueurs
│   ├── 4. Lancer le tour suivant
│   ├── 5. Enregistrer les résultats
│   └── 6. Voir le classement
├── 3. Rapports
│   ├── 1. Tous les joueurs (alphabétique)
│   ├── 2. Tous les tournois
│   ├── 3. Informations d'un tournoi
│   ├── 4. Joueurs d'un tournoi (alphabétique)
│   └── 5. Tours et matchs d'un tournoi
└── 4. Quitter
```

## Fonctionnalités

- Gestion des joueurs (ajout, liste alphabétique)
- Création et déroulement complet de tournois
- Génération automatique des appariements (aléatoire au tour 1,
  système suisse ensuite avec évitement des matchs répétés)
- Enregistrement des résultats (victoire, défaite, match nul)
- Sauvegarde automatique en JSON après chaque modification
- Rechargement complet de l'état au redémarrage
- 5 rapports conformes aux spécifications techniques

## Données

Les données sont sauvegardées dans le dossier `data/` :

- `data/players.json` : tous les joueurs du club
- `data/tournaments/` : un fichier JSON par tournoi

## Générer un nouveau rapport flake8

```
flake8 --format=html --htmldir=flake8_rapport
```

Ouvrir ensuite `flake8_rapport/index.html` dans un navigateur.

## Structure du projet

```
chess_tournament/
├── main.py
├── constants.py
├── setup.cfg
├── requirements.txt
├── README.md
├── models/
│   ├── player.py
│   ├── match.py
│   ├── round.py
│   ├── tournament.py
│   ├── player_storage.py
│   └── tournament_storage.py
├── views/
│   ├── menu_view.py
│   ├── player_view.py
│   ├── tournament_view.py
│   └── report_view.py
├── controllers/
│   ├── main_controller.py
│   ├── player_controller.py
│   ├── tournament_controller.py
│   └── report_controller.py
├── interfaces/
│   ├── player_interface.py
│   ├── tournament_interface.py
│   └── report_interface.py
├── data/
│   ├── players.json
│   └── tournaments/
└── flake8_rapport/
```
