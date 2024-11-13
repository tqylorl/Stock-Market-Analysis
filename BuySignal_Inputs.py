import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import time
from datetime import datetime

def convert_to_datetime(date_str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        raise ValueError(f"Invalid date format: {date_str}. Use 'YYYY-MM-DD' format.")

def fetch_stock_data(ticker, period='6mo', interval='1d'):
    print(f"Fetching stock data for {ticker}...")
    return yf.download(ticker, period=period, interval=interval)

def calculate_indicators(data):
    data['EMA_20'] = data['Close'].ewm(span=20, adjust=False).mean()
    data['EMA_50'] = data['Close'].ewm(span=50, adjust=False).mean()
    data['EMA_12'] = data['Close'].ewm(span=12, adjust=False).mean()
    data['EMA_26'] = data['Close'].ewm(span=26, adjust=False).mean()
    data['MACD'] = data['EMA_12'] - data['EMA_26']
    data['Signal_Line'] = data['MACD'].ewm(span=9, adjust=False).mean()

    delta = data['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
    RS = gain / loss
    data['RSI'] = 100 - (100 / (1 + RS))

    data['SMA_20'] = data['Close'].rolling(window=20).mean()
    data['StdDev'] = data['Close'].rolling(window=20).std()
    data['Upper_Band'] = data['SMA_20'] + (data['StdDev'] * 2)
    data['Lower_Band'] = data['SMA_20'] - (data['StdDev'] * 2)

    return data

def find_buy_signals(data):
    buy_signals = []
    for i in range(len(data)):
        if (data['EMA_20'].iloc[i] > data['EMA_50'].iloc[i]) and \
           (30 <= data['RSI'].iloc[i] <= 60) and \
           (data['MACD'].iloc[i] > data['Signal_Line'].iloc[i]) and \
           (data['Close'].iloc[i] <= data['Lower_Band'].iloc[i] * 1.05):
            buy_signals.append(i)
    return buy_signals

def find_sell_signals(data):
    sell_signals = []
    for i in range(len(data)):
        if (data['EMA_20'].iloc[i] < data['EMA_50'].iloc[i]) and \
                (data['RSI'].iloc[i] > 70 or data['RSI'].iloc[i] < 30) and \
                (data['MACD'].iloc[i] < data['Signal_Line'].iloc[i]) and \
                (data['Close'].iloc[i] <= data['Lower_Band'].iloc[i] * 1.05):

            if i > 2 and all(data['EMA_20'].iloc[i - j] < data['EMA_50'].iloc[i - j] for j in range(3)):
                sell_signals.append(i)

    return sell_signals

def plot_stock_data(data, ticker, buy_signals, sell_signals, zoom_start=None, zoom_end=None):
    plt.figure(figsize=(10, 5))
    plt.plot(data.index, data['Close'], label=f'{ticker} Close Price', color='blue')
    plt.plot(data.index, data['EMA_20'], label='EMA 20', color='red')
    plt.plot(data.index, data['EMA_50'], label='EMA 50', color='orange')
    plt.fill_between(data.index, data['Lower_Band'], data['Upper_Band'], color='gray', alpha=0.3, label='Bollinger Bands')

    for signal in buy_signals:
        plt.plot(data.index[signal], data['Close'].iloc[signal], marker='^', color='green', markersize=10, label='Buy Signal')

    for signal in sell_signals:
        plt.plot(data.index[signal], data['Close'].iloc[signal], marker='v', color='red', markersize=10, label='Sell Signal')

    plt.title(f'{ticker} Price with Buy and Sell Signals and Indicators')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)

    if zoom_start and zoom_end:
        plt.xlim(convert_to_datetime(zoom_start), convert_to_datetime(zoom_end))

    plt.show()

def analyze_stock(ticker, zoom_start=None, zoom_end=None):
    data = fetch_stock_data(ticker)
    data = calculate_indicators(data)

    buy_signals = find_buy_signals(data)
    sell_signals = find_sell_signals(data)

    print(f"Buy signals for {ticker} on dates: {data.index[buy_signals].tolist()}")
    print(f"Sell signals for {ticker} on dates: {data.index[sell_signals].tolist()}")

    plot_stock_data(data, ticker, buy_signals, sell_signals, zoom_start, zoom_end)
    return data, buy_signals, sell_signals

def get_tickers():
    tickers_input = input("Enter stock tickers (comma-separated, e.g., AAPL,GOOG,MSFT): ")
    return [ticker.strip().upper() for ticker in tickers_input.split(',')]

def get_interval():
    interval_input = input("Enter interval for fetching data (in seconds, e.g., 3600 for 1 hour): ")
    return int(interval_input)

def get_zoom_dates():
    zoom_option = input("Do you want to zoom into a specific date range? (yes/no): ").strip().lower()

    if zoom_option == 'yes':
        zoom_start = input("Enter the start date (YYYY-MM-DD): ")
        zoom_end = input("Enter the end date (YYYY-MM-DD): ")
        return zoom_start, zoom_end
    return None, None

def run_real_time_analysis(tickers, interval, zoom_start=None, zoom_end=None):
    try:
        while True:
            for ticker in tickers:
                analyze_stock(ticker, zoom_start, zoom_end)

            print(f"Waiting for {interval} seconds before the next analysis...")
            time.sleep(interval)

            stop_option = input("Do you want to stop the analysis? (yes/no): ").strip().lower()
            if stop_option == 'yes':
                print("Stopping the real-time analysis.")
                break
    except KeyboardInterrupt:
        print("Real-time stock analysis stopped.")

def main():
    tickers = get_tickers()
    interval = get_interval()
    zoom_start, zoom_end = get_zoom_dates()

    run_real_time_analysis(tickers, interval, zoom_start, zoom_end)

if __name__ == "__main__":
    main()