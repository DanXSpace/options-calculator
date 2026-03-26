import numpy as np
from scipy.stats import norm

def calc_d1(strike_price, expiration, sigma, spot_price, treasury_rate):
    d1 = (np.log(spot_price / strike_price) + (treasury_rate + sigma**2 / 2) * expiration) / (sigma * np.sqrt(expiration))
    return d1

def calc_d2(strike_price, expiration, sigma, spot_price, treasury_rate):
    d2 = calc_d1(strike_price, expiration, sigma, spot_price, treasury_rate) - sigma * np.sqrt(expiration)
    return d2

def black_scholes(strike_price, expiration, sigma, spot_price, treasury_rate, call=True):
    d1 = calc_d1(strike_price, expiration, sigma, spot_price, treasury_rate)
    d2 = calc_d2(strike_price, expiration, sigma, spot_price, treasury_rate)
    call_scholes = spot_price * norm.cdf(d1) - strike_price * np.exp(-treasury_rate * expiration) * norm.cdf(d2)
    put_scholes = strike_price * np.exp(-treasury_rate * expiration) * norm.cdf(-d2) - spot_price * norm.cdf(-d1)
    if call:
        return call_scholes
    else:
        return put_scholes

def delta(strike_price, expiration, sigma, spot_price, treasury_rate, call=True):
    d1 = calc_d1(strike_price, expiration, sigma, spot_price, treasury_rate)
    call_delta = norm.cdf(d1)
    put_delta = norm.cdf(d1) - 1
    if call:
        return call_delta
    else:
        return put_delta

def gamma(strike_price, expiration, sigma, spot_price, treasury_rate):
    d1 = calc_d1(strike_price, expiration, sigma, spot_price, treasury_rate)
    gamma = (norm.pdf(d1)) / (spot_price * sigma * np.sqrt(expiration))
    return gamma

def vega(strike_price, expiration, sigma, spot_price, treasury_rate):
    d1 = calc_d1(strike_price, expiration, sigma, spot_price, treasury_rate)
    vega = spot_price * norm.pdf(d1) * np.sqrt(expiration)
    return vega

def theta(strike_price, expiration, sigma, spot_price, treasury_rate, call = True):
    d1 = calc_d1(strike_price, expiration, sigma, spot_price, treasury_rate)
    d2 = calc_d2(strike_price, expiration, sigma, spot_price, treasury_rate)
    call_theta = ((-spot_price * norm.pdf(d1) * sigma) / (2 *np.sqrt(expiration))) - treasury_rate * strike_price * np.exp(-treasury_rate * expiration) * norm.cdf(d2)
    put_theta = ((-spot_price * norm.pdf(d1) * sigma) / (2 *np.sqrt(expiration))) + treasury_rate * strike_price * np.exp(-treasury_rate * expiration) * norm.cdf(-d2)
    if call:
        return call_theta
    else:
        return put_theta
