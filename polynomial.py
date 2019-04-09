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
        out = "f(x) = "
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
        return self._horners_coefficients(x)[0]

    def derivative(self, x):
        """Get the function's derivative using Horner's method."""
        if self._num_terms == 1:
            return 0  # constant
        else:
            return Polynomial(self._horners_coefficients(x)[1:]).eval(x)

    def _horners_coefficients(self, x0):
        b = np.ndarray(self._num_terms)

        i = self._num_terms - 2
        b[-1] = self._coefficients[-1]
        while i >= 0:
            b[i] = self._coefficients[i] + b[i + 1] * x0
            i -= 1

        return b
