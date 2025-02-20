import yfinance as yf

# Define stock ticker (Example: TCS for Tata Consultancy Services)
stock = yf.Ticker("TCS.NS")  # Use "TCS.NS" for NSE India stocks

# Get the latest stock price and details
stock_info = stock.history(period="1d")

# Extract relevant details
current_price = stock_info['Close'].iloc[-1]
open_price = stock_info['Open'].iloc[-1]
high_price = stock_info['High'].iloc[-1]
low_price = stock_info['Low'].iloc[-1]

print(f"TCS Stock Data:")
print(f"Current Price: {current_price}")
print(f"Open Price: {open_price}")
print(f"High Price: {high_price}")
print(f"Low Price: {low_price}")

# Save to CSV
stock_info.to_csv("tcs_stock_data.csv")
print("Stock data saved to tcs_stock_data.csv")
