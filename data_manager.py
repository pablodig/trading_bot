# Data Management Module: data_manager.py

# This module will handle fetching historical data from yfinance and real-time data from the Alpaca API.
# It will also preprocess the data to make it suitable for the LSTM model.

import yfinance as yf
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import alpaca_trade_api as tradeapi
from config import API_KEY, SECRET_KEY, BASE_URL

# Initialize Alpaca API
api = tradeapi.REST(API_KEY, SECRET_KEY, base_url=BASE_URL, api_version='v2')

def get_historical_data(symbol, start_date, end_date):
    """
    Fetches historical stock data for the given symbol between start_date and end_date using yfinance.

    :param symbol: The stock symbol to fetch data for (e.g., 'AAPL').
    :param start_date: The start date for the data fetch.
    :param end_date: The end date for the data fetch.
    :return: A DataFrame with the historical stock data.
    """
    data = yf.download(symbol, start=start_date, end=end_date)
    return data

def get_real_time_data(symbol, start_date, end_date):
    """
    Fetches real-time stock data for the given symbol using the Alpaca API.

    :param symbol: The stock symbol to fetch data for (e.g., 'AAPL').
    :param start_date: The start date for the data fetch in 'YYYY-MM-DD' format.
    :param end_date: The end date for the data fetch in 'YYYY-MM-DD' format.
    :return: A DataFrame with the real-time stock data.
    """
    data = api.get_barset(symbol, 'day', start=start_date, end=end_date).df
    return data

def preprocess_data(data, feature_columns):
    """
    Preprocesses the data by selecting specific features and normalizing them.

    :param data: The DataFrame with stock data.
    :param feature_columns: The columns to be used as features.
    :return: The normalized data as a NumPy array, and the scaler object for inverse transformations.
    """
    scaler = MinMaxScaler()
    data_scaled = scaler.fit_transform(data[feature_columns])
    return data_scaled, scaler

# Example usage
# Uncomment the following lines to test the functionality after implementing the rest of the project components.

symbol = 'AAPL'
start_date = '2020-01-01'
end_date = '2020-12-31'
data = get_historical_data(symbol, start_date, end_date)
feature_columns = ['Open', 'High', 'Low', 'Close', 'Volume']
data_scaled, scaler = preprocess_data(data, feature_columns)
print(data_scaled)
