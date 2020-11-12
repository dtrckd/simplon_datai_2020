# Construire un moteur de recherche d'emploi 

compétences: c1 c2 c3 c4 c5 c20
Keywords: Scraping, Scrapy, MongoDB, RSS, Flask, Open Data, client-serveur, URL, Requete HTTP


## Description

Construire un moteur de recherche d'emploi à partir de données bruts présentes sur le web et develloper une application client-serveur pour acceder aux données.

## Contexte

Face à la montée du chômage systémique lié aux perturbation sur le marché du travail, les demandeurs d'emploi vont drastiquement augmenter et les emplois evoluer.
Cela va occasionner un fort besoin en recherche d'emploi.
Dans ce contexte, M. Pontier CEO de la société FlashBot cherche à develloper un moteur de recherche d'emploi et à fait appel à votre expertise.
Ils cherchent à construire un système permettant d'agréger des offres d'emploi à partir de données disponible sur l'Internet, à la fois rapidement et de manière innovante.
L'objectif étant de faciliter la recherche d'emploi et de maximiser les chances qu'un demandeur d'emploi trouve une offre adaptée pour lui.

Plusieurs pateforme existantes offrent des API permettant de rechercher des offres d'emplois.
Cependant les données sont dispersés, hétérogènes et ne permettent pas de faire de l'offre adapté.

Aujourd'hui M. Pontier cherche à exploiter un **flux RSS** à partir du lien suivant: http://rss.jobsearch.monster.com/rssquery.ashx?q=big data

La mission consiste à exploiter ce lien pour récolter le maximum de fiche d'emploi et les stocker en Base De Donnée (BDD) afin de les rendres accessibles et facilliter l'ajout de nouveaux documents.
Pour ce faire le client suggère l'utilisation d'une BDD **NoSQL** orienté document dans le but de faciliter:
* l'ajout de nouveaux document avec des formats différents
* la recherche d'information textuelles

Enfin, le client souhaite créer une application client-serveur permettant à un utilisateur de rechercher les offres d'emploi dans sa BDD à partir de requetes **HTTP**.

En conclusion, le client vous propose de designer et implémenter le systéme avec les caractéristiques suivantes:
* une bot/programme en python pour récolter les données et les envoyer à la BDD. <!--(Attension: Limiter votre nombre de requêtes pour la phase de test pour ne pas vous faire bannir du site cible!)-->
* Pour chaque document vous devez créer une entrée dans une BDD orienté document avec tout les champs présent (titre, description, etc)(le client suggére MongoDB) .
* Chaque document inséré en BDD devra avoir un champ correspondant au terme de recherche utilisé lors de la requete au flux RSS.
* le nombre d'elements dans la bdd doit être optimisé, c'est à dire que les doublons doivent être ecartés.
* un application client-serveur doit permettre de faire des requetes à la BDD. Notamment vous devez créer une page permettant de faire une recherche textuelle sur l'ensemble des documents récupérer et de retourner la liste des 10 premiers documents les plus pertinents.


### Bonus Tech
* améliorer le retour d'une requete client en affichant le nombre de document totale qui ont matché une recherche
* Creer une nouvelle route dans votre serveur/backend pour afficher les statistiques de votre base de donnée depuis une requete client: 
    * nombre de documents totale,
    * nombre de mot unique totale dans l'ensemble des documents,
    * nombre de mots non unique totale
* créer un fichier requirements.txt permettant d'installer automatiquement les dépendances python.


### Bonus Data
* Comment peut-on mesurer la pertinence pour le classement des documents ? Comment est-elle mesurer ?
* afficher la distribution (histogramme) de la répartition des offres d'emploi par métiers.
* quelles sont les 20 mots les plus fréquents dans les offres d'emplois ? (En dehors des **stopwords**) le 10 bi-gram les plus fréquents ?
* Combien d'offre d'emploi différent avez vous pu trouver sur Monster ? Pouvez vous augmentez ce nombre avec un lexique différent



## Ressources

mongodb: 
* https://www.mongodb.com/
* https://docs.mongodb.com/
scrapy:
* https://scrapy.org
* https://docs.scrapy.org



## Livrable

un git par apprenants avec les éléments suivants:
1. le bot, qui doit pouvoir être lancé pour alimenter la base de données.
2. le serveur, qui doit pouvoir être lancé et servir (ie répondre) à des requetes HTTP.
3. un fichier Readme.md qui décrit succinctement votre code et explique comment lancer votre programme, les éventuelles arguments et comment effectuer les requêtes de recherche.

## Modalité pédagogique

durée: 3 jours  
groupe: collaboration en trinôme  

### Organisations

###### Jour1

1. Découverte du sujet des groupes et de l'organisation didactique : 30 min pour laisser les groupes relire et discuter le brief ensemble, déterminer une feuille de route, puis point pour faire remonter les questions et regarder quelques feuille de route.
2. Installation de MongoDB guidé (le but n'est pas de perdre trop de temps à l'installation).

```markdown
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

    Si l'installation a fonctionné, vous pourrez renter dans un interpreteur mongodb avec la commande suivante:

        docker exec -it mongodb mongo


    **avec apt**

    voir le tuto pour debian ou ubuntu sur la doc mongo.
```


3. veilles MongoDB
4. stratégie pour récolter les données ?
5. suite ?


## Critére de perfomance

**critère humain**
* la moyenne d'avancement entre tout les groupes doit être maximale, et l'ecart type minimal


**critère tech**
* la rapidité d'executions des requêtes utilisateur. 
* qualité du code (structure, commentaires et fonctionnalité).
* qualité de l'interface utilisateur pour requeter le moteurs de recherche.

