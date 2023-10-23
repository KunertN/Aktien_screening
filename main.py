import yfinance as yf
import matplotlib.pyplot as plt

def compare_stocks(stock1, stock2):
    stock_data1 = yf.download(stock1, start="2020-01-01", end="2023-01-01")
    stock_data2 = yf.download(stock2, start="2020-01-01", end="2023-01-01")

    return stock_data1, stock_data2

def plot_stock_comparison(stock1, stock2):
    stock_data1, stock_data2 = compare_stocks(stock1, stock2)

    plt.figure(figsize=(12, 6))
    plt.plot(stock_data1['Close'], label=stock1)
    plt.plot(stock_data2['Close'], label=stock2)
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.title(f"{stock1} vs. {stock2} Stock Price Comparison")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    stock1 = "DBK.DE"  
    stock2 = "ING"  

    plot_stock_comparison(stock1, stock2)