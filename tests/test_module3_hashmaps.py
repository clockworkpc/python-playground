# type: ignore[arg-type]

from code.module3.hashmaps import Hashmaps
import pytest

def test_count_unique_strings():
    assert Hashmaps.count_frequencies(["a", "b", "a", "c", "b"]) == {"a": 2, "b": 2, "c": 1}

def test_count_empty():
    assert Hashmaps.count_frequencies([]) == {}

def test_count_single():
    assert Hashmaps.count_frequencies(["x"]) == {"x": 1}

def test_count_case_sensitive():
    assert Hashmaps.count_frequencies(["X", "x", "X"]) == {"X": 2, "x": 1}

def test_count_numeric_keys():
    assert Hashmaps.count_frequencies(["1", "2", "1"]) == {"1": 2, "2": 1}
