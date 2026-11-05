import csv

def run_stock_tracker():
    # 1. Hardcoded dictionary of stock prices (in USD)
    stock_prices = {
        "AAPL": 180.00,
        "TSLA": 250.00,
        "GOOGLE": 140.00,
        "MSFT": 420.00,
        "AMZN": 175.00
    }

    portfolio = {}

    print("=== Simple Stock Portfolio Tracker ===")
    print("Available Stocks & Prices:")
    for ticker, price in stock_prices.items():
        print(f"  {ticker}: ${price:.2f}")
    print("\nType 'done' when finished entering your stocks.\n")

    # 2. User input loop for stock names and quantities
    while True:
        ticker = input("Enter stock symbol (or 'done' to finish): ").strip().upper()
        
        if ticker == 'DONE':
            break
            
        if ticker not in stock_prices:
            print(f"Error: '{ticker}' is not in the price list. Choose from {list(stock_prices.keys())}.")
            continue

        try:
            quantity = int(input(f"Enter quantity of {ticker} shares: ").strip())
            if quantity <= 0:
                print("Error: Quantity must be a positive whole number.")
                continue
        except ValueError:
            print("Error: Invalid input. Please enter a whole number for quantity.")
            continue

        # Accumulate shares if the user enters the same stock multiple times
        portfolio[ticker] = portfolio.get(ticker, 0) + quantity
        print(f"Added {quantity} shares of {ticker}.\n")

    if not portfolio:
        print("\nNo stocks entered. Exiting program.")
        return

    # 3. Calculate and display total investment value
    print("\n" + "=" * 45)
    print(f"{'Stock':<10} {'Shares':<10} {'Price':<12} {'Subtotal':<12}")
    print("-" * 45)

    total_investment = 0.0
    summary_rows = []

    for ticker, qty in portfolio.items():
        price = stock_prices[ticker]
        subtotal = qty * price
        total_investment += subtotal
        summary_rows.append([ticker, qty, price, subtotal])
        print(f"{ticker:<10} {qty:<10} ${price:<11.2f} ${subtotal:<11.2f}")

    print("-" * 45)
    print(f"{'Total Investment Value:':<32} ${total_investment:.2f}")
    print("=" * 45)

    # 4. Optional file saving (.txt or .csv)
    save_choice = input("\nSave portfolio summary? Enter 'txt', 'csv', or 'no': ").strip().lower()

    if save_choice == 'txt':
        filename = "portfolio_summary.txt"
        with open(filename, "w") as file:
            file.write("=== Stock Portfolio Summary ===\n")
            file.write(f"{'Stock':<10} {'Shares':<10} {'Price':<12} {'Subtotal':<12}\n")
            file.write("-" * 45 + "\n")
            for row in summary_rows:
                file.write(f"{row[0]:<10} {row[1]:<10} ${row[2]:<11.2f} ${row[3]:<11.2f}\n")
            file.write("-" * 45 + "\n")
            file.write(f"Total Investment Value: ${total_investment:.2f}\n")
        print(f"Portfolio saved to {filename}")

    elif save_choice == 'csv':
        filename = "portfolio_summary.csv"
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Stock", "Shares", "Price ($)", "Subtotal ($)"])
            writer.writerows(summary_rows)
            writer.writerow([])
            writer.writerow(["Total Investment", "", "", total_investment])
        print(f"Portfolio saved to {filename}")

    else:
        print("Portfolio was not saved.")

if __name__ == "__main__":
    run_stock_tracker()