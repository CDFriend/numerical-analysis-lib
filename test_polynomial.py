from polynomial import Polynomial


def test_repr():
    p = Polynomial([1])
    assert str(p) == "1"

    p = Polynomial([1, 2, 3])
    assert str(p) == "1 + 2x + 3*x^2"

    p = Polynomial([-1, -2, -3])
    assert str(p) == "-1 - 2x - 3*x^2"


def test_eval():
    p = Polynomial([1])
    assert p.eval(2) == 1

    p = Polynomial([1, 2])
    assert p.eval(2) == 5

    p = Polynomial([1, 2, 3])
    assert p.eval(2) == 17