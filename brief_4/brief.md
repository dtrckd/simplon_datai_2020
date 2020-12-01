
keywords: NLP (TALN), classification.

# The Spam Detector

# Description

Madame Esposito devellope pour son entreprise un chatbot dans le but de répondre automatiquement à ses nombreux clients. Cependant son programme recoit un grand nombre de message malveillant ou à charactere publicitaire ce qui degrade les performance de son bot en plus d'occasionner des traitements informatique se répercutant sur sa facture d'electricité.

Madame Esposito vous a conacté afin de créer un programme capable de detecter automatiquement les SPAM. 
Pour cela, elle a construit un jeux de donnée comportant un ensemble de SMS de type SPAM et NON SPAM (HAM), disponible à l'addresse suivante : 
http://www.dt.fee.unicamp.br/~tiago/smsspamcollection/

Par ailleurs, afin d'intégrer les résultats dans son équipe, elle nous demande les choses suivantes:
* Afin d'estimer le cout du devellopement et suivre le projet, une checklist des taches à réaliser doit être rédigé.
* Vous devez créer des fonctions pour les diférentes partie de votre code afin de pouvoir les réutiliser facilement
* Vous devez effectuer une validation croisé (cross-validation) sur 10 jeux de'apprentissage et de test différent. Le seed doit être fixé à 42 et le jeux de test doit représenter 20% des données.
* Comparer au moins trois algorithme de classification en terme de **f1 score**. Lequel est le plus puissant ?

## Bonus


Pouvez améliorer les résultats ?
* est-ce que la lemmatisation améliore les résultats ?
* est-ce que la racinisation (stemming) améliore les résultats ?

* est-ce que la lemmatisation améliore les résultats ?
* est-ce que la racinisation (stemming)  améliore les résultats ?

Une fois ces étapesréalisées, reproduire la même expérience avec le jeux suivant, représant cette fois des commentaires Youtube :
https://archive.ics.uci.edu/ml/datasets/YouTube+Spam+Collection

Les performances sont-elles similaire à ceux obtenus avec le jeux de données précedent ?

Madame esposito souhaite controler si les modéles appris avec le premier jeux de données sont capable de prédire les données de test du deuxième jeu et vice-versa.
Réaliser un tableau comparant
* les résultats de prédiction du modeles appris sur les SPAN SMS pour prédire les SPAM commentaire youtube.
* et les résultats de prédiction du modeles appris surles SPAM commentaire youtube pour prédire les SPAM SMS youtube



# Proposed Plan

**1) Veille en Traitement du langage + checklist+45min**

https://becominghuman.ai/a-simple-introduction-to-natural-language-processing-ea66a1747b32

https://towardsdatascience.com/your-guide-to-natural-language-processing-nlp-48ea2511f6e1

https://code.tutsplus.com/fr/tutorials/introducing-the-natural-language-toolkit-nltk--cms-28620

https://towardsdatascience.com/introduction-to-natural-language-processing-for-text-df845750fb63

* parsing and tokenization ?
* vectorization ? Bag of words ?
* advantage of TFIDF ?
* stops words ?

**2) Load, clean and prepare the data**

Vectoriser et netoyer vos données.
https://scikit-learn.org/stable/modules/feature_extraction.html#text-feature-extraction

Quelle est le type Python de vos données après vectorisation.

* Quelle sont les 10 mots les plus fréquent dans le jeux de données ?
* Les moins fréquents ?
* Tracer la distribution de la fréquence des mots présents dans le jeux de données. Qu'obersvez vous ?




**Aides/propositions**
* Stop words avec NLTK
* scikit-learn pour la vectorization

**3) Apprenstissage

Que représente la mesure f1 ?
Quelles sont ces avantages sur d'autre mesure tel que la précision le rappel ou l'accuracy ?

**3) Veille cross validation**
https://scikit-learn.org/stable/modules/cross_validation.html

Utilisez la méthode de [ShuffleSplit](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.ShuffleSplit.html#sklearn.model_selection.ShuffleSplit) pour construire vos jeux de données permettant la validation croisée.

**4) Train**

Fit the models and compare the performance in a table that show
* the mean of the f1 score
* the standard deviation of the f1 score

Qu'observez vous ?

