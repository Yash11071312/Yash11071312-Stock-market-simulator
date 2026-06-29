import matplotlib.pyplot as plt
from market import get_history


def show_chart(symbol):

    history = get_history(symbol)

    plt.figure(figsize=(6, 4))

    plt.plot(history, marker="o")

    plt.title(symbol + " Price History")

    plt.xlabel("Updates")

    plt.ylabel("Price")

    plt.grid(True)

    plt.show()