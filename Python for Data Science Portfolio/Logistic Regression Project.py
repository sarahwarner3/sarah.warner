#------ LOGISTIC REGRESSION PROJECT ------# 

#Work with an advertising data set and indicate whether or not a particular internet user clicked on an Advertisement.
#Try to create a model that will predict whether or not they will click on an ad based off the features of that user.

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline

ad_data = pd.read_csv('advertising.csv')

#Explore the data
  sns.jointplot(data = ad_data, x = 'Age', y = 'Area Income')
  plt.show()
  sns.jointplot(data = ad_data, x = 'Daily Time Spent on Site', y = 'Daily Internet Usage')
  plt.show()
  sns.pairplot(data = ad_data, hue = 'Clicked on Ad')
  plt.show()

#Train and test the data
  from sklearn.model_selection import train_test_split
  ad_data.columns
  X = ad_data[['Age', 'Area Income', 'Daily Internet Usage', 'Male', 'Daily Time Spent on Site']]
  y = ad_data['Clicked on Ad']
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 101)
  from sklearn.linear_model import LogisticRegression
  logmodel = LogisticRegression()
  logmodel.fit(X_train, y_train)

#Predictions and Evaluations
  predictions = logmodel.predict(X_test)
  from sklearn.metrics import classification_report, confusion_matrix
  print(classification_report(y_test, predictions))
  print(confusion_matrix(y_test, predictions))
