# Options Calculator

Black-Scholes option pricing model with Greeks calculator and visualizations.

## What it does

Given an option's parameters, calculates:

| Greek | Meaning |
|-------|---------|
| **Price** | Fair value of the option (call or put) |
| **Delta** | Rate of change of price relative to spot |
| **Gamma** | Rate of change of delta relative to spot |
| **Vega** | Sensitivity to implied volatility |
| **Theta** | Time decay (value lost per day) |

Also generates plots of option price and delta across a range of spot prices.

![Option price vs spot price](https://github.com/user-attachments/assets/54758915-0151-439b-b4eb-a8f8cf966f82)

## Usage

```bash
uv run python main.py
```

Example output (strike=100, spot=100, σ=0.20, T=1yr, r=5%):

```
Price: 10.4506
Delta: 0.6368
Gamma: 0.0188
Vega:  37.5240
Theta: -6.4140
```

## Project Structure

```
options_calculator/
├── pricer.py      # Black-Scholes formula + Greeks (delta, gamma, vega, theta)
├── visualizer.py  # Matplotlib plots of price and delta vs. spot price
└── main.py        # Entry point with example parameters
```

## Tech Stack

- **NumPy** — vectorized math
- **SciPy** — normal distribution (CDF/PDF)
- **Matplotlib** — plotting
- **uv** — Python package management

## Setup

```bash
git clone https://github.com/DanXSpace/options-calculator
cd options-calculator
uv sync
uv run python main.py
```
