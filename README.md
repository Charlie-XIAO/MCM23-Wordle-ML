# The Mathematical Contest in Modeling (MCM'23)

Team 2316597 | Problem C

## Problem 1

### Statement

The number of reported results vary daily. Develop a model to explain this variation and use your model to create a prediction interval for the number of reported results on March 1, 2023. Do any attributes of the word affect the percentage of scores reported that were played in Hard Mode? If so, how? If not, why not?

### Solutions

For the first part of the question, it asked about the relation between the number of reported result and the date. `Q1-1.ipynb` used inverse proportional curves to fit the data (excluding the surging part), `Q1-2.ipynb` used ARIMA to fit the data (including the surging part), and `Q1-3.ipynb` used ARIMA to fit the data (excluding the surging part). `Q1-2.ipynb` seems not to be giving a reasonable prediction, but `Q1-1.ipynb` and `Q1-3.ipynb` produce very similar result when excluding the first 80 dates from the dataset. A prediction interval could be obtained by changing how many dates we exclude.

The second part of the question is yet to be done.
