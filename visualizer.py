import matplotlib.pyplot as plt
import numpy as np
from pricer import black_scholes, delta

def plot_price_vs_spot(strike_price, expiration, sigma, treasury_rate):
    x1 = np.linspace(50, 150, 100)
    bs = black_scholes(strike_price, expiration, sigma, x1, treasury_rate, call=True)
    plt.plot(x1,bs)
    plt.xlabel("Spot Price")
    plt.ylabel("Option Price")
    plt.show()

def plot_delta_vs_spot(strike_price, expiration, sigma, treasury_rate):
    x1 = np.linspace(50, 150, 100)
    delta_values = delta(strike_price, expiration, sigma, x1, treasury_rate, call=True)
    plt.plot(x1,delta_values)
    plt.xlabel("Spot Price")
    plt.ylabel("Delta")
    plt.show()
