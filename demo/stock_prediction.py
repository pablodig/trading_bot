import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense, LSTM

def get_stock_data(ticker, start_date, end_date):
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    return stock_data

ticker = 'YHOO'
start_date = '2010-01-01'
end_date = '2021-09-01'
stock_data = get_stock_data(ticker, start_date, end_date)

def preprocess_data(data, feature_cols, target_col):
    data = data[feature_cols]
    target = data[target_col]
    scaler = MinMaxScaler()
    data = scaler.fit_transform(data)
    return data, target, scaler

feature_columns = ['Open', 'High', 'Low', 'Close', 'Volume']
target_column = 'Close'
data, target, scaler = preprocess_data(stock_data, feature_columns, 
target_column)

train_data, test_data, train_target, test_target = train_test_split(data, target, 
test_size=0.2, shuffle=False)


def create_model(input_shape):
    model = Sequential()
    model.add(LSTM(units=50, return_sequences=True, input_shape=input_shape))
    model.add(LSTM(units=50, return_sequences=False))
    model.add(Dense(units=25))
    model.add(Dense(units=1))
    model.compile(optimizer='adam', loss='mean_squared_error')
    return model

input_shape = (train_data.shape[1], 1)
model = create_model(input_shape)

train_data = np.reshape(train_data, (train_data.shape[0], train_data.shape[1], 
1))
model.fit(train_data, train_target, batch_size=64, epochs=100)

test_data = np.reshape(test_data, (test_data.shape[0], test_data.shape[1], 1))
predicted_prices = model.predict(test_data)
predicted_prices = scaler.inverse_transform(predicted_prices)

