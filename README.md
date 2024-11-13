# 🎉 Stock Market Analysis Tool 📈

> **Analyze stock trends and identify buy signals using Exponential Moving Averages (EMAs) – perfect for investors and data enthusiasts!**

This Python-based tool provides a robust way to analyze stock price trends, identify buy signals, and visualize key trends to support data-driven investment strategies. With easy-to-understand charts and Excel output, this tool simplifies technical analysis.

---

## 🌟 Features

- **📊 Automated Data Collection**: Fetch historical stock price data directly from Yahoo Finance.
- **📈 Indicator Calculations**: Calculate **20-day** and **50-day** EMAs to observe short-term and long-term price trends.
- **🚀 Buy Signal Detection**: Identify buy signals based on EMA crossovers (20-day EMA crossing above 50-day EMA).
- **📑 Exportable Results**:
  - **Excel Output**: Neatly formatted table including Date, Close Price, EMAs, and Buy Signals.
  - **Graph Visualization**: Plot with Close Price, EMAs, and Buy Signal markers for clear trend analysis.

---

## ⚙️ Requirements

<div style="position: relative;">
<pre><code id="requirements">pip install yfinance pandas matplotlib</code></pre>
<button onclick="copyToClipboard('requirements')" style="position: absolute; top: 0; right: 0; padding: 5px; background-color: #007bff; color: white; border: none; border-radius: 3px; cursor: pointer;">Copy</button>
</div>

---

## 🚀 How to Use

### 1. Clone the Repository
<div style="position: relative;">
<pre><code id="clone">git clone https://github.com/yourusername/stock-market-analysis-tool.git
cd stock-market-analysis-tool</code></pre>
<button onclick="copyToClipboard('clone')" style="position: absolute; top: 0; right: 0; padding: 5px; background-color: #007bff; color: white; border: none; border-radius: 3px; cursor: pointer;">Copy</button>
</div>

### 2. Run the Tool
<div style="position: relative;">
<pre><code id="run">python BuySignal.py</code></pre>
<button onclick="copyToClipboard('run')" style="position: absolute; top: 0; right: 0; padding: 5px; background-color: #007bff; color: white; border: none; border-radius: 3px; cursor: pointer;">Copy</button>
</div>

### 3. View the Output
- **Excel File**: Saved in the project directory with stock data and buy signals.
- **Graph**: Displays the stock trend and buy signals for easy visual analysis.

---

## 📄 Example Output

### Excel Table

An Excel file (`Stock_Analysis_Data.xlsx`) is generated with columns:
- **Date**: The date of each data point.
- **Close Price (USD)**: Closing price of the stock.
- **20-Day EMA**: Short-term Exponential Moving Average.
- **50-Day EMA**: Long-term Exponential Moving Average.
- **Signal**: Buy Signal when the 20-day EMA crosses above the 50-day EMA.

### Graph Visualization

The tool also generates a graph displaying:
- **Close Price** (in blue)
- **20-Day EMA** (in red)
- **50-Day EMA** (in orange)
- **Buy Signals**: Marked by green upward triangles at the crossover points.

---

## 🔧 Example Code

<div style="position: relative;">
<pre><code id="exampleCode">import yfinance as yf
import pandas as pd

# Calculate EMAs for given data
def calculate_emas(data):
    data['EMA_20'] = data['Close'].ewm(span=20, adjust=False).mean()
    data['EMA_50'] = data['Close'].ewm(span=50, adjust=False).mean()
    return data

# Fetch stock data and apply the buy signal detection
ticker = 'NVDA'
data = yf.download(ticker, start='2022-12-31', end='2023-08-20')
data = calculate_emas(data)
</code></pre>
<button onclick="copyToClipboard('exampleCode')" style="position: absolute; top: 0; right: 0; padding: 5px; background-color: #007bff; color: white; border: none; border-radius: 3px; cursor: pointer;">Copy</button>
</div>

---

## 🤝 Contributing

We welcome contributions! Feel free to open an issue or submit a pull request for any enhancements, bug fixes, or additional features.

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 📬 Contact

If you have any questions, suggestions, or feedback, feel free to reach out at [your-email@example.com](mailto:your-email@example.com).

---

## 🙌 Acknowledgments

- **Yahoo Finance** for the stock data via the `yfinance` library.
- **Matplotlib** and **Pandas** for data visualization and manipulation.

---

### 🎉 Enjoy exploring stock trends and making informed investment decisions! 🚀📊

---

