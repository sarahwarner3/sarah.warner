#------ K NEAREST NEIGHBORS PROJECT ------# 

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import sklearn

df = pd.read_csv('KNN_Project_Data')

#Explore the data
  sns.pairplot(data = df, hue = 'TARGET CLASS')

#Standardize the variables
  from sklearn.preprocessing import StandardScaler
  scaler = StandardScaler()
  scaler.fit(df.drop('TARGET CLASS', axis = 1))
  scaled_features = scaler.transform(df.drop('TARGET CLASS', axis = 1))
  scaled_features
  df_features = pd.DataFrame(scaled_features, columns = df.columns[:-1])
  df_features

# Train, test, split
  from sklearn.model_selection import train_test_split
  X = df_features
  y = df['TARGET CLASS']
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 101)

#Use KNN
  from sklearn.neighbors import KNeighborsClassifier
  knn = KNeighborsClassifier(n_neighbors = 1)
  knn.fit(X_train, y_train)

#Predictions and evaluations
  prediction = knn.predict(X_test)
  from sklearn.metrics import confusion_matrix, classification_report
  print(confusion_matrix(y_test, prediction))
  print(classification_report(y_test, prediction))

#Choose a K value
  error_rate = []

  for i in range (1,60):
     knn = KNeighborsClassifier(n_neighbors = i)
     knn.fit(X_train, y_train)
     prediction_i = knn.predict(X_test)
     error_rate.append(np.mean(prediction_i != y_test))

  plt.figure(figsize = (12, 8))
  plt.plot(range (1,60),error_rate, color = 'green', linestyle = '--', marker = 'o', markerfacecolor = 'black', markersize = 10)
  plt.title('Error Rate vs K Value')
  plt.xlabel('K Value')
  plt.ylabel('Error Rate')

#Retrain with new K value
  knn = KNeighborsClassifier(n_neighbors = 30)
  knn.fit(X_train, y_train)
  new_prediciton = knn.predict(X_test)

  print(confusion_matrix(y_test, new_prediciton))
  print('\n')
  print(classification_report(y_test, new_prediciton))


