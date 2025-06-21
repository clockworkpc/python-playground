import pytest
from code.module4.discrete_math import DiscreteMath


def test_is_prime():
    assert DiscreteMath.is_prime(7) == True


def test_is_prime():
    assert DiscreteMath.is_prime(41) == True


def test_is_prime():
    assert DiscreteMath.is_prime(8) == False


def test_is_prime():
    assert DiscreteMath.is_prime(11) == True


def test_prime_factors():
    assert DiscreteMath.prime_factors(28) == [2, 2, 7]


def test_mod_exp():
    assert DiscreteMath.modular_exponentiation(2, 5, 13) == 6


def test_n_choose_k():
    assert DiscreteMath.n_choose_k(5, 2) == 10


def test_n_choose_k():
    assert DiscreteMath.combinatorics(5, 2) == 10


def test_count_divisors():
    assert DiscreteMath.count_divisors(12) == 6
