# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Setting pandas display options for large data
pd.options.display.max_rows = 200
pd.options.display.max_columns = 150

# Read file and preliminary exploration
stocks = pd.read_table("sphist.csv", delimiter=",")
stocks.info()
stocks.head()

# Conver Date column to datetime format and sort_values in ascending order
stocks['Date'] = pd.to_datetime(stocks['Date'])
stocks = stocks.sort_values(by = 'Date', ascending = True, ignore_index = True)

# Generate indicators and confirm 
stocks['5_days_avg'] = stocks['Close'].rolling(window = 5).mean().shift(periods=1)
stocks['30_days_avg'] = stocks['Close'].rolling(window = 30).mean().shift(periods=1)
stocks['365_days_avg'] = stocks['Close'].rolling(window = 365).mean().shift(periods=1)
stocks['5_days_sd'] = stocks['Close'].rolling(window = 5).std().shift(periods=1)
stocks['30_days_sd'] = stocks['Close'].rolling(window = 30).std().shift(periods=1)
stocks['365_days_sd'] = stocks['Close'].rolling(window = 365).std().shift(periods=1)
stocks = stocks.copy() # to avoid copyset warning

print(stocks.head(6))
print(stocks.loc[28:33])
print(stocks.loc[360:368])
