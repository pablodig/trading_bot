import alpaca_trade_api as tradeapi
import pandas as pd

API_KEY = "PKV1ETWSU6FG7PXYKZ8H"
SECRET_KEY = "gdjTwF8I0yczlnkNDtjQysahlLkgrDIShNoeiIr9"
BASE_URL = "https://paper-api.alpaca.markets"  # Use this URL for paper trading

api = tradeapi.REST(API_KEY, SECRET_KEY, base_url=BASE_URL, api_version='v2')

def get_stock_data(symbol, start_date, end_date):
    timeframe = '1D'
    data = api.get_bars(
        symbol,
        tradeapi.rest.TimeFrame.Day,
        start=pd.Timestamp(start_date, tz='America/New_York').isoformat(),
        end=pd.Timestamp(end_date, tz='America/New_York').isoformat(),
        adjustment='raw'
    ).df
    return data


symbol = 'AAPL'
start_date = '2021-01-01'
end_date = '2021-01-31'

stock_data = get_stock_data(symbol, start_date, end_date)
print(stock_data)