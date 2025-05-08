  
import sys
print("Using Python from:", sys.executable)


import requests

def fetch_latest_stock_price(api_key, ticker_symbol):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticker_symbol}&apikey={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        # Check for API error
        if "Time Series (Daily)" not in data:
            print("API response error:", data)
            return

        time_series = data["Time Series (Daily)"]
        latest_date = max(time_series.keys())
        latest_prices = time_series[latest_date]

        print(f"Latest Date: {latest_date}")
        print(f"Open: {latest_prices['1. open']}")
        print(f"High: {latest_prices['2. high']}")
        print(f"Low: {latest_prices['3. low']}")
        print(f"Close: {latest_prices['4. close']}")
        print(f"Volume: {latest_prices['5. volume']}")
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")

def main():
    api_key = "UWMZT4Y4IJ1J248F"
    ticker_symbol = input("Enter ticker symbol (e.g., AAPL): ")
    fetch_latest_stock_price(api_key, ticker_symbol)

main()
