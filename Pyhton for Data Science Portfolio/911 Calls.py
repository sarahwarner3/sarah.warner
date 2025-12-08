#------ 911 CALLS PROJECT ------#

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline

df = pd.read_csv('911.csv')

#Find top 5 zipcodes for 911 calls:
  df['zip'].value_counts().head(5)

#Find top 5 townships for 911 calls:
  df['twp'].value_counts().head(5)

#Create new column for call reason:
  df['Reason'] = df['title'].apply(lambda x: x.split(':')[0])

#Find most common reason for a 911 call:
  df['Reason'].value_counts()
  sns.countplot(data = df, x = 'Reason', palette = 'Set2')

#Convert timeStamp column from str to DateTime objects:
  df['timeStamp'] = pd.to_datetime(df['timeStamp'])

#Create Hour, Month, and Day of Week columns for each 911 call:
  time = df['timeStamp'].iloc[0]
  time.hour
  df['Hour'] = df['timeStamp'].apply(lambda time: time.hour)
  df['Month'] = df['timeStamp'].apply(lambda time: time.month)
  df['Day of Week'] = df['timeStamp'].apply(lambda time: time.dayofweek)
  dmap = {0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'}
  df['Day of Week'] = df['Day of Week'].map(dmap)

#Create a countplot for Day of Week with Reason:
  sns.countplot(data = df, x = 'Day of Week', hue = 'Reason')
  plt.legend(loc='center left', bbox_to_anchor=(1, .5))

#Create a countplot for Month with Reason:
  sns.countplot(data = df, x = 'Month', hue = 'Reason', palette = 'Set1')
  plt.legend(loc='center left', bbox_to_anchor=(1, .5))

#Create a groupby object for the Month and aggregate the data to fill in missing months:
  byMonth = df.groupby('Month').count()
  byMonth.head()

#Create a plot showing calls per month:
  byMonth['lat'].plot()
  sns.lmplot(data = byMonth.reset_index(), x = 'Month', y = 'lat')

#Create a Date column from the TimeStamp column:
  df['Date'] = df['timeStamp'].apply(lambda t: t.date())

#Create a plot of 911 calls by Date and Reason:
  df[df['Reason'] == 'Traffic'].groupby('Date').count()['lat'].plot()
  plt.tight_layout()
  plt.title('Traffic')

  df[df['Reason'] == 'Fire'].groupby('Date').count()['lat'].plot()
  plt.tight_layout()
  plt.title('Fire')

  df[df['Reason'] == 'EMS'].groupby('Date').count()['lat'].plot()
  plt.tight_layout()
  plt.title('EMS')

#Create a heatmap of calls by Hour and Day of Week:
  dayHour = df.groupby(by = ['Day of Week','Hour']).count()['Reason'].unstack()
  plt.figure(figsize = (12,6))
  sns.heatmap(data = dayHour, cmap = 'viridis')

#Create a heatmap of calls by Month and Day of Week:
  dayMonth = df.groupby(by = ['Day of Week','Month']).count()['Reason'].unstack()
  plt.figure(figsize = (12,6))
  sns.heatmap(data = dayMonth, cmap = 'coolwarm')
