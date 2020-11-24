
keywords:  numpy, scikit-learn, logistic regression, descente de gradient, optimisation.


# Organisation

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
* the randomization of the data ?


What does the `train_test_split` function in sklearn do ?

use the `train_test_split` function of sklearn to build a test set with size that represents 20% of the original dataset (and 80% for the training set).

check that the ratio is correct.

**3) Predict Digits**

Predict one digit (for exemple `7`) with a logistic regression algorihmn plus (at least) **two** others of your choices. 

Show the performance results whithin a table for each models in terms of:
* the **precision** score on the testing set 
* the **recall** score on the testing set
* the inference time for each algorithm
* how many data the algorithms needs the be efficient (and why) ? 

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


