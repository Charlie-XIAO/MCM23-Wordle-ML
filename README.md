# The Mathematical Contest in Modeling (MCM'23)

Team 2316597 | Problem C

## Problem 1

### Statement

The number of reported results vary daily. Develop a model to explain this variation and use your model to create a prediction interval for the number of reported results on March 1, 2023. Do any attributes of the word affect the percentage of scores reported that were played in Hard Mode? If so, how? If not, why not?

### Solutions

For the first part of the question, it asked about the relation between the number of reported result and the date. `Q1-1.ipynb` used inverse proportional curves to fit the data (excluding the surging part), `Q1-2.ipynb` used ARIMA to fit the data (including the surging part), and `Q1-3.ipynb` used ARIMA to fit the data (excluding the surging part). `Q1-2.ipynb` seems not to be giving a reasonable prediction, but `Q1-1.ipynb` and `Q1-3.ipynb` produce very similar result when excluding the first 80 dates from the dataset. A prediction interval could be obtained by changing how many dates we exclude.

For the second part of the question, it asked about the attributes of the word that may affect the percentage of scores reported that were played in Hard Mode. `Q1-4.ipynb` analyzed the relation between character occurrence / character frequency and the Hard Mode percentage.

## Problem 2

### Statement

For a given future solution word on a future date, develop a model that allows you to predict the distribution of the reported results. In other words, to predict the associated percentages of (1, 2, 3, 4, 5, 6, X) for a future date. What uncertainties are associated with your model and predictions? Give a specific example of your prediction for the word EERIE on March 1, 2023. How confident are you in your model’s prediction?

### Solutions

`Q2-1.ipynb` analyzed the attributes ROC, POV, EYH, and EGH, and determined their correlation with the distribution of number of trials. `Q2-2.ipynb` used the Decision Tree Regression model to predict the distribution for the word EERIE. `Q2-3.ipynb` used the Random Forest Regression model to predict the distribution for the word EERIE. `Q2-2.ipynb` and `Q2-3.ipynb` gave almost the same prediction.
