import yfinance as yf
import pandas as pd
import tkinter as tk
from tkinter import messagebox


portfolio = {}


def get_stock_data(symbol):
    stock = yf.Ticker(symbol)
    stock_info = stock.history(period="1d")
    if not stock_info.empty:
        return stock_info['Close'][0]
    else:
        return None


def add_stock():
    symbol = symbol_entry.get().upper()
    shares = shares_entry.get()

    if not symbol or not shares.isdigit():
        messagebox.showerror("Input Error", "Please enter a valid symbol and number of shares.")
        return

    stock_price = get_stock_data(symbol)
    if stock_price is not None:
        portfolio[symbol] = {'shares': int(shares), 'price': stock_price}
        messagebox.showinfo("Success", f"Added {shares} shares of {symbol} at ${stock_price:.2f} per share.")
    else:
        messagebox.showerror("Error", f"Could not retrieve data for {symbol}.")
    clear_entries()


def remove_stock():
    symbol = symbol_entry.get().upper()

    if symbol in portfolio:
        del portfolio[symbol]
        messagebox.showinfo("Success", f"Removed {symbol} from portfolio.")
    else:
        messagebox.showerror("Error", f"{symbol} not found in portfolio.")
    clear_entries()


def track_portfolio():
    total_value = 0
    portfolio_data = []
    portfolio_text.delete('1.0', tk.END)  # Clear the text area
    portfolio_text.insert(tk.END, f"{'Stock':<10}{'Shares':<10}{'Price':<10}{'Value':<10}\n")
    portfolio_text.insert(tk.END, "=" * 40 + "\n")
    
    for symbol, data in portfolio.items():
        shares = data['shares']
        stock_price = get_stock_data(symbol)
        if stock_price is not None:
            stock_value = shares * stock_price
            total_value += stock_value
            portfolio_data.append([symbol, shares, stock_price, stock_value])
            portfolio_text.insert(tk.END, f"{symbol:<10}{shares:<10}{stock_price:<10.2f}{stock_value:<10.2f}\n")
        else:
            portfolio_text.insert(tk.END, f"Error: Could not retrieve data for {symbol}.\n")
    
    portfolio_text.insert(tk.END, "=" * 40 + "\n")
    portfolio_text.insert(tk.END, f"Total Portfolio Value: ${total_value:.2f}\n")

def clear_entries():
    symbol_entry.delete(0, tk.END)
    shares_entry.delete(0, tk.END)


root = tk.Tk()
root.title("Stock Portfolio Tracker")


tk.Label(root, text="Stock Symbol:").grid(row=0, column=0, padx=10, pady=10)
symbol_entry = tk.Entry(root)
symbol_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Number of Shares:").grid(row=1, column=0, padx=10, pady=10)
shares_entry = tk.Entry(root)
shares_entry.grid(row=1, column=1, padx=10, pady=10)

add_button = tk.Button(root, text="Add Stock", command=add_stock)
add_button.grid(row=2, column=0, padx=10, pady=10)

remove_button = tk.Button(root, text="Remove Stock", command=remove_stock)
remove_button.grid(row=2, column=1, padx=10, pady=10)

track_button = tk.Button(root, text="Track Portfolio", command=track_portfolio)
track_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

portfolio_text = tk.Text(root, width=50, height=10)
portfolio_text.grid(row=4, column=0, columnspan=2, padx=10, pady=10)


root.mainloop()
