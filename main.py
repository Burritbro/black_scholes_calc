from numpy import *
import pandas

# ------------- creating a dataframe --------------- #
distribution_d_f = pandas.read_csv("bracker_normal_distribution.csv")
distribution_df = distribution_d_f.astype(float)
# distribution_df['D'] = pandas.to_numeric(distribution_df['D'])
# print(type(distribution_df['D']))

# print(distribution_df.loc[distribution_df['D'] == -3.05, 'N(d)'])


def questions():
    # ------------ gather all inputs ----------------- #
    stock_p = float(input("What is the stock price? $"))
    strike_p = float(input("What is the strike price? $"))
    interest_rate = float(input("What is the interest rate? %")) * .01
    t = float(input("How many days till expiration? "))
    sig = float(input("what is the volatility? %")) * .01

    # ---------------- call calc function ------------------ #
    print(calculation(stock_price=stock_p, strike_price=strike_p, interest=interest_rate, time=t, sigma=sig))


def calculation(stock_price, strike_price, interest, time, sigma):
    # ----------- finding d1; distribution for what you paid -------------- #
    d1 = round((log((stock_price / strike_price)) + (interest + ((sigma ** 2) / 2)) * (time / 365)) / (
            sigma * sqrt((time / 365))), 2)
    # print(f"d1:{d1}")

    # -------------- distribution for what you get --------------- #
    d2 = round((log((stock_price / strike_price)) + (interest - ((sigma ** 2) / 2)) * (time / 365)) / (
            sigma * sqrt((time / 365))), 2)

    # -------------- N(d1) and N(d2) ------------------ #

    n_1 = float(distribution_df.loc[distribution_df['D'] == d1, 'N(d)'])
    print(f"n_1: {n_1}")

    n_2 = float(distribution_df.loc[distribution_df['D'] == d2, 'N(d)'])
    print(f"n_2: {n_2}")

    # ---------------- call price --------------------- #
    paid = (stock_price * n_1)
    acquire = (strike_price / power(e, (interest * (time / 365))) * n_2)
    # print(paid)
    call_value = paid - acquire
    # if int(str(round(call_value, 2)).split('.')[1]) == 1:
    #     return f"${round(call_value, 2)}0"
    # else:
    return f"${round(call_value, 2)}"


questions()
