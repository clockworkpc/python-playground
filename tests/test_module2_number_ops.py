# type: ignore[arg-type]

from module2.number_ops import NumberOps
import pytest

def test_add_positive():
    assert NumberOps.add_numbers(3, 5) == 8

def test_add_negative():
    assert NumberOps.add_numbers(-4, -6) == -10

def test_add_mixed():
    assert NumberOps.add_numbers(10, -3) == 7

def test_add_zero():
    assert NumberOps.add_numbers(0, 5) == 5

def test_add_large():
    assert NumberOps.add_numbers(999_999, 1) == 1_000_000

def test_digits_simple():
    assert NumberOps.split_digits(1234) == [1, 2, 3, 4]

def test_digits_single():
    assert NumberOps.split_digits(7) == [7]

def test_digits_zero():
    assert NumberOps.split_digits(0) == [0]

def test_digits_large():
    assert NumberOps.split_digits(9876543210) == [9,8,7,6,5,4,3,2,1,0]

def test_digits_leading_zero_sim():
    assert NumberOps.split_digits(int("0012")) == [1, 2]  # int drops leading zeros
