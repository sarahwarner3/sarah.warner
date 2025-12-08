#------ NATURAL LANGUAGE PROCESSING PROJECT ------# 

#Attempt to classify Yelp Reviews into 1 star or 5 star categories based off the text content in the reviews.

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

yelp = pd.read_csv('yelp.csv')

yelp['text length'] = yelp['text'].apply(len)

#Explore the data
  p1 = sns.FacetGrid(yelp, col = "stars")
  p1.map(sns.histplot, "text length", bins=20)

  sns.boxplot(data = yelp, x = 'stars', y = 'text length', hue = 'stars', legend = False)

  sns.countplot(data = yelp, x = 'stars', hue = 'stars', legend = False)

  stars = yelp.groupby('stars').mean(numeric_only = True)
  stars

  stars_corr = stars.corr()
  stars_corr
  sns.heatmap(data = stars_corr, cmap = 'coolwarm', annot = True)

#NLP classification
  yelp_class = yelp[(['stars'] == 1) | (yelp['stars'] == 5)]
  yelp_class.head()
  X = yelp_class['text']
  y = yelp_class['stars']
  from sklearn.feature_extraction.text import CountVectorizer
  cv = CountVectorizer()
  X = cv.fit_transform(X)

#Train, test, split
  from sklearn.model_selection import train_test_split
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 101)

#Train the model
  from sklearn.naive_bayes import MultinomialNB
  nb = MultinomialNB()
  nb.fit(X_train, y_train)

#Predictions and evaluations
  predictions = nb.predict(X_test)
  from sklearn.metrics import confusion_matrix, classification_report
  print(confusion_matrix(y_test, predictions))
  print('\n')
  print(classification_report(y_test, predictions))

#Using text processing
  from sklearn.feature_extraction.text import TfidfTransformer
  from sklearn.pipeline import Pipeline
  pipeline = Pipeline([
     ('bow', CountVectorizer()), #strings to token integer counts
     ('tfidf', TfidfTransformer()), #integer counts to weighted TF-IDF scores
     ('classifier', MultinomialNB()), #train on TF-IDF vectors with Naive Bayes classifier])

#Using the pipeline
  X = yelp_class['text']
  y = yelp_class['stars']
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 101)
  pipeline.fit(X_train, y_train)
  predictions = pipeline.predict(X_test)
  print(confusion_matrix(y_test, predictions))
  print('\n')
  print(classification_report(y_test, predictions))
  


