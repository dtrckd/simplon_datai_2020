# Construire un moteur de recherche d'emploi 

compétences: c3 c20 c2 c5 c2 c4 c1  
Keywords: Scraping, Scrapy, MongoDB, RSS, Flask, Open Data  


## Description

Construire un moteur de recherche d'emploi à partir de données bruts présentes sur le web.

## Contexte

Face à la montée du chômage systémique(ça veut dire quoi?), les demandeurs d'emploi vont drastiquement augmenter. Cela va occasionner un fort besoin en recherche d'emploi.
Dans ce contexte, nous cherchons à construire un système (un progamme?) permettant d'agréger des offres d'emploi disponibles sur l'Internet. 
L'objectif étant de faciliter la recherche d'emploi et de maximiser les chances qu'un demandeur d'emploi trouve une offre adaptée pour lui.

La source des donnée proviendra dans un premier temps d'un **flux RSS** du lien suivant: http://rss.jobsearch.monster.com/rssquery.ashx
Ce lien (site?) permet notamment de filtrer les résultats à l'aide d'un champs textuel. Ce champs peut être renseigné en ajoutant à l'URL le paramètre `q` contenant la champs à chercher.
Par exemple en effectuant une requête à l'URL : `http://rss.jobsearch.monster.com/rssquery.ashx?q=machine_learning`, qui va chercher les métiers traitants de "machine learning".

Afin de récupérer un large nombre de fiches d'emploi pour alimenter notre base de données, nous allons faire une requête sur le flux RSS donné en utilisant des mot clés représentant les catégories des métiers provenant de l'open data (?). Vous devrez notamment agréger les terminologies présentées dans les deux catalogues suivants:
* récupérer tout les termes uniques du "libellé ROME" : https://www.data.gouv.fr/fr/datasets/r/ccf8aec2-3463-414c-b9ed-1d416f2b7a96
* récupérer tout les termes uniques du "libellé métier" : https://api.opendata.onisep.fr/downloads/5fa5949243f97/5fa5949243f97.json 

Muni de cette ensemble lexicale, vous êtes chargées de designer et implémenter un bot qui doit récupérer l'ensemble des fiches d'emploi pour chaque mot du lexique construit.
(Attention! Limiter votre nombre de requêtes pour la phase de test pour ne pas vous faire banner du site cible!)
Une bonne manière de construire ce bot est de respecter les caractéristiques suivantes: 
* Le bot doit prendre comme paramètre (peu importe comment) le fichier lexical que vous avez construit
* Pour chaque entrée de ce fichier lexical le bot doit extraire tout les documents présents dans le flux RSS avec chacun des champs présents (titre, description, etc).
* Pour chaque document **UNIQUE** vous devez créer une entrée dans une base de données NoSQL orientée document (tel que MongoDB)
* Insérer pour chaque document le terme de recherche avec la requête RSS à retourner (preciser)

Finalement, vous devez créer une application simple (type client serveur) permettant d'accéder à votre base de donnée. Notamment vous devez créer une page permettant de faire une recherche textuelle sur l'ensemble des documents récupérer et de retourner la liste des 10 premiers documents les plus pertinents.

Comment pourrait-on mesurer la pertinence ?

### Bonus

* retourner le nombre de document totale correspondant à une requêtes.
* afficher la distribution (histogramme) de la répartition des offres d'emploi par métiers.
* afficher les statistiques de votre base de donnée suivantes: Nombre de documents totale, nombre de mot unique totale dans l'ensemble des documents, nombre de mots non unique totale
* quelles sont les 20 mots les plus fréquents dans les offres d'emplois ? (En dehors des **stopwords**) le 10 bi-gram les plus fréquents ?
* Combien d'offre d'emploi différent avez vous pu trouver sur Monster ? Pouvez vous augmentez ce nombre avec un lexique différent
* Accélérer l'accès à votre base de donnée définissant des indexs.
* créer un fichier requirements.txt permettant d'installer automatiquement les dépendances python.



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
2. le serveur, qui doit pouvoir être lancé et qui accessible depuis un navigateur.
3. un fichier Readme.md qui décrit succinctement votre code et explique comment lancer votre programme, les éventuelles arguments et comment effectuer les requêtes de recherche.

## Modalité pédagogique

durée: 3 jours  
groupe: collaboration en trinôme  

### Organisations

###### Jour1

1. Découverte du sujet des groupes et de l'organisation didactique : 20 min pour laisser les groupes relire et discuter le brief ensemble, déterminer une feuille de route, puis point pour faire remonter les questions et regarder quelques feuille de route.
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
    * créer une collection
    * insérer à la main 2 ou 3 fiche d'emploi à partir du résultat renvoyé par le flux RSS utiliser `db.my_collection.insert({...})`. 
    * lister les documents de votre base à l'aide la function `db.my_collection.find`.
    * effectuer des requete textuelle sur les document que vous avez insérer: voir la doc sur la recherche textuelle: https://docs.mongodb.com/manual/text-search/ 
    * qu'est ce qu'un index ? comment mongo utilises les index et pourquoi ?


4. Créer le lexique de mots métiers.

5. ...

###### jour2

à venir...

## Critére de perfomance

**critère humain**
* la moyenne d'avancement entre tout les groupes doit être maximale, et l'ecart type minimal


**critére tech**
* la rapidité de la réponse aux requêtes utilisateur. 
* qualité du code (structure, commentaires et fonctionnalité)
* qualité de l'interface utilisateur pour requeter le moteur de recherche

