import tkinter as tk
from tkinter import ttk, messagebox

from market import *
from portfolio import *
from charts import show_chart

root = tk.Tk()

root.title("SYS Stocks V2")
root.geometry("1200x700")
root.configure(bg="#1e1e1e")

# ================= MAIN FRAME =================

main_frame = tk.Frame(root, bg="#1e1e1e")
main_frame.pack(fill="both", expand=True)

# ================= TOP AREA =================

top_frame = tk.Frame(main_frame, bg="#1e1e1e")
top_frame.pack(fill="both", expand=True)

market_frame = tk.Frame(
    top_frame,
    bg="#2b2b2b",
    bd=2,
    relief="ridge"
)

market_frame.pack(
    side="left",
    fill="both",
    expand=True,
    padx=10,
    pady=10
)

portfolio_frame = tk.Frame(
    top_frame,
    bg="#2b2b2b",
    bd=2,
    relief="ridge"
)

portfolio_frame.pack(
    side="right",
    fill="both",
    expand=True,
    padx=10,
    pady=10
)

# ================= BOTTOM =================

transaction_frame = tk.Frame(
    main_frame,
    bg="#2b2b2b",
    bd=2,
    relief="ridge",
    height=200
)

transaction_frame.pack(
    fill="x",
    padx=10,
    pady=10
)

# ================= TITLES =================

tk.Label(
    market_frame,
    text="📈 Market",
    bg="#2b2b2b",
    fg="white",
    font=("Arial", 18, "bold")
).pack(pady=10)

tk.Label(
    portfolio_frame,
    text="💼 Portfolio",
    bg="#2b2b2b",
    fg="white",
    font=("Arial", 18, "bold")
).pack(pady=10)

tk.Label(
    transaction_frame,
    text="📜 Transactions",
    bg="#2b2b2b",
    fg="white",
    font=("Arial", 18, "bold")
).pack(pady=10)


def start_app():
    root.mainloop()