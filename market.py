import random
from datetime import datetime

# ---------------- STOCK DATABASE ---------------- #

stocks = {
    "AAPL": {
        "price": 150,
        "previous": 150,
        "high": 150,
        "low": 150,
        "history": [150]
    },
    "TSLA": {
        "price": 220,
        "previous": 220,
        "high": 220,
        "low": 220,
        "history": [220]
    },
    "GOOG": {
        "price": 180,
        "previous": 180,
        "high": 180,
        "low": 180,
        "history": [180]
    },
    "AMZN": {
        "price": 170,
        "previous": 170,
        "high": 170,
        "low": 170,
        "history": [170]
    },
    "MSFT": {
        "price": 200,
        "previous": 200,
        "high": 200,
        "low": 200,
        "history": [200]
    }
}


# ---------------- MARKET STATUS ---------------- #

def market_status():

    hour = datetime.now().hour

    if 9 <= hour < 16:
        return "🟢 Market Open"

    return "🔴 Market Closed"


# ---------------- UPDATE STOCKS ---------------- #

def update_market():

    for stock in stocks.values():

        stock["previous"] = stock["price"]

        # Price changes between -2% and +2%

        percent = random.uniform(-0.02, 0.02)

        new_price = stock["price"] * (1 + percent)

        stock["price"] = round(max(10, new_price), 2)

        if stock["price"] > stock["high"]:
            stock["high"] = stock["price"]

        if stock["price"] < stock["low"]:
            stock["low"] = stock["price"]

        stock["history"].append(stock["price"])

        # Keep last 100 prices

        if len(stock["history"]) > 100:
            stock["history"].pop(0)


# ---------------- STOCK INFO ---------------- #

def get_price(symbol):

    symbol = symbol.upper()

    if symbol in stocks:
        return stocks[symbol]["price"]

    return None


def get_history(symbol):

    return stocks[symbol]["history"]


def get_stock(symbol):

    return stocks[symbol]


# ---------------- GAIN / LOSS ---------------- #

def get_change(symbol):

    stock = stocks[symbol]

    return round(stock["price"] - stock["previous"], 2)


def get_change_percent(symbol):

    stock = stocks[symbol]

    if stock["previous"] == 0:
        return 0

    return round(
        ((stock["price"] - stock["previous"]) /
         stock["previous"]) * 100,
        2
    )


# ---------------- TOP GAINER ---------------- #

def top_gainer():

    best = None
    value = -999

    for symbol in stocks:

        change = get_change_percent(symbol)

        if change > value:
            value = change
            best = symbol

    return best, value


# ---------------- TOP LOSER ---------------- #

def top_loser():

    worst = None
    value = 999

    for symbol in stocks:

        change = get_change_percent(symbol)

        if change < value:
            value = change
            worst = symbol

    return worst, value


# ---------------- ALL STOCKS ---------------- #

def get_all_stocks():

    return stocks