
# Word embedding


## Decouvrir le word-embedding avec Keras ?

Explorer la couche Embeding (Word embedding) de Keras sur votre jeux de classification de texte (émotions)

Quelle est l'impact cette couche sur vos résultats entrainement ? 

**Advice**: Faite une fonction type "classification report" prenant en entré un modéle/expérience donnée et qui vous retourne les résultats de classification, dont notamment : 
* accuracy
* le f1 score pour chaque classe
* le temps d'apprentissage
* le nombre de neurone/poids de votre modèle


**Questions**:
- Quelle doit être le format de donnée en entrée de la couche "Embedding" ?
- Expliquer ce que fait et le rôle de la fonction `pas_sequence` ? Quelle sont les paramètres important de cette fonction ?
- Expliquer ce que fait et le rôle de la couche `GlobalMaxPool1d` ? Quelle sont les paramètre important ? Quelle alternatives existe il ?

Bonus: explorer différent modéle (ie paramètrisation) pour trouver le plus performant.

ressource: https://learn-neural-networks.com/world-embedding-by-keras/


