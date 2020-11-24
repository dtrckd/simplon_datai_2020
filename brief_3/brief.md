
keywords: numpy, scikit-learn, logistic regression, descente de gradient, optimisation.

# Detect hand-written digits with logistic regression and explore gradient descent

# Description

Mr Pontier is back and needs your help. This times, he needs to automatically detect hand-written digits written on pictures that represents the phone numbers of his clients and collaborators.
Because he has thousands of documents, this will take far too long to do it manually. This is why he asked you if you can design an algorithm that automatically detect the number from the pictures.

Furthermore, Mr Pontier wants
* to understand how the algorithm works,
* to compare the performance with several classification algorithms 
* to observe the convergence of a grandient descent algorithm for further investigation.


# Proposed Plan

**1) Get and understand your data**

git clone the repository and run the given notebook in https://github.com/dtrckd/simplon_datai_2020/blob/master/brief_3/.

what is the type of the data ?

How many pixel has one data instance ?

What is the type of data of one pixel ? what does it represents ?


**2) Prepare your ML algorithm**

> Veille
How to evaluate classification algorithms ?
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

In the dataset we have multiple labels. Therefore, to start we will predict in a binary case. It means that that we will predict only if an image is a given digit (for exemple `7`) or not.

To do so, we will a **logistic regression** algorithm plus (at least) **two** others of your choices. 

Fit the model and show the performance results whithin a table for each models in terms of:
* the **precision** score on the testing set 
* the **recall** score on the testing set
* the inference time for each algorithm

How many input data the algorithms needs the be efficient (and why) ? 

Compare the performance on the training set. What do you observe ?

**4) Multi-class classification**

Fit now the algorithm in the multiclass case (ie using all the the classes (target)).

Show the result with
* the confusion matrix (see sklearn.metrics.plot_confusion_matrix)
* the classification report (see sklearn.metrics.classification_report)


**5) Gradient descent ?**

We want to observe the convergence of the performance.
To do so, we want to implement our own version of the Logistic regression inference algorithm.

> veille
What algorithm uses sklearn to estimate the model parameters for the logistic regression ?
* What are the keys equations we need to implement the algorithm ?
* what is the difference between the gradient descent and the stochastic gradient descent ?

Write the *pseudo-code* of the algorithm to be sure to understand all the different steps.
https://fr.wikipedia.org/wiki/Pseudo-code

Implement the gradient descent for the logistic regression.


Show the convergence of the performance results with two graphics:
* the **precision** score on testing set AND training set 
* the **recall** score on testing set AND training set 


What is the impact of the learning rate on the convergence ?
What difference do you observe on the results between the training set and testing set
