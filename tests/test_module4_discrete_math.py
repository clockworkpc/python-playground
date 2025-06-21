import pytest
from code.module4_discrete_math import Module4

def test_is_prime():
    assert Module4.is_prime(7) == True

def test_prime_factors():
    assert Module4.prime_factors(28) == [2, 2, 7]

def test_mod_exp():
    assert Module4.mod_exp(2, 5, 13) == 6

def test_n_choose_k():
    assert Module4.n_choose_k(5, 2) == 10

def test_count_divisors():
    assert Module4.count_divisors(12) == 6
