import pytest
from calc import add, subtract
from calc import tan
import math
from calc import multiply
from calc import log
from calc import sqrt
from calc import power
from calc import divide

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(3, 5) == -2

def test_tan_function():
    assert tan(0) == 0
    assert tan(math.pi / 4) == pytest.approx(1, 0.0001)


def test_log_non_positive_number():
    assert log(0) == "Error: Logarithm of non-positive number is not allowed"
    assert log(-1) == "Error: Logarithm of non-positive number is not allowed"


def test_power_zero_exponent():
    assert power(5, 0) == 1


def test_divide_by_zero():
    assert divide(10, 0) == "Error: Division by zero is not allowed"


def test_log():
    assert log(1) == 0
    assert log(math.e) == 1
    assert log(0) == "Error: Logarithm of non-positive number is not allowed"
    assert log(-1) == "Error: Logarithm of non-positive number is not allowed"


def test_power():
    assert power(2, 3) == 8
    assert power(5, 0) == 1
    assert power(2, -2) == 0.25
    assert power(-2, 3) == -8


def test_divide():
    assert divide(10, 2) == 5
    assert divide(5, 0) == "Error: Division by zero is not allowed"
    assert divide(-10, 2) == -5
    assert divide(0, 5) == 0


def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-1, 5) == -5
    assert multiply(0, 10) == 0
    assert multiply(-3, -3) == 9


def test_log_positive_number():
    assert log(1) == 0


def test_power_function():
    assert power(2, 3) == 8


def test_divide_non_zero():
    assert divide(10, 2) == 5


def test_multiply_positive_numbers():
    assert multiply(3, 4) == 12


def test_log_non_positive_number():
    assert log(0) == "Error: Logarithm of non-positive number is not allowed"
    assert log(-1) == "Error: Logarithm of non-positive number is not allowed"


def test_power_negative_exponent():
    assert power(2, -3) == 0.125


def test_divide_by_zero():
    assert divide(10, 0) == "Error: Division by zero is not allowed"


def test_log_non_positive():
    assert log(0) == "Error: Logarithm of non-positive number is not allowed"
    assert log(-1) == "Error: Logarithm of non-positive number is not allowed"


def test_sqrt_negative():
    assert sqrt(-4) == "Error: Square root of negative number is not allowed"


def test_power():
    assert power(2, 3) == 8
    assert power(5, 0) == 1


def test_divide_by_zero():
    assert divide(10, 0) == "Error: Division by zero is not allowed"

