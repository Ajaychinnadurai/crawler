import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf

# Load the stock data (Replace 'tcs_stock_data.csv' with your CSV file)
df = pd.read_csv("tcs_stock_data.csv", parse_dates=["Date"], index_col="Date")

# Show the first few rows
print(df.head())

# Plot the stock price trend
plt.figure(figsize=(12, 5))
plt.plot(df["Close"], label="Closing Price", color="blue")
plt.title("TCS Stock Price Trend")
plt.xlabel("Date")
plt.ylabel("Stock Price (INR)")
plt.legend()
plt.grid()
plt.show()

# Calculate Moving Averages (e.g., 7-day and 30-day)
df["7-Day MA"] = df["Close"].rolling(window=7).mean()
df["30-Day MA"] = df["Close"].rolling(window=30).mean()

# Plot Moving Averages
plt.figure(figsize=(12, 5))
plt.plot(df["Close"], label="Closing Price", color="blue")
plt.plot(df["7-Day MA"], label="7-Day Moving Avg", linestyle="dashed", color="red")
plt.plot(df["30-Day MA"], label="30-Day Moving Avg", linestyle="dashed", color="green")
plt.title("TCS Stock Moving Averages")
plt.xlabel("Date")
plt.ylabel("Stock Price (INR)")
plt.legend()
plt.grid()
plt.show()

# Calculate and plot daily returns (Volatility)
df["Daily Return"] = df["Close"].pct_change()

plt.figure(figsize=(12, 5))
sns.histplot(df["Daily Return"].dropna(), bins=50, kde=True, color="purple")
plt.title("TCS Daily Returns Distribution")
plt.xlabel("Daily Return (%)")
plt.ylabel("Frequency")
plt.show()

# Print statistical summary
print("\nStock Data Statistics:")
print(df.describe())
