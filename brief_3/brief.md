
keywords:  numpy, scikit-learn, logistic regression, descente de gradient, optimisation.

# Description

Mr Pontier is back and need your help. This times, he needs to automatically detect hand-written digits written on picture that represents the phone number of his clients and collaborator. Has he have thousands of document, this will take for too long to do it manually. This is why he asked you if you can design an algorithm that automatically detect the number from the picture.

Furthermore, Mr Pontier wants to understand how the algorithm works, and wants to observe the convergence for further improvments.


# Proposed Plan

**1) Get and understand your data**

git clone the repository and run the given notebook.

what is the type of the data ?

How many pixel has one data instance ?

What is the type of data of one pixel ? what does it represents ?


**2) Prepare your ML algorithm**

> Veille
How do evaluate classification algorithms ?
* https://scikit-learn.org
* wikipedia
* towards data science
* ...

> Questions
* Write the equation of the **precision** and **recall** score and explicit what each terms represents.
* explain the purpose of the training set ?
* explain the prpose of the testing set ?
<!--* the randomization of the data ?-->


What does the `train_test_split` function in sklearn do ?

use the `train_test_split` function of sklearn to build a test set with size that represents 20% of the original dataset (and 80% for the training set).

check that the ratio is correct.

**3) Predict Digits**

In the dataset we have multiple label. Therefore, to start we will predict in a binary case. It meansthat that we will predict only if an image is a given digit (for exemple `7`) or not.

To do that we will a **logistic regression** algorithm plus (at least) **two** others of your choices. 

Fit the model and show the performance results whithin a table for each models in terms of:
* the **precision** score on the testing set 
* the **recall** score on the testing set
* the inference time for each algorithm

How many input data the algorithms needs the be efficient (and why) ? 

**4) Gradient descent ?**

> veille
What algorithm uses sklearn to estimate the model parameters for the logistic regression ?

We want to observe the convergence of the performance.
To do so, we want to implement our own version of the Logistic regression inference algorithm.

Show the convergence of the performance results with two graphics:
* the **precision** score on testing set AND training set 
* the **recall** score on testing set AND training set 


What is the impact of the learning rate on the convergence ?
What difference do you observe on the results between the training set and testing set


