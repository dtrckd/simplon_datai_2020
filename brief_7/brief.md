
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
2. Use the PCA to improve the speed of your similarity search with 100 components. Does the result are coherent.


## LastFM Project

M. Pontier vous contact pour l'aider à construire un système de recommandation. Il dispose d'une base de données comportant des données concernant ses utilisateurs (anonymisé) contenant les artistes qu'ils écoutent sur sa plateforme ainsi que le nombre d'écoutes. Monsieur pontier souhaite recommander à ses utilisateur  des artistes qu'il n'ont pas encore écoutés, et cela en fonction de leurs préférences musicale.

Monsieur pontier souhaite utiliser la librairie Lightfm, avec laquelle il a déjà un driver permettant de charger ses données qu'il vous fournit, un vrai bonus.
Monsieur Pontier à pu voir que la documentation comporte plusieurs modèle, il souhaite évaluer les modèle sur une jeux de train/test et utiliser le meilleurs modéle.

Pour l'évaluation, il souhaite comparer la mesure AUC, la précision et le rappel (visiter la documentation de Lightfm), qui devront être présenté dans un tableau.


#### Bonus 1

Comparer les résulats de l'AUC avec le meilleurs modéle de lightfm et une PCA (TruncatedSDV).


#### Bonus 2

L'apprentissage devant être le plus rapide possible tout en obtenant les meilleurs résultats, il vous est demandé de trouver le nombre d'itération permettant d'atteindre la convergence de 95% de la valeur maximal d'AUC sur le jeux de test.


### Veille

Quelle système de recommandation allez vous mettre en place ?

Qu'est ce que Lightfm ?

Qu'est ce un système de recommandation dit à "implicit feedback" ? Et a "explicit feedback ?


### Ressources: 

LightFM: https://github.com/lyst/lightfm

Jeux de données Last.fm : https://grouplens.org/datasets/hetrec-2011/

The world is large and we know just a small part of it, dont forget the big picture: https://github.com/jihoo-kim/awesome-RecSys
