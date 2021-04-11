# Puissances 4 (extended)

## Description

Nous allons créer notre jeu de société, et un bot qui apprend à jouer automatiquement !


# Contexte

Vous devez développer un jeu de “puissance 4” similaire au jeu “4 in a row”. Dans ce jeu, deux joueurs s’affrontent. Ils doivent à tour de rôle poser un jeton dans une grille. Les jetons viennent se déposer dans l’emplacement libre le plus bas de la colonne choisie. Le joueur qui réussit à aligner 4 de ses jetons, dans n’importe quelle direction, gagne la partie. Le jeu doit être jouable dans les modes suivants :

* humain contre humain sur la même machine,
* humain contre IA
* IA contre IA.

L’IA doit proposer plusieurs niveaux de difficulté. La taille de la grille doit être paramétrable. Deux IA doivent être proposé, une aléatoire, et une autre entrainé par renforcement. (voir section IA)


## Structure

Le programme doit être développé suivant les trois grandes parties suivantes : 

* le moteur de jeu, 
* la partie graphique 
* l'IA (Intelligence Artificielle).

Le programme doit pouvoir être exécuté depuis un programme python simple (c'est à dire inférieur à 200 lignes de code). L'objectif étant de faire appel à des **modules python** pour la réutilisation de brique de code et afin d'anticiper la dette technique.

## Ligne de commandes

Votre programme doit supporter plusieurs paramètres en ligne de commande permettant de : 

* choisir le mode de jeu.
* définir les dimensions du plateaux.
* BONUS: options pour entrainer votre IA.

exemple de commandes: 

    python connect4.py --help
    python connect4.py --mode hxh  # pour humain contre humain
    python connect4.py --mode hxr  # pour humain contre robot (humain commencent)
    python connect4.py --mode rxh  # pour humain contre robot (robot commence)
    python connect4.py --mode rxr  # pour robot contre robot

## IA

L'algorithme par renforcement permet à un agent d'apprendre une stratégie de jeux afin de maximiser une certaine récompense.

L'objectif est d'implémenter un algorithme de type "off-policy" et "model-free". De plus nous souhaitons développer une approche type "deep reinforcement learning" afin de s'abstraire d'un connaissance exhaustive de l'ensemble de nombre d'états de jeux pour permettre un passage à l'échelle.

* Vous devez fournir une statistique de votre IA entrainée par renforcement : 
    - proportion de partie gagné
    - évolution du nombre de coup des parties
    - évolution de la loss de votre modèle

## Test Unitaires et Fonctionnels

Les testent permettent de vérifier un programme selon différent critère. Les test unitaires et fonctionnels, permettent d'automatiser la vérification de fonction et de scenario d'un programme automatiquement pour assurer qu'un cahier des charges est respecté (cad que le code fait bien ce qu'il est supposé faire). Cela permet notamment de faciliter la détection et la correction de bug lors de mise à jours ou de modification du code.

* Testez au moins deux fonctions critiques de votre code.
* Réalisez des test unitaires pour vérifier que le jeux détectes correctement les puissances 4.

Vos test doivent pouvoir être lancé depuis un script différent. Par exemple depuis un Makefile (e.g `make test`) ou depuis un script (e.g. `./test.py`).

## Documentation

Vous devez fournir une documentation **utilisateur** minimal. L'utilisation d'une section **Documentation** dans un Readme au format Markdown est recommandé.

# Modalité pédagogique 

Travaille en agence de développement.
Organisation Agile/Scrum.

# Critére de performance

Tournoi ou les bot des différentes agences s'affronteront.

# Ressources

* http://www.maths-pour-tous.org/cours-mej/doc/Dossier%20MeJ%202010-14/Dossier%20Mej%20%202011-12/Puissance%204/Compte-Rendu%20commun.pdf
* https://fr.wikipedia.org/wiki/Puissance_4
* http://mathieu.buard.free.fr/jeux/ludotheque/puissance4.html



DQN paper: https://www.cs.toronto.edu/~vmnih/docs/dqn.pdf
Openai RL ressources: https://spinningup.openai.com/en/latest/spinningup/rl_intro.html
RL cheatsheet: https://gist.github.com/dtrckd/807d5bbebe8ca36ac4a54f6680db8e40
retour d'un ingénieur sur des algo de bot (min-max et DQN) sur le puissance 4: https://www.eurodecision.com/construction-intelligence-artificielle-pour-le-jeu-puissance-4

Exemples d'algo type DQN avec Keras:
montain car : https://towardsdatascience.com/reinforcement-learning-w-keras-openai-dqns-1eed3a5338c
Cart Pole: https://www.analyticsvidhya.com/blog/2019/04/introduction-deep-q-learning-python/
