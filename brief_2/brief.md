

# Construire un moteur de recherche d'emploi 

c3 c20 c2 c5 c2 c4 c1


## Description

Construire un moteur de recherche d'emploi à partir de donnée brut présente sur le web.
Keywords: Scraping, Scrapy, MongoDB, RSS, Flask, Open Data

## Contexte

Face à la monté du chomage systémique, les demandeurs d'emploi vont drastiquement augmenter. Cela va occasionner un fort besoin en recherche d'emploi.
Dans ce contexte, nous cherchons à construire un systéme permettant d'aggréger des offres d'emploi disponible sur l'internet. 
L'objectif étant de faciliter la recherche d'emploi et de maximiser les chances qu'un demandeur d'emploie trouve une offre adapté pour lui.

La source des donnée proviendra dans un premier temps d'un **flux RSS** du lien suivant: http://rss.jobsearch.monster.com/rssquery.ashx
Ce lien permet notamment de filtrer les résultats à l'aide d'un champs textuel. Ce champs peut être renseigner en ajoutant à l'URL le paramètre `q` contenant la champs à chercher.
Par exmple en requetant l'URL suivante: `http://rss.jobsearch.monster.com/rssquery.ashx?q=machine learning`, pour cherche les métiers traitant de "machine learning".

Afin de récupérer un large nombre de fiche d'emploi pour alimenter notre base de donnée, nous allons requeter le flux RSS donné en utilisant des mot clés représentant les catégories de métier provenant de l'open data. Vous devrez notamment aggréger les terminologie présentees dans les deux catalogues suivants:
* https://www.data.gouv.fr/fr/datasets/r/ccf8aec2-3463-414c-b9ed-1d416f2b7a96 : récupérer tout les termes unique du "libéllé ROME"
* https://api.opendata.onisep.fr/downloads/5fa5949243f97/5fa5949243f97.json : récupérer tout les termes unique du "libéllé métier"

Muni de cette ensemble lexical, vous êtes chargé de designer et implémenter un bot charger de récupérer l'ensemble des fiches métiers pour chaque mot du lexique construit. (Attention limiter votre nombre de requete pour les phase de test pour ne pas vous faire ban du site cible). Ce bot doit répondre au cararistiques suivantes : 
* le bot doit prendre en paramètre (peut importe comment) le fichier lexical que vous avez contruit
* pour chaque entrer de ce ficher lexical le bot doit extraire tout les documents présents dans le flux RSS avec chacun des champs présents (title, description, etc).
* pour chaque document **UNIQUE** vous devais créer une entrée dans une base données NoSQL orienté document (tel que MongoDB)
* insérer pour chaque document le terme de recherche avec la requete RSS à retourner

Finalement, vous devez créer une application simple (type client serveur) permettant d'acceder à votre base de donnée. Notamment vous devez créer une page permettant de faire une recherche textuelle sur l'ensemble des documents récupérer et de retourner la liste des 10 premiers documents les plus pertinents.

### Bonus

* retourner le nombre de document totale correspondant à une requetes.
* afficher la distribution (histogramme) de la répartition des offres d'emploi par métiers.
* afficher les statisques de votre base de donnée suivantes: Nombre de documents totale, nombre de mot unique totale dans l'ensemble des documents, nombre de mots non unique totale
* quelles sont les 20 mots les plus frequents dans les offres d'emploi ? (En dehors des **stopwords**)
* Combien d'offre d'emploi différent avez vous pu trouver sur Monster ? Pouvez vous augmentez ce nombre avec un lexique différet
* Accelerer l'acces à votre base de donnée définnissant des indexs.
* créer un requirements.txt permettant d'installer automatiquement les dépendances python



## Ressources

mongodb: 
* https://www.mongodb.com/
* https://docs.mongodb.com/
scrapy:
* https://scrapy.org
* https://docs.scrapy.org



## Livrable

un git par apprenants avec les élements suivants:
1. le bot, qui doit pouvoir être lancé pour alimenter la base de données.
2. le serveur, qui doit pouvoir être lancé et requetable depuis un navigateur.
3. un fichier Readme.md qui décrit succintement votre code et explique comment lancer votre programme, les eventuelles arguments et comment effectuer les requetes de recherche.

## Modalité pédagogique

durée: 3 jours
groupe: collaboration en trinome

Jour1:

1. decouverte du sujet et des groupes et présentation
2. Installation de MongoDB guidé (le but n'est pas de perdre trop de temps à l'installation).

Voici deux méthodes pour installer mongo du plus simple au plus complexe (à utiliser en fonction de votre préférence ou en cas d'echec d'une méthode)

**avec docker**

Commencons par installer **docker**

soit avec : `sudo snap install docker`
ou avec `apt`: `apt install docker.io`

Ensuite, créer un repertoire ou seront stocker les donnée de la MongoDB, par exemple

    mkdir -p ~/data-mongodb

il suffit ensuite d'installer mongo avec la suivante suivante

    docker run -d -p 27017:27017 -v ~/src/data/mongo-docker:/data/db --name mongodb mongo:4.2 

ici, docker se charge d'installer tout le necessaire et de placer le tout dans un conteneur isolé.

Si l'installation a fonctionné, vous pourrer renter dans un interpreteur mongodb avec la commande suivante:

    docker exec -it mongodb mongo



**avec apt**

voir le tuto pour debian ou ubuntu sur la doc mongo




3. veilles MongoDB + 

+ veilles Mongodb + 



## Critére de perfomance

**critère humain**
* la moyenne d'avancement entre tout les groupes doit être maximale, et l'ecart type minimal


**critére tech**
* la rapidité de la réponse aux requetes utilisateur. 
* qualité du code (structure, commentaires et fonctionalité)
* qualité de l'interface utilisateur pour requeter le moteur de recherche

