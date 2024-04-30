import requests
import pandas as pd

def get_market_data():
    crypto_response = requests.get("CRYPTO_API_URL")
    stock_response = requests.get("STOCK_API_URL")
    crypto_data = crypto_response.json()
    stock_data = stock_response.json()
    return pd.DataFrame(crypto_data + stock_data)

def filter_data(data, filter_type):
    if filter_type == 'rising':
        return data[data['change_percent'] > 0].sort_values(by='change_percent', ascending=False)
    elif filter_type == 'declining':
        return data[data['change_percent'] < 0].sort_values(by='change_percent')
    elif filter_type == 'cheapest':
        return data.sort_values(by='last_price')[:10]
    elif filter_type == 'most_expensive':
        return data.sort_values(by='last_price', ascending=False)[:10]
