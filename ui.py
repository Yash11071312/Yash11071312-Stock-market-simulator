import tkinter as tk
from tkinter import ttk, messagebox

from market import *
from portfolio import *
from charts import show_chart
root = tk.Tk()

root.title("SYS Stocks V2")
root.geometry("1200x700")
root.configure(bg="#1e1e1e")
market_frame = tk.Frame(root, bg="#2b2b2b")
market_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)

portfolio_frame = tk.Frame(root, bg="#2b2b2b")
portfolio_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

bottom_frame = tk.Frame(root, bg="#2b2b2b")
bottom_frame.pack(side="bottom", fill="x", padx=10, pady=10)
tk.Label(
    market_frame,
    text="Market",
    font=("Arial", 18, "bold"),
    bg="#2b2b2b",
    fg="white"
).pack()

tk.Label(
    portfolio_frame,
    text="Portfolio",
    font=("Arial", 18, "bold"),
    bg="#2b2b2b",
    fg="white"
).pack()

tk.Label(
    bottom_frame,
    text="Transactions",
    font=("Arial", 18, "bold"),
    bg="#2b2b2b",
    fg="white"
).pack()
def start_app():
    root.mainloop()