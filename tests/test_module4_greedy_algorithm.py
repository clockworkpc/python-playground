# type: ignore[arg-type]

from code.module4.coin_change import CoinChange
import pytest

def test_exact_match():
    assert CoinChange.min_coins([1, 5, 10, 25], 30) == 2  # 25 + 5

def test_multiple_combinations():
    assert CoinChange.min_coins([1, 3, 4], 6) == 2  # 3 + 3

def test_zero_amount():
    assert CoinChange.min_coins([1, 5, 10], 0) == 0

def test_single_denom():
    assert CoinChange.min_coins([1], 7) == 7

def test_large_amount():
    assert CoinChange.min_coins([1, 5, 10, 25], 99) == 9  # 3x25 + 2x10 + 4x1
