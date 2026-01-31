import requests
API_KEY = "56AWNVO2JP0F0QPF"
 
api_url="https://www.alphavantage.co/"

def get_stock_market_Data(symbol, is_timeseries):
    if is_timeseries:
        query = f"query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}"
    else:
        query = f"query?symbol={symbol}&apikey={API_KEY}"
    response = requests.get(url=api_url+query)
    for key, value in response.json().items():
        if key == "Time Series (Daily)":
            continue
        else:
            print(key, value)

symbol = input("Enter the symbol you want for the stock market api eg. (AMZN, GOGL)")
is_timeseries = True
get_stock_market_Data(symbol, is_timeseries)