
1. Get the dataset and give an overview of the data
2. Show a graphics of the Close prices (you can use `plotly` to have zoom capability)
5. sort the dataset given the date 
6. decode the `date` value using the function `pd.to_datetime`. Explain the purpose of this step ?
3. normalize the dataset (You can use the `MinMaxScaler`). Explain the purpose of this step ?

# Many to one model

Goal: predict the last 250 days prices given a sequence of previous observations. For each single price prediction we will use only the last 50 past days to predict the next price day.

Build a train and a test set in order to evaluate the model performance.

* Utiliser une fenetre d'observation de 50 jours
* Utiliser une sequence de prédiction de 1

# Many to many model


Reproduce this experiments but this time predict the value for several dayt in the future. Show the results in a grid plot with 3, 6, 10 days.


