# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2700,
    "MSFT": 300,
    "AMZN": 3300
}

# To store the portfolio
portfolio = {}

print("📊 Welcome to the Stock Portfolio Tracker!")
print("Enter your stock holdings. Type 'done' when finished.\n")

# Take user input
while True:
    stock = input("Enter stock symbol (AAPL, TSLA, etc.): ").upper()
    if stock == 'DONE':
        break
    if stock not in stock_prices:
        print("❗ Stock not found in list. Try again.")
        continue
    try:
        quantity = int(input(f"Enter quantity of {stock}: "))
        portfolio[stock] = portfolio.get(stock, 0) + quantity
    except ValueError:
        print("❗ Please enter a valid number.")

# Calculate total investment
total_value = 0
print("\n📋 Your Portfolio:")
for stock, qty in portfolio.items():
    value = stock_prices[stock] * qty
    print(f"{stock}: {qty} shares × ${stock_prices[stock]} = ${value}")
    total_value += value

print(f"\n💰 Total Investment Value: ${total_value}")

# Optional: Save to file
save = input("\nDo you want to save the result to a file? (yes/no): ").lower()
if save == "yes":
    with open("portfolio_summary.txt", "w") as file:
        file.write("Stock Portfolio Summary\n")
        file.write("------------------------\n")
        for stock, qty in portfolio.items():
            value = stock_prices[stock] * qty
            file.write(f"{stock}: {qty} × ${stock_prices[stock]} = ${value}\n")
        file.write(f"\nTotal Investment: ${total_value}\n")
    print("✅ Portfolio saved to 'portfolio_summary.txt'")
