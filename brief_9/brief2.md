# Word-embedding avec Keras




**Decouverte du word-embedding**

Explorer la couche Embeding (Word embedding) de Keras sur votre jeux de classification de texte (émotions) en s'appuyant sur la ressource suivante : 
https://realpython.com/python-keras-text-classification/

Quelle est l'impact de cette couche sur vos résultats d'entrainement ? 

**Advice**: Faite une fonction type "classification report" prenant en entrée un modéle/expérience donnée et qui vous retourne les résultats de classification, dont notamment : 
* accuracy
* le f1 score pour chaque classe
* le temps d'apprentissage
* le nombre de neurone/poids de votre modèle


Questions:
- Quelle doit être le format de donnée en entrée de la couche "Embedding" ?
- Expliquer ce que fait et le rôle de la fonction `pad_sequence` ? Quelle sont les paramètres important de cette fonction ?
- Expliquer ce que fait et le rôle de la couche `GlobalMaxPool1d` ? Quelle sont les paramètre important ? Quelle alternatives existe il ?

**Manipulation**

Extraire la matrice d'embedding et le dictionnaire de mappig des mots.
* Comment calculer la similarité entre deux mots ?

**Pre-trained model**

Utiliser un modéle d'embedding pré-entrainer (https://nlp.stanford.edu/projects/glove/), pour initialiser vos poids.
- Explisuqer le role du paramètre `trainable` ?
- Quelle est l'impact sur les performance ?

Bonus: explorer différent modéle (ie paramètrisation) pour trouver le plus performant. (**Tips**: You can use the Grid-Search function of scikit-learn with Keras model ;))


ressources:
- https://learn-neural-networks.com/world-embedding-by-keras/
- https://medium.com/@kadircanercetin/intuitive-understanding-of-word-embeddings-with-keras-6435fe92a57b


## Model explanation

- rétrospective sur le modèle de Deep learning, alignement, et brainstorm des améliorations possibles en terme de preprocesing et paramétrage.
- Ecriture d'un fonction permettant de prédire la classe d'un document avec le modèle. (rediscussion de l'interpétation de la fonction de sortie (sigmoid, softmax, linear). 
- veilles sur Lime et Shap
    * https://github.com/marcotcr/lime
    * https://github.com/slundberg/shap
- utiliser lime pour prédire la classification d'un document quelconque
- réaliser une enquête pour expliquer les features qui impact le modéle positivement et négativement (extrayez un certain nombre de document bien classé et mal classé pour chaque classe). Proposez des idées d'améliorations.

Bonus1: même exercice avec shap.
Bonus2: implementer vos améliorations.

