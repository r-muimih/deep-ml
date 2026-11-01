import math

PI = 3.14159

def power_grid_forecast(consumption_data):
    n = len(consumption_data)
    xs = list(range(1, n + 1))  # days are 1-indexed, so day 15 is x = 15

    # 1) Remove the daily fluctuation
    detrended = [
        y - 10 * math.sin(2 * PI * x / 10)
        for x, y in zip(xs, consumption_data)
    ]

    # 2) Least-squares line y = m*x + b
    sum_x = sum(xs)
    sum_y = sum(detrended)
    sum_xy = sum(x * y for x, y in zip(xs, detrended))
    sum_x2 = sum(x * x for x in xs)

    m = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x ** 2)
    b = (sum_y - m * sum_x) / n

    # 3) Base prediction for day 15
    base15 = m * 15 + b

    # 4) Add the day 15 fluctuation back
    f15 = 10 * math.sin(2 * PI * 15 / 10)
    pred15 = base15 + f15

    # 5) Round, then apply the 5% safety margin, rounding up
    return math.ceil(1.05 * round(pred15))