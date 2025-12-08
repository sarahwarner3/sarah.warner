#------ RANDOM FOREST PROJECT ------# 

#Explore publicly available data from LendingClub.com. Lending Club connects people who need money (borrowers) with people who have money (investors).
#Hopefully, as an investor you would want to invest in people who showed a profile of having a high probability of paying you back. Try to create a model that will help predict this.
#Use lending data from 2007-2010 and to classify and predict whether or not the borrower paid back their loan in full.

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('loan_data.csv')

#Explore the data
  plt.figure(figsize = (10,6))
  sns.set_style('darkgrid')
  data[data['credit.policy']==1]['fico'].hist(bins = 30, alpha = 0.5, color = 'blue', label = 'Credit Policy = 1')
  data[data['credit.policy']==0]['fico'].hist(bins = 30, alpha = 0.5, color = 'red', label = 'Credit Policy = 0')
  plt.legend()
  plt.xlabel('FICO')

  plt.figure(figsize = (10,6))
  sns.set_style('darkgrid')
  data[data['not.fully.paid']==1]['fico'].hist(bins = 30, alpha = 0.5, color = 'blue', label = 'Not Fully Paid = 1')
  data[data['not.fully.paid']==0]['fico'].hist(bins = 30, alpha = 0.5, color = 'red', label = 'Not Fully Paid = 0')
  plt.legend()
  plt.xlabel('FICO')

  sns.jointplot(data = data, x = 'fico', y = 'int.rate', color = 'purple')

  plt.figure(figsize = (10,4))
  sns.lmplot(data = data, x = 'fico', y = 'int.rate', hue = 'credit.policy', col = 'not.fully.paid', palette = 'Set1')

#Set up the data
  data.info()
  cat_feats = ['purpose']
  final_data = pd.get_dummies(data, columns = cat_feats, drop_first = True)
  final_data

#Train, test, split
  from sklearn.model_selection import train_test_split
  X = final_data.drop('not.fully.paid', axis = 1)
  y = final_data['not.fully.paid']
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 101)

#Train decision tree model
  from sklearn.tree import DecisionTreeClassifier
  dtree = DecisionTreeClassifier()
  dtree.fit(X_train, y_train)

#Predictions and evaluation of the decision tree
  from sklearn.metrics import classification_report, confusion_matrix
  predictions = dtree.predict(X_test)
  print(classification_report(y_test, predictions))
  print(confusion_matrix(y_test, predictions))

#Train the random forest model
  from sklearn.ensemble import RandomForestClassifier
  rfc = RandomForestClassifier()
  rfc.fit(X_train, y_train)

#Predictions and evaluation
  new_predictions = rfc.predict(X_test)
  print(classification_report(y_test, new_predictions))
  print(confusion_matrix(y_test, new_predictions))


