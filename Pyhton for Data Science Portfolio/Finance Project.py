#------ FINANCE PROJECT ------#

from pandas_datareader import data, wb
import yfinance as yf
import pandas as pd
import numpy as np
import seaborn as sns
import datetime
import matplotlib.pyplot as plt
import plotly
import cufflinks as cf
cf.go_offline()

all_banks = pd.read_pickle('all_banks.pkl')

start = datetime.datetime(2006,1,1)
end = datetime.datetime(2016,1,1)

#Create dataframes for the banks
  BAC = yf.download('BAC', start, end) #Bank of America
  C = yf.download('C', start, end) #CitiGroup
  GS = yf.download('GS', start, end) # Goldman Sachs
  JPM = yf.download('JPM', start, end) #JPMorgan Chase
  MS = yf.download('MS', start, end) # Morgan Stanley
  WFC = yf.download('WFC', start, end) #Wells Fargo

#Concatenate dataframes into a single dataframe
  tickers = ['BAC', 'C', 'GS', 'JPM', 'MS', 'WFC']
  bank_stocks = pd.concat([BAC, C, GS, JPM, MS, WFC], axis = 1, keys = tickers)

#Find max close price for each bank's stock:
  all_banks.xs(key = 'Close', axis = 1, level = 'Stock Info').max()

#Add a column of return values for each bank stock at close:
  returns = pd.DataFrame()
  for tick in tickers:
    returns[tick+' Return'] = all_banks[tick]['Close'].pct_change()

#Create a plot showing close price for each bank over time
  for tick in tickers:
    all_banks[tick]['Close'].plot(figsize=(12,4),label=tick)
  plt.legend()

#Create a plot of the rolling 30 day average against the Close Price for Bank Of America's stock for the year 2008
  plt.figure(figsize=(12,6))
  BAC['Close'].loc['2008-01-01':'2009-01-01'].rolling(window=30).mean().plot(label = '30 Day Avg')
  BAC['Close'].loc['2008-01-01':'2009-01-01'].plot(label = 'BAC CLOSE')
  plt.legend()

#Create a candle plot of Bank of America's stock from Jan 1st 2015 to Jan 1st 2016
  close_corr = all_banks.xs(key='Close',axis=1,level='Stock Info').corr()
  close_corr.plot(kind='kde')
