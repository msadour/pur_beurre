# GrandPy bot
## Installation
* Récupérer le projet via GitHub : En ligne de commande, dans le répertoire souhaité, lancer la commande : "clone https://github.com/msadour/pur_beurre.git"
* Installer les dépendances : Une fois le projet récupéré, en ligne de commande, placer vous dans le dossier du projet et lancer la commande suivante : "pip install -r requirements.txt".

## Pré requis en local
* Aller dans le dossier "website_pur_beurre" et editez le fichier "config.py" afin de mettre la valeur de website_online à False.
* Pour alimenter la base de donnée (Necessite internet) ainsi que le chargement des images : lancer la commande suivante (cela peut prendre beaucoup de temps !) : http://127.0.0.1:8000/website_pur_beurre/feed_database
* Si vous n'avez pas acces à internet, vous pouvez utiliser l'URL suivante : http://127.0.0.1:8000/website_pur_beurre/feed_database_by_mock

## Lancement
* En local,  le programme se lance en ligne de commande à la racine du projet avec la commande suivante : "python manage.py runserver". Une fois lancé, allez sur votre navigateur et entrez l'url suivante : http://127.0.0.1:8000/website_pur_beurre/home ;
* En ligne, allez sur l'adresse suivante : https://ms-purbeurre.herokuapp.com/website_pur_beurre/home

## Utilisation
* Une fois redirigé vers la page d'accueil il faut d'abord s'inscrire si vous n'avez pas de compte (autrement connectez vous directement) en renseignement un nom d'utilisateur, un email et un mot de passe.
* Une fois connecté, vous pouvez rechercher des substituts d'aliment.
* Si parmis les aliments il y en a qui vous convienne, sauvegardez les en cliquant sur l'icone representant une disquette orange.
* Vous pouvez retrouver les aliments substituées en cliquant sur l'icone representant une carrote.