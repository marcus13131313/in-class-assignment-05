import pytest

from src.my_math import sum, multiply, difference

def test_sum():
    res = sum(1,1)
    assert res == 2

# Work together
## Test multiply
def test_multiply():# test multiply,see is it ok to work with different of number like -value
    res = multiply(2, 3)
    assert res == 6
    res = multiply(-2, 3)
    assert res == -6
    res = multiply(0, 5)
    assert res == 0

# Check for understanding
## Test difference
def test_difference(): # test difference, inorder to work withh all cases
    res = difference(5, 3)
    assert res == 2
    res = difference(3, 5)
    assert res == -2
    res = difference(0, 0)
    assert res == 0


# Work together
## Test absolute sum
def test_absolute_sum(): # test it to see is all the value keep + value or not
    res = absolute_sum(3, -4)
    assert res == 7
    res = absolute_sum(-5, -6)
    assert res == 11
    res = absolute_sum(0, 0)
    assert res == 0


# Check for understanding
## Test calculate age

def test_calculate_birth_year():
    res = calculate_birth_year(2025, 25, True)
    assert res == 2000  
    res = calculate_birth_year(2025, 25, False)
    assert res == 1999  
