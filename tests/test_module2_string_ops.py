# type: ignore[arg-type]

from module2.string_ops import StringOps
import pytest

def test_basic_split():
    assert StringOps.split_words("hello world") == ["hello", "world"]

def test_empty_string():
    assert StringOps.split_words("") == []

def test_trailing_spaces():
    assert StringOps.split_words("  a  b  ") == ["a", "b"]
#
def test_comma_split_custom():
    assert StringOps.split_words("a,b,c", ",") == ["a", "b", "c"]

def test_multiple_delimiters():
    assert StringOps.split_words("a--b--c", "--") == ["a", "b", "c"]
