#------ LINEAR REGRESSION PROJECT ------#

#Congratulations! You just got some contract work with an Ecommerce company based in New York City that sells clothing online but they also have in-store style and clothing advice sessions.
#Customers come in to the store, have sessions/meetings with a personal stylist, then they can go home and order either on a mobile app or website for the clothes they want.
#The company is trying to decide whether to focus their efforts on their mobile app experience or their website. They've hired you on contract to help them figure it out!

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

customers = pd.read_csv('Ecommerce Customers')

#Explore relationships across the entire data set
  sns.pairplot(data = customers)
  plt.show()

#Create a linear model plot of Yearly Amount Spent vs. Length of Membership
  sns.lmplot(data=customers, x = 'Length of Membership', y = 'Yearly Amount Spent')
  plt.grid()
  plt.show()

#Train and test the data
  customers.columns
  X = customers[['Avg. Session Length', 'Time on App', 'Time on Website', 'Length of Membership']]
  y = customers['Yearly Amount Spent']
  from sklearn.model_selection import train_test_split
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 101)

#Train the model
  from sklearn.linear_model import LinearRegression
  lm = LinearRegression()
  lm.fit(X_train, y_train)
  print('Coefficients: \n', lm.coef_)
  cdf = pd.DataFrame(lm.coef_, X.columns, columns = ['Coeff'])
  cdf

#Predict test data
  predictions = lm.predict(X_test)
  plt.scatter(y_test, predictions)
  plt.xlabel('Y Test')
  plt.ylabel('Predicted Y')
  plt.show()

#Evaluate the model
  from sklearn import metrics
  metrics.mean_absolute_error(y_test, predictions)
  metrics.mean_squared_error(y_test, predictions)
  np.sqrt(metrics.mean_squared_error(y_test, predictions))

#Residuals
  sns.displot((y_test - predictions), kde = True, bins = 40)
  plt.show()

#Conclusion
 cdf
   #For every unit increase in session length, Yearly amount spent increases by $25.98
   #For every unit increase in time on app, Yearly amount spent increases by $38.59
   #For every unit increase in time on website, Yearly amount spent increases by $0.19
   #For every unit increase in length of membership, Yearly amount spent increases by $61.28
#The company should focus more on their mobile app.
