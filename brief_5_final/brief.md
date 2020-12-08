# La roue des émotions

Construit d’après les travaux du psychologue américain Robert Plutchik, la roue des émotions est un modèle des émotions humaines et peut facilement servir à définir des personnages, ainsi que leur évolution dans une trame narrative. 

Depuis quelques années, les dispositifs de communication médiatisée par ordinateur (CMO) sont massivement utilisés, aussi bien dans les activités professionnelles que personnelles. Ces dispositifs permettent à des participants distants physiquement de communiquer. La plupart implique une communication écrite médiatisée par ordinateur (CEMO) : forums de discussion, courrier électronique, messagerie instantanée. Les participants ne s’entendent pas et ne se voient pas mais peuvent communiquer par l’envoi de messages écrits, qui combinent, généralement, certaines caractéristiques des registres écrit et oral (Marcoccia, 2000a ; Marcoccia, Gauducheau, 2007 ; Riva, 2001). 

Imaginez que vous souhaitez savoir ce qui se passe derrière votre écran d'ordinteur, qui sont vos contacts les plus actifs et quelle est leur personnalité (pas banal comme question !!). Vous allez alors vous lancer dans l’analyse de leur narration et tenter d’extraire quelle émotion se dégage de chacune des phrases.

Chez Simplon nous utilisons tous les jours des outils de discussion textuels et nous construisons nos relations sociales et professionnelles autour de ces dispositifs. Pour entretenir des rapports sociaux stables, sereins, de confiance et efficaces, au travers des outils de communication écrites, lorsqu'il n'est pas possible d'avoir la visio (avec caméra), il est nécessaire de détecter des éléments "clés" dans les channels de discussions / mails qui nous permettront de déceler de la colère, de la frustration, de la tristesse ou encore de la joie de la part d'un collègue ou d'un amis pour adapter nos relations sociales. 
En tant qu'expert en data science, nous allons vous demander de développer un modèle de machine learning permettant de classer les phrases suivant l'émotion principale qui en ressort.

Pour des questions d’ordre privé, nous ne vous demanderons pas de nous communiquer les conversations provenant de votre réseau social favori ou de vos emails mais nous allons plutôt vous proposer deux jeux de données contenant des phrases, ces fichiers ayant déjà été annoté.

Vous devrez proposer plusieurs modèles de classification des émotions et proposer une analyse qualitative et quantitative de ces modèles en fonction de critères d'évaluation. Vous pourrez notamment vous appuyer sur les outils de reporting des librairies déjà étudiées. Vous devrez investiguer des au travers de la librairie NLTK quels sont les traitements qui peuvent améliorer vos classifications (rajouter des features, Embedding Word, stopwords) .

Deux jeux de données annotés vous sont fournis. Vous devrez sélectionner un des jeux de données pour réaliservosapprentissage et l'évaluation de vos modèles.
Question : 
Apprendre avec un des jeux de données permet de prédire avec l'autre. Est-ce que les deux fichiers combinés permettent d'apprendre avec l'un et avec l'autre (transfert d'apprentissage)

Vous devrez ensuite présenter vos résultats sous la forme d'un dashboard muli-pages Dash. 
La première page du Dashboard sera dédiée à l'analyse et au traitement des données. Vous pourrez par exemple présenter les données "brut" sous la forme d'un tableau puis les données pré-traitées dans le même tableau avec un bouton ou menu déroulant permettant de passer d'un type de données à un autre. Sur cette première page de dashboard seront accessibles vos graphiques ayant trait à votre première analyse de données (histogramme, bubble chart, scatterplot etc). 
Une deuxième page du Dashboard sera dédiée aux résultats issues des classifications . Il vous est demandé de comparer les résultats d'au moins 4 classifiers. Sur cette page de dashboard pourra se trouver par exemple, des courbes de rappel de précision: (trace la précision et le rappel pour différents seuils de probabilité), un rapport de classification (un rapport de classification visuel qui affiche la precision, le recall, le f1-score, support) une carte thermique, ou encore une matrice de confusion. Une dernière page de Dashboard affichera l'analyse finale de votre travail (quel est l'algorithme de classification le plus efficace pour ce cas d'étude etc., par exemple sous forme de tableau).

 Herberger le dashboard sur le cloud de datavisualisation Héroku (https://www.heroku.com/)

Vos travaux devront être “poussés” sur Github au plus tard le Jeudi 17 Décembre à 17h30 (le lien sera accessible via simplonline). Les rendus tardifs ne seront pas pris en compte et les compétences ne seront donc pas validées !

