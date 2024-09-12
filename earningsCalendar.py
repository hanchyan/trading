import csv
import requests

# Replace with your own API key
ALPHA_VANTAGE_API_KEY = 'AZQE5T55E3RQTFG7'
HORIZON = '3month'  # Adjust the horizon if needed

# List of tickers (replace with your list of 500 tickers)
TICKERS = [
    'AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA', 'META', 'NVDA', 'BRK.B', 'UNH', 'V',
    'JPM', 'MA', 'HD', 'DIS', 'PYPL', 'NFLX', 'ADBE', 'CMCSA', 'INTC', 'CSCO',
    # Add more tickers as needed
]

def fetch_earnings_data(ticker, horizon):
    url = 'https://www.alphavantage.co/query?function=EARNINGS_CALENDAR&symbol={}&horizon={}&apikey={}'.format(ticker, horizon, ALPHA_VANTAGE_API_KEY)
    response = requests.get(url)
    content = response.content.decode('utf-8')
    return content

def process_earnings_data(content):
    # Process the CSV data
    csv_reader = csv.reader(content.splitlines(), delimiter=',')
    for row in csv_reader:
        print(row)

def main():
    for ticker in TICKERS:
        print('Fetching data for {}'.format(ticker))
        data = fetch_earnings_data(ticker, HORIZON)
        process_earnings_data(data)

if __name__ == '__main__':
    main()
