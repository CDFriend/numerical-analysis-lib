from polynomial import Polynomial


def test_repr():
    p = Polynomial([1])
    assert str(p) == "f(x) = 1"

    p = Polynomial([1, 2, 3])
    assert str(p) == "f(x) = 1 + 2x + 3*x^2"

    p = Polynomial([-1, -2, -3])
    assert str(p) == "f(x) = -1 - 2x - 3*x^2"


def test_eval():
    p = Polynomial([1])
    assert p.eval(2) == 1

    p = Polynomial([1, 2])
    assert p.eval(2) == 5

    p = Polynomial([1, 2, 3])
    assert p.eval(2) == 17


def test_eval_range():
    p = Polynomial([3, 2, 1])  # x^2 + 2x + 3
    x, y = p.eval_range(0, 3, num=4)

    assert list(y) == [3, 6, 11, 18]


def test_derivative():
    p = Polynomial([1])
    assert p.derivative(1) == 0

    p = Polynomial([1, 2])
    assert p.derivative(1) == 2

    p = Polynomial([1, 2, 3])  # 1 + 2x + 3x^2
    assert p.derivative(1) == 8


def test_multiply():
    p1, p2 = Polynomial([2]), Polynomial([2])  # f(x) = 4
    assert str(p1 * p2) == "f(x) = 4"

    # (1 + 2x)(3 + 4x) = 3 + 10x + 8x^2
    p1, p2 = Polynomial([1, 2]), Polynomial([3, 4])
    assert str(p1 * p2) == "f(x) = 3 + 10x + 8*x^2"

