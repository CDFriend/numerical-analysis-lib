import numpy as np
import matplotlib.pyplot as plt
from polynomial import Polynomial


def lagrange(x, y):
    """Constructs an interpolating polynomial for a set of data points using the
    Lagrange method.
    :param x Vector of x data points
    :param y Vector of y data points
    :return Interpolating polynomial for x and y points.
    """
    assert len(x) == len(y), "Length mismatch for x and y datapoints"

    # P(x) = (sum of) Li(x)f(xi)
    px = Polynomial(np.zeros(len(x) - 1))
    for xi, yi in zip(x, y):
        li_num = Polynomial([1])
        li_den = 1
        for xj in x:
            if xj == xi:
                continue

            li_num *= Polynomial([-xj, 1])  # (x - xj)
            li_den *= (xi - xj)

        li = li_num * (yi / li_den)
        px = px + li

    return px


if __name__ == "__main__":
    x = np.array([1, 2, 3])
    y = np.array([12, 3, 14])
    px = lagrange(x, y)

    plt.scatter(x, y)

    polypts_x, polypts_y = px.eval_range(0, 5)
    plt.plot(polypts_x, polypts_y)

    plt.show()
