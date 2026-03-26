from pricer import black_scholes, delta, gamma, vega, theta
from visualizer import plot_price_vs_spot, plot_delta_vs_spot

def main():
    params = (100, 1, 0.2, 100, 0.05)
    print(f"Price: {black_scholes(*params):.4f}")
    print(f"Delta: {delta(*params):.4f}")
    print(f"Gamma: {gamma(*params):.4f}")
    print(f"Vega:  {vega(*params):.4f}")
    print(f"Theta: {theta(*params):.4f}")
    plot_price_vs_spot(100, 1, 0.2, 0.05)
    plot_delta_vs_spot(100, 1, 0.2, 0.05)

if __name__ == "__main__":
    main()
