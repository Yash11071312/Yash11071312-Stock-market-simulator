import json
import os

# ---------------- FILE PATHS ---------------- #

DATA_FOLDER = "data"

PORTFOLIO_FILE = os.path.join(DATA_FOLDER, "portfolio.json")
TRANSACTION_FILE = os.path.join(DATA_FOLDER, "transactions.json")


# ---------------- CREATE DATA FOLDER ---------------- #

if not os.path.exists(DATA_FOLDER):
    os.makedirs(DATA_FOLDER)


# ---------------- SAVE PORTFOLIO ---------------- #

def save_portfolio(balance, portfolio):

    data = {
        "balance": balance,
        "portfolio": portfolio
    }

    with open(PORTFOLIO_FILE, "w") as file:
        json.dump(data, file, indent=4)


# ---------------- LOAD PORTFOLIO ---------------- #

def load_portfolio():

    if not os.path.exists(PORTFOLIO_FILE):

        return {
            "balance": 10000,
            "portfolio": {}
        }

    with open(PORTFOLIO_FILE, "r") as file:

        return json.load(file)


# ---------------- SAVE TRANSACTIONS ---------------- #

def save_transactions(transactions):

    with open(TRANSACTION_FILE, "w") as file:

        json.dump(transactions, file, indent=4)


# ---------------- LOAD TRANSACTIONS ---------------- #

def load_transactions():

    if not os.path.exists(TRANSACTION_FILE):
        return []

    with open(TRANSACTION_FILE, "r") as file:

        return json.load(file)


# ---------------- RESET DATA ---------------- #

def reset_data():

    save_portfolio(10000, {})

    save_transactions([])