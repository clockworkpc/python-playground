import pytest
from code.interview.string_algorithm import StringAlgorithm


# # Longest Palindromic Substring
# def test_longest_palindromic_substring_case1():
#     assert StringAlgorithm.longest_palindromic_substring("babad") in ["bab", "aba"]
#
#
# def test_longest_palindromic_substring_case2():
#     assert StringAlgorithm.longest_palindromic_substring("cbbd") == "bb"
#
#
# def test_longest_palindromic_substring_case3():
#     assert StringAlgorithm.longest_palindromic_substring("a") == "a"
#
#
# def test_longest_palindromic_substring_case4():
#     assert StringAlgorithm.longest_palindromic_substring("ac") in ["a", "c"]
#
#
# def test_longest_palindromic_substring_case5():
#     assert (
#         StringAlgorithm.longest_palindromic_substring("racecarannakayak") == "racecar"
#     )
#
#
# # String Matching
# def test_string_matching_case1():
#     assert StringAlgorithm.string_match("hello", "ll") == 2
#
#
# def test_string_matching_case2():
#     assert StringAlgorithm.string_match("aaaaa", "bba") == -1
#
#
# def test_string_matching_case3():
#     assert StringAlgorithm.string_match("abc", "c") == 2
#
#
# def test_string_matching_case4():
#     assert StringAlgorithm.string_match("abcdef", "def") == 3
#
#
# def test_string_matching_case5():
#     assert StringAlgorithm.string_match("abcxabcdabxabcdabcdabcy", "abcdabcy") == 15
#
#
# String Permutation


def test_string_permutation_case1():
    assert StringAlgorithm.string_permutation("abc", "bca") is True


def test_string_permutation_case2():
    assert StringAlgorithm.string_permutation("abc", "def") is False


def test_string_permutation_case3():
    assert StringAlgorithm.string_permutation("aabbcc", "abcabc") is True


def test_string_permutation_case4():
    assert StringAlgorithm.string_permutation("hello", "oellh") is True


def test_string_permutation_case5():
    assert StringAlgorithm.string_permutation("test", "sett") is True


# case-sensitive permutation test
def test_string_permutation_case6():
    assert StringAlgorithm.string_permutation("abc", "ABC") is False


# 5 permutation tests including spaces and special characters, where order matters
def test_string_permutation_case7():
    assert StringAlgorithm.string_permutation("a b c", "c b a") is True


def test_string_permutation_case8():
    assert StringAlgorithm.string_permutation("a!b@c#", "c#b!a@") is True


def test_string_permutation_case9():
    assert StringAlgorithm.string_permutation("hello world", "world hello") is False
