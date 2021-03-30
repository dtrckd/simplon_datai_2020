
1. Get the dataset and give an overview of the data
2. Show a graphics of the Close prices (you can use `plotly` to have zoom capability)
5. sort the dataset given the date 
6. decode the `date` value using the function `pd.to_datetime`. Explain the purpose of this step ?
3. normalize the dataset (You can use the `MinMaxScaler`). Explain the purpose of this step ?

# Model 1

Goal: to predict the last 250 days prices given all the previous observations.

Build a train and a test set in order to evaluate the model performance.

* Utiliser une fenetre d'observation de 50 jours
* Utiliser un sequence de prédiction de 1

