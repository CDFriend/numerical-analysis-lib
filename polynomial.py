import numpy as np


class Polynomial:
    """Represents a polynomial function."""
    def __init__(self, coefficients):
        """Creates a new Polynomial.
        :param coefficients: Coefficients of each polynomial term, starting from 0th order.
        """
        assert len(coefficients) >= 1, "Polynomial must have at least 1 term"
        self._num_terms = len(coefficients)
        self._coefficients = np.array(coefficients)

    def __repr__(self):
        out = ""
        for i, a in enumerate(self._coefficients):
            if a == 0:
                continue

            sign = "+" if a > 0 else "-"
            if i > 1:
                out += (" %s %d*x^%d" % (sign, abs(a), i))
            elif i == 1:
                out += (" %s %dx" % (sign, abs(a)))
            else:
                if a < 0:
                    out += "-"
                out += ("%d" % (abs(a)))

        return out.strip()

    def eval(self, x):
        """Evaluate using Horner's method"""
        i = self._num_terms - 2
        b_last = self._coefficients[-1]
        while i >= 0:
            b = self._coefficients[i] + b_last * x
            b_last = b
            i -= 1

        return b_last
