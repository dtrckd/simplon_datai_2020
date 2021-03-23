# Avatar generator with generative deep learning

Afin de proposer un service de génération automatique d'avatar, la société **Dupond Père et Fils** vous mandate afin de développer l'application.

Pour ce faire, vous disposez d'un jeux de données d'avatars disponible ici (utilisez celui de 10000 images) : https://google.github.io/cartoonset/download.html
L'opérateur souhaite utilisé une technologie de modèle profond génératif de type GAN.
De plus, celui-ci dispose de ressource limité, il vous est demandé de redimensioner les images en 128x128 pixels.

On vous demande de réaliser les éléments suivants : 
* désigner le système d'apprentissage afin de produire un modèle entrainé pour le service de génération d'avatar
* créer une application web permettant de générer des avatars:
    - l'application affichera par défaut une grille ou seras affiché par défaut sur une même page 10x8 avatars (10 ligne 8 colonne).
    - un bouton permettant de régénérer les avatars.
    - 

Bonus : 
Développer un modèle alternatif utilisant un modèle type Variational Auto-Encoder (VAE)

durée: 2j


ressources: 
* Deep Learning with Python (Francois Chollet)
* https://machinelearningmastery.com/what-are-generative-adversarial-networks-gans/
* https://keras.io/examples/generative/dcgan_overriding_train_step/
