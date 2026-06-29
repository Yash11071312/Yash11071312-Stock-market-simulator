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

market_table = ttk.Treeview(
    market_frame,
    columns=("Stock", "Price", "Change", "%", "High", "Low"),
    show="headings",
    height=15
)

market_table.heading("Stock", text="Stock")
market_table.heading("Price", text="Price")
market_table.heading("Change", text="Change")
market_table.heading("%", text="%")
market_table.heading("High", text="High")
market_table.heading("Low", text="Low")

market_table.column("Stock", width=80, anchor="center")
market_table.column("Price", width=80, anchor="center")
market_table.column("Change", width=80, anchor="center")
market_table.column("%", width=80, anchor="center")
market_table.column("High", width=80, anchor="center")
market_table.column("Low", width=80, anchor="center")

market_table.pack(fill="both", expand=True, padx=10, pady=10)

market_table.tag_configure(
    "green",
    foreground="#00cc66"
)

market_table.tag_configure(
    "red",
    foreground="#ff4444"
)

market_table.tag_configure(
    "white",
    foreground="black"
)
market_table.tag_configure("green", foreground="green")
market_table.tag_configure("red", foreground="red")
market_table.tag_configure("white", foreground="black")
def refresh_market():

    update_market()

    market_table.delete(*market_table.get_children())

    for symbol, stock in get_all_stocks().items():

        change = get_change(symbol)
        percent = get_change_percent(symbol)

        if change > 0:
            tag = "green"
            change_text = f"+{change}"
            percent_text = f"+{percent}%"

        elif change < 0:
            tag = "red"
            change_text = str(change)
            percent_text = f"{percent}%"

        else:
            tag = "white"
            change_text = "0"
            percent_text = "0%"

        market_table.insert(
            "",
            "end",
            values=(
                symbol,
                stock["price"],
                change_text,
                percent_text,
                stock["high"],
                stock["low"]
            ),
            tags=(tag,)
        )

    root.after(3000, refresh_market)
def start_app():
    refresh_market()
    root.mainloop()