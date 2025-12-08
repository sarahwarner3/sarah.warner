#------ NEURAL NETWORKS PROJECT ------# 

#Use historical data from LendingClub on loans given out with information on whether the borrower defaulted, build a model that can predict if a borrower will pay back their loan.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('TensorFlow_FILES/lending_club_loan_two.csv')

#Explore the data
  sns.countplot(data = df, x = 'loan_status', hue = 'loan_status', palette = 'Set2')
  sns.histplot(data = df, x = 'loan_amnt', bins=40)
  sns.heatmap(df.corr(numeric_only=True),annot=True, cmap='viridis')
  sns.scatterplot(data = df, x = 'installment', y = 'loan_amnt')

  grade_order = sorted(df['grade'].unique())
  sns.countplot(data = df, x = 'grade', hue = 'loan_status', order = grade_order, palette = 'Paired')

  subgrade_order = sorted(df['sub_grade'].unique())
  sns.countplot(data = df, x = 'sub_grade', hue = 'sub_grade', palette = 'viridis', order = subgrade_order, hue_order = subgrade_order)
  sns.countplot(data = df, x = 'sub_grade', hue = 'loan_status', palette = 'viridis', order = subgrade_order)

  f_and_g = df[(df['grade'] == 'G') | (df['grade'] == 'F')]
  subgrade_order = sorted(f_and_g['sub_grade'].unique())
  sns.countplot(data = f_and_g, x = 'sub_grade', hue = 'sub_grade', palette = 'viridis', order = subgrade_order, hue_order = subgrade_order)
  sns.countplot(data = f_and_g, x = 'sub_grade', hue = 'loan_status', palette = 'viridis', order = subgrade_order)

  df['loan_repaid'] = df['loan_status'].map({'Fully Paid':1,'Charged Off':0})
  df[['loan_repaid', 'loan_status']]

#Data Preprocessing
  ((df.isnull().sum())/len(df))*100

  df['emp_title'].value_counts()
  df = df.drop('emp_title', axis=1)

  sorted(df['emp_length'].dropna().unique())
  sns.countplot(data = df, x = 'emp_length', hue = 'loan_status', palette = 'Set2', order = emp_length_order)
  emp_co = df[df['loan_status'] == 'Charged Off'].groupby('emp_length').count()['loan_status']
  emp_fp = df[df['loan_status'] == 'Fully Paid'].groupby('emp_length').count()['loan_status']
  emp_len = emp_co/emp_fp
  emp_len.plot(kind = 'bar')
  df = df.drop('emp_length', axis=1)

  df['purpose'].head(10)
  df['title'].head(10)
  df = df.drop('title', axis=1)

  df.corr(numeric_only = True)['mort_acc'].sort_values()
  total_acc_avg = df.groupby('total_acc').mean(numeric_only=True)['mort_acc']
  def fill_mort_acc(total_acc, mort_acc):
      if np.isnan(mort_acc):
          return total_acc_avg[total_acc]
      else:
          return mort_acc
  df['mort_acc'] = df.apply(lambda x: fill_mort_acc(x['total_acc'], x['mort_acc']), axis=1)
  df.isnull().sum()
  df = df.dropna()

  df['term'].value_counts()
  df['term'] = df['term'].apply(lambda term: int(term[:3]))

  df = df.drop('grade',axis=1)

  dummies = pd.get_dummies(df['sub_grade'], drop_first = True)
  df = pd.concat([df.drop('sub_grade', axis =1), dummies],axis=1)

  dummies = pd.get_dummies(df[['verification_status', 'application_type','initial_list_status','purpose']], drop_first = True)
  df = pd.concat([df.drop(['verification_status', 'application_type','initial_list_status','purpose'], axis =1), dummies],axis=1)

  df['home_ownership'].value_counts()
  df['home_ownership'] = df['home_ownership'].replace(['NONE','ANY'],'OTHER')
  dummies = pd.get_dummies(df['home_ownership'], drop_first = True)
  df = pd.concat([df.drop('home_ownership', axis =1), dummies],axis=1)

  df['zip_code'] = df['address'].apply(lambda address:address[-5:])
  dummies = pd.get_dummies(df['zip_code'], drop_first = True)
  df = pd.concat([df.drop('zip_code', axis =1), dummies],axis=1)
  df = df.drop('address', axis=1)

  df['earliest_cr_line'] = df['earliest_cr_line'].apply(lambda date: int(date[-4:]))

#Train, test, split
  from sklearn.model_selection import train_test_split
  df = df.drop('loan_status', axis =1)
  X = df.drop('loan_repaid', axis = 1)
  y = df['loan_repaid'].values
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=101)
  
  from sklearn.preprocessing import MinMaxScaler
  scaler = MinMaxScaler()
  X_train = scaler.fit_transform(X_train)
  X_test = scaler.transform(X_test)

#Create the model
  from tensorflow.keras.models import Sequential
  from tensorflow.keras.layers import Dense,Dropout
  X_train.shape

  model = Sequential()
  model.add(Dense(78, activation = 'relu'))
  model.add(Dropout(0.2))
  model.add(Dense(39, activation = 'relu'))
  model.add(Dropout(0.2))
  model.add(Dense(19, activation = 'relu'))
  model.add(Dropout(0.2))
  model.add(Dense(1, activation = 'sigmoid'))
  model.compile(loss = 'binary_crossentropy', optimizer = 'adam')

  model.fit(x = X_train, y = y_train, epochs = 50, batch_size = 256, validation_data = (X_test, y_test))

#Evaluate the model
  losses = pd.DataFrame(model.history.history)
  losses.plot()
  from sklearn.metrics import classification_report, confusion_matrix
  predictions = (model.predict(X_test) > 0.5).astype("int32")
  print(classification_report(y_test, predictions))
  df['loan_repaid'].value_counts()
  317696/len(df)

#Predict a new customer
  import random
  random.seed(101)
  random_ind = random.randint(0,len(df))
  new_customer = df.drop('loan_repaid',axis=1).iloc[random_ind]
  new_customer

  new_customer = scaler.transform(new_customer.values.reshape(1,78))
  (model.predict(new_customer) > 0.5).astype("int32")
  df.iloc[random_ind]['loan_repaid']
