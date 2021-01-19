
# Recommander Systems

Construire, comprendre et tuner un système de recommandation.

# Description

## Familarisation

Les systèmes de recommandations sont utilisé traditionnellement et comme le nom l'indique pour recommander du contenu à des utilisateurs.
Par exemple pour recommander un film à des utilisateurs en fonctions de ceux qu'ils ont vue, ou de la musique, ou des vidéos ou encore implémenter des fonctionnalités "more like this".

Nous allons commencer par suivre et reproduire les étapes de ce tuto: 

*  https://www.datacamp.com/community/tutorials/recommender-systems-python

En assumant que vous avez peu de RAM, nous allons nous arrêter au moment de calculer la  `compute_sim` variable.


**step1 : simple recommander**
Quelle est la complexité en mémoire de cette opération ?
(utiliser cosine_similarity qui utilise moins de mémoire (quand même 8Go, possible sur collab)
Cela rentre t'il sur votre machine ?

Qu'essaye de faire l'auteur avec ce calcul ?
Comment pouvons-nous contourner ce problème ?


**step2 : content based recommander**

implémenter la deuxiéme partie en évitant le produit de matrice.

**step3 : amélioration**

coder les 2 améliorations :
1. Introduce a popularity filter: this recommender would take the 30 most similar movies, calculate the weighted ratings (using the IMDB formula from above), sort movies based on this rating, and return the top 10 movies.
2. Other crew members: other crew member names, such as screenwriters and producers, could also be included.


## LastFM Project

to come...
