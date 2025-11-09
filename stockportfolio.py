# --- Stock Portfolio Tracker ---

# Step 1: Hardcoded dictionary for stock prices
stock_prices = {
    "AAPL": 180,    # Apple
    "TSLA": 250,    # Tesla
    "GOOGL": 140,   # Google
    "AMZN": 170,    # Amazon
    "MSFT": 320     # Microsoft
}

# Step 2: Take user input for stocks
portfolio = {}
print("Available Stocks:", ", ".join(stock_prices.keys()))
print("Enter 'done' when finished.\n")

while True:
    stock_name = input("Enter stock symbol: ").upper()
    if stock_name == "DONE":
        break
    elif stock_name not in stock_prices:
        print("❌ Stock not found! Try again.")
        continue
    
    quantity = int(input(f"Enter quantity for {stock_name}: "))
    portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity

# Step 3: Calculate total investment
print("\n📊 Your Portfolio Summary:")
total_value = 0
for stock, qty in portfolio.items():
    value = stock_prices[stock] * qty
    total_value += value
    print(f"{stock}: {qty} shares × ${stock_prices[stock]} = ${value}")

print(f"\n💰 Total Investment Value: ${total_value}")

# Step 4: Optional - Save to file
save_choice = input("\nDo you want to save this summary? (yes/no): ").lower()
if save_choice == "yes":
    with open("portfolio_summary.txt", "w") as file:
        file.write("Stock Portfolio Summary\n")
        file.write("========================\n")
        for stock, qty in portfolio.items():
            value = stock_prices[stock] * qty
            file.write(f"{stock}: {qty} shares × ${stock_prices[stock]} = ${value}\n")
        file.write(f"\nTotal Investment Value: ${total_value}\n")
    print("✅ Portfolio saved to 'portfolio_summary.txt'.")
