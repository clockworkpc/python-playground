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

def test_equal():
    assert StringOps.compare_strings("test", "test") is True

def test_case_mismatch():
    assert StringOps.compare_strings("Test", "test") is False

def test_whitespace_diff():
    assert StringOps.compare_strings("abc", "abc ") is False

def test_empty_strings():
    assert StringOps.compare_strings("", "") is True

def test_unicode():
    assert StringOps.compare_strings("café", "café") is True

def test_normal_concat():
    assert StringOps.concat_strings("hello", "world") == "helloworld"

def test_with_space():
    assert StringOps.concat_strings("foo", " bar") == "foo bar"

def test_empty_a():
    assert StringOps.concat_strings("", "yo") == "yo"

def test_empty_b():
    assert StringOps.concat_strings("yo", "") == "yo"

def test_both_empty():
    assert StringOps.concat_strings("", "") == ""

def test_basic_reverse():
    assert StringOps.reverse_string("abc") == "cba"

def test_empty_reverse():
    assert StringOps.reverse_string("") == ""

def test_palindrome():
    assert StringOps.reverse_string("madam") == "madam"

def test_numeric_string():
    assert StringOps.reverse_string("123") == "321"

def test_unicode_string():
    assert StringOps.reverse_string("你好") == "好你"
