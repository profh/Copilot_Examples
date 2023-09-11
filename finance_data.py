# Use Alpha Vantage API to get stock data and plot it in a graph
import requests
import pandas as pd
import matplotlib.pyplot as plt

API_KEY = "YOUR_API_KEY_GOES_HERE"
STOCK_SYMBOL = "MSFT"

def get_stock_data(symbol):
  # get daily stock data from Alpha Vantage
  
  url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}"
  response = requests.get(url)
  data = response.json()
  return data

def main():
  data = get_stock_data(STOCK_SYMBOL)
  
  # Turn the data into a Pandas DataFrame
  df = pd.DataFrame(data["Time Series (Daily)"]).T
  df.index = pd.to_datetime(df.index)
  df = df.astype(float)
  
  # Print the dataframe
  print(df)
  
  # Plot the data in a graph
  plt.plot(df.index, df["4. close"])
  plt.show()
  pass

if __name__ == "__main__":
  main()
  
