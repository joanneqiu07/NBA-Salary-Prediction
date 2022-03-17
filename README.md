# nba-salary-prediction
Final project for PIC 16A Winter 2022

# Group Members: 
Joanne Qiu, Yupei Hu, Shikang Yang 

# Project Description
The project is about to use past stats, such as scores, player efficiency rate, shooting percentage, for NBA
players to predict their salary for the future season by applying multiple regression. The inputs will be the
basic stats for the player and the outputs will be a numerical value of salary prediction.

# Package requirements
pandas, numpy, plotly.express, matplotlib.pyplot, seaborn, sklearn.model_selection, sklearn.metrics, sklearn.linear_model, statsmodels.api, sklearn.decomposition, sklearn.ensemble

Download the cleaner.py(https://github.com/joanneqiu07/nba-salary-prediction)

# Detailed description
1. Features Engineering
import two datasets and clean the data with the Cleaner class. 
clean the salary column. combine two datasets together. Done data cleaning

2. Distribution Graph
Use Plotly to create an interactive plot

![newplot](https://user-images.githubusercontent.com/85484264/158737280-9cb2cf2e-de5e-4d65-8d00-dd7051a8c2e8.png)

Create histograms to see the distributions of different variables

![hist](https://user-images.githubusercontent.com/85484264/158738170-b6d38dc4-c77a-4e18-bd5e-74bb67bf7c04.PNG)

3. Basic Statistcs
Check for multilinearity

![Hotmap](https://user-images.githubusercontent.com/85484264/158738312-6b5e27bc-fa66-4db1-9b7c-4bbb930f0dd8.PNG)

separate the data into label and train set.

4. Train, Test Spliting

5. Defining metrics

6. Linear Regression
Build a linear regression model and fit it to the training set.
Test the regression model.
Fit a linear model using the Ordinary Least Squares.

7. Principle Component Analysis
Since there are some features that have multi-colinearity, we can use PCA to reduce the dimensions of our input. Reformat and view results, reduce the features to two.

8. AdaBoost
Build an AdaBoost Regression model and check its performance.

9. RandomForest
Build a random forest model and check its performance.

# Scope and limitations
The limitation of this program is that the features need to be modified according to different Datasets. You can modify the parameters according to your purpose. More features can be extended to make different predictions.

# License and terms of use
MIT License and Terms of use

# References and acknowledgement
NBA players contracts in 2021-2022 on the Basketball Reference site(https://www.basketballreference.com/contracts/players.html).

# Background and source of the dataset
NBA players stats in 2020-2021 on Kaggle(https://www.kaggle.com/justinas/nba-players-data).

NBA players contracts history in 2011-2019 on Kaggle(https://www.kaggle.com/jarosawjaworski/current-nba-players-contracts-history).

All NBA players stats on the NBA data site(https://www.nba.com/stats/)

# Tutorials
1. NBA Salary Prediction using Multiple Regression: A tutorial of using a linear regression model to predict NBA players’salary in R(https://www.kaggle.com/koki25ando/nba-salary-prediction-using-multiple-regression/report). 

2. Plotly tutorials on the official website: tutorials of using Plotly to visualize data(https://plotly.com/python/plotly-fundamentals/).








