from datetime import datetime
from market import get_price
from storage import (
    save_portfolio,
    save_transactions,load_portfolio, load_transactions
)
# ---------------- USER DATA ---------------- #


saved = load_portfolio()

balance = saved["balance"]
portfolio = saved["portfolio"]

transactions = load_transactions()


# ---------------- BUY ---------------- #

def buy_stock(symbol, qty):

    global balance

    symbol = symbol.upper()

    if qty <= 0:
        return False, "Quantity must be greater than 0."

    price = get_price(symbol)

    if price is None:
        return False, "Invalid Stock."

    total_cost = price * qty

    if balance < total_cost:
        return False, "Insufficient Balance."

    if symbol not in portfolio:

        portfolio[symbol] = {
            "qty": qty,
            "avg_price": price
        }

    else:

        old_qty = portfolio[symbol]["qty"]
        old_avg = portfolio[symbol]["avg_price"]

        new_qty = old_qty + qty

        new_avg = (
            (old_qty * old_avg) +
            (qty * price)
        ) / new_qty

        portfolio[symbol]["qty"] = new_qty
        portfolio[symbol]["avg_price"] = round(new_avg, 2)

    balance -= total_cost

    transactions.append({
        "time": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
        "type": "BUY",
        "stock": symbol,
        "qty": qty,
        "price": price
        
    })
    save_portfolio(balance, portfolio)
    save_transactions(transactions)

    return True, "Stock Purchased Successfully."


# ---------------- SELL ---------------- #

def sell_stock(symbol, qty):

    global balance

    symbol = symbol.upper()

    if qty <= 0:
        return False, "Quantity must be greater than 0."

    if symbol not in portfolio:
        return False, "You don't own this stock."

    if portfolio[symbol]["qty"] < qty:
        return False, "Not enough shares."

    price = get_price(symbol)

    balance += price * qty

    portfolio[symbol]["qty"] -= qty

    transactions.append({
        "time": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
        "type": "SELL",
        "stock": symbol,
        "qty": qty,
        "price": price
    })
    if portfolio[symbol]["qty"] == 0:
        del portfolio[symbol]
    save_portfolio(balance, portfolio)
    save_transactions(transactions)

    return True, "Stock Sold Successfully."


# ---------------- PROFIT ---------------- #

def stock_profit(symbol):

    if symbol not in portfolio:
        return 0

    qty = portfolio[symbol]["qty"]

    avg = portfolio[symbol]["avg_price"]

    current = get_price(symbol)

    return round((current - avg) * qty, 2)


def total_profit():

    total = 0

    for stock in portfolio:
        total += stock_profit(stock)

    return round(total, 2)


# ---------------- VALUE ---------------- #

def portfolio_value():

    total = 0

    for stock in portfolio:

        qty = portfolio[stock]["qty"]

        total += qty * get_price(stock)

    return round(total, 2)


def net_worth():

    return round(balance + portfolio_value(), 2)


# ---------------- GETTERS ---------------- #

def get_balance():
    return round(balance, 2)


def get_portfolio():
    return portfolio


def get_transactions():
    return transactions