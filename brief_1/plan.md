# Plan j2 Régression Linéaire

### 0) Round table

Retour rapide sur la digestion de la journée précédente.

* Confusions ?
* Précisions ?

### 1) Veille Régression Linéaire

1. quelle est le principe de la régression linéaire ? Comment l'algorithme apprend-t-il ?
2. Dans quelle cas est t'il pertinent de l'utiliser ? Sur quelle mesure s'appuie t'on ?
3. Comment évaluer les performances de l'algorithme ?


### 2) Prédire le prix des voitures

Commencez par utiliser un algo de régression linéaire en prenant en compte l'age de la voiture seulement : 

* avec numpy (utiliser la fonction `numpy.polyfit`)
* avec scipy (utiliser la fonction `scipy.stats.linregres`)
* avec sklearn
* avec votre propre classe (Python). Implémentez notamment les méthodes `fit` et `predict` afin d'être compatible avec la librairie sklearn.

Tracer toutes les différents modèle "appris" par la régression linéaire sur un même graphe. Qu'observez vous ?

ressources: https://www.kaggle.com/sudhirnl7/linear-regression-tutorial

### 3) Évaluer les performances

Évaluer les performances des différentes implémentation de la régression linéaire en utilisant l'erreur quadratique moyenne (MSE). Pour cela, construisez un jeu de d'apprentissage et je de test (training and testing set).

Comparer les résultats dans un tableau (utilisez les frames pandas).


ressources:
* https://towardsdatascience.com/train-test-split-and-cross-validation-in-python-80b61beca4b6
* https://scikit-learn.org/stable/modules/model_evaluation.html#regression-metrics

### 4) Améliorer (Bonus)

Pouvez vous améliorer les performances de la régression linéaire: 
* en utilisant une régression linéaire **multivarié** (par ex. en utilisant les featues Kms_driven et Transmission
* en nettoyantes données ?
* autre ?





