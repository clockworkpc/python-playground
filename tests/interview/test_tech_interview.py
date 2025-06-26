import pytest
from code.interview.tech_interview import TechInterview as TI

# Are characters case-sensitive?
# Should whitespace be considered?
# Are only letters allowed, or can there be digits/symbols?
# Should the original strings remain unchanged?


def test_two_strings_are_anagrams_case1():
    assert TI.are_anagrams("abc", "cba") == True


def test_two_strings_are_anagrams_case2_case_sensitive():
    assert (
        TI.are_anagrams("abc", "CBA", case_sensitive=True, allowed_characters=["alpha"])
        == False
    )


def test_two_strings_are_anagrams_case3_with_whitespace():
    assert (
        TI.are_anagrams(
            "a b c",
            "c b a",
            allowed_characters=["alpha", "space"],
        )
        == True
    )


def test_anagrams_with_whitespace_ignored():
    assert (
        TI.are_anagrams(
            "a b c",
            "cb a",
        )
        == False
    )


def test_anagrams_with_whitespace_required_mismatch():
    assert (
        TI.are_anagrams("a b c", "abc", allowed_characters=["alpha", "space"]) == False
    )


def test_anagrams_with_tabs_and_spaces():
    assert (
        TI.are_anagrams("a\tb c", "c b\ta", allowed_characters=["alpha", "space"])
        == True
    )


def test_anagrams_with_whitespace_only_strings():
    assert (
        TI.are_anagrams("   ", " ", allowed_characters=["alpha", "space"]) == False
    )  # Unequal whitespace counts


def test_anagrams_with_whitespace_ignored_and_symbols():
    assert (
        TI.are_anagrams("a b!c", "c!b a", allowed_characters=["alpha", "punctuation"])
        == True
    )


def test_two_strings_are_anagrams_case4_ignore_symbols():
    assert (
        TI.are_anagrams("a!b@c", "c@b!a", allowed_characters=["alpha", "punctuation"])
        == True
    )


def test_two_strings_are_anagrams_case5_not_anagrams():
    assert TI.are_anagrams("abc", "def") == False


# **Find the first non-repeating character in a string**
#
# * What should be returned if all characters repeat?
# * Is the string case-sensitive?
# * What is the expected output: index or character?


def test_first_non_repeating_character_case1():
    assert (
        TI.first_non_repeating_character("abcabcde", case_sensitive=False, mode="char")
        == "d"
    )


def test_first_non_repeating_character_case2_case_sensitive():
    assert (
        TI.first_non_repeating_character(
            "aAbBcC", case_sensitive=False, allowed_characters=["alpha"], mode="char"
        )
        is None
    )


def test_first_non_repeating_character_case3_all_repeat():
    assert (
        TI.first_non_repeating_character(
            "aabbcc", case_sensitive=False, allowed_characters=["alpha"], mode="char"
        )
        is None
    )


def test_first_non_repeating_character_case4_empty_string():
    assert (
        TI.first_non_repeating_character(
            "", case_sensitive=False, allowed_characters=["alpha"], mode="char"
        )
        is None
    )


def test_first_non_repeating_character_case5_index_mode():
    assert (
        TI.first_non_repeating_character(
            "abcabcde",
            case_sensitive=False,
            allowed_characters=["alpha"],
            mode="index",
        )
        == 6
    )


def test_first_non_repeating_character_case6_case_sensitive_index():
    assert (
        TI.first_non_repeating_character(
            "aAbBcC", case_sensitive=True, allowed_characters=["alpha"], mode="index"
        )
        == 0
    )


# Additional tests for various tech interview problems


# **Reverse a string in-place**
def test_reverse_string_ascii():
    assert TI.reverse_string("hello", encoding="ascii") == "olleh"


#
def test_reverse_string_unicode():
    assert TI.reverse_string("héllo", encoding="utf-8") == "olléh"


def test_reverse_string_with_memory():
    assert TI.reverse_string("world", encoding="ascii") == "dlrow"


def test_reverse_string_empty():
    assert TI.reverse_string("", encoding="ascii") == ""


# **Rotate an array by k steps**
def test_rotate_array_right_basic():
    assert TI.rotate_array([1, 2, 3, 4, 5], k=2, direction="right") == [
        4,
        5,
        1,
        2,
        3,
    ]


def test_rotate_array_left_with_memory():
    assert TI.rotate_array([1, 2, 3, 4, 5], k=2, direction="left") == [
        3,
        4,
        5,
        1,
        2,
    ]


def test_rotate_array_k_greater_than_length():
    assert TI.rotate_array([1, 2, 3], k=5, direction="right") == [
        2,
        3,
        1,
    ]


def test_rotate_array_empty():
    assert TI.rotate_array([], k=3, direction="left") == []


# **Longest substring without repeating characters**
def test_longest_unique_substring_ascii_length():
    assert TI.longest_unique_substring("abcabcbb", return_type="length") == 3


def test_longest_unique_substring_ascii_substring():
    assert TI.longest_unique_substring("abcabcbb", return_type="substring") == "abc"


def test_longest_unique_substring_unicode():
    assert TI.longest_unique_substring("héllohé", return_type="length") == 3


def test_longest_unique_substring_case_sensitive():
    assert TI.longest_unique_substring("aAbBcCd", return_type="length") == 7


#
# # === Data Structures ===
#
#
# # Stack using queues
# def test_stack_using_one_queue_push_costly():
#     stack = TI.StackUsingQueue(mode="push_costly")
#     stack.push(1)
#     stack.push(2)
#     assert stack.pop() == 2
#     assert stack.top() == 1
#
#
# def test_stack_using_two_queues_pop_costly():
#     stack = TI.StackUsingQueue(mode="pop_costly")
#     stack.push(3)
#     stack.push(4)
#     assert stack.pop() == 4
#     assert stack.top() == 3
#
#
# # Hash map for duplicates
# def test_find_duplicates_boolean_result():
#     assert TI.find_duplicates([1, 2, 3, 1]) == True
#
#
# def test_find_duplicates_multiple_types():
#     assert TI.find_duplicates(["a", "b", "a", 1, 2, 1]) == True
#
#
# def test_find_duplicates_preserve_order():
#     assert TI.find_duplicates(["x", "y", "x"], return_list=True) == ["x"]
#
#
# # Intersection of arrays
# def test_array_intersection_with_duplicates():
#     assert TI.intersect_arrays([1, 2, 2, 1], [2, 2], allow_duplicates=True) == [2, 2]
#
#
# def test_array_intersection_sorted_output():
#     assert TI.intersect_arrays([4, 9, 5], [9, 4, 9, 8, 4], sort_output=True) == [4, 9]
#
#
# # LRU Cache
# def test_lru_cache_put_get():
#     cache = TI.LRUCache(capacity=2)
#     cache.put(1, 1)
#     cache.put(2, 2)
#     assert cache.get(1) == 1
#     cache.put(3, 3)
#     assert cache.get(2) == -1  # evicted
#     cache.put(4, 4)
#     assert cache.get(1) == -1
#     assert cache.get(3) == 3
#     assert cache.get(4) == 4
#
#
# # === Algorithms ===
#
#
# # Merge sorted arrays
# def test_merge_sorted_arrays_in_place():
#     assert TI.merge_sorted([1, 3, 5], [2, 4, 6], in_place=True) == [1, 2, 3, 4, 5, 6]
#
#
# def test_merge_sorted_arrays_with_duplicates():
#     assert TI.merge_sorted([1, 2, 2], [2, 3], in_place=False) == [1, 2, 2, 2, 3]
#
#
# # Detect cycle in linked list
# def test_linked_list_cycle_detection():
#     node1 = TI.ListNode(1)
#     node2 = TI.ListNode(2)
#     node1.next = node2
#     node2.next = node1  # cycle
#     assert TI.has_cycle(node1) == True
#
#
# def test_linked_list_no_cycle():
#     node1 = TI.ListNode(1)
#     node2 = TI.ListNode(2)
#     node1.next = node2
#     assert TI.has_cycle(node1) == False
#
#
# # Binary search
# def test_binary_search_found():
#     assert TI.binary_search([1, 2, 3, 4, 5], 3) == 2
#
#
# def test_binary_search_not_found():
#     assert TI.binary_search([1, 2, 4, 5], 3) == -1
#
#
# # Maximum subarray sum
# def test_kadane_mixed_array():
#     assert TI.max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
#
#
# def test_kadane_all_negative():
#     assert TI.max_subarray_sum([-3, -2, -1]) == -1
#
#
# # Count number of islands
# def test_count_islands_basic():
#     grid = [["1", "1", "0", "0"], ["1", "0", "0", "1"], ["0", "0", "1", "1"]]
#     assert TI.count_islands(grid, diagonals=False) == 3
#
#
# # === Complexity Focus ===
#
#
# # Optimize brute-force
# def test_optimized_sum_to_target():
#     assert TI.two_sum([2, 7, 11, 15], target=9) == (0, 1)
#
#
# # Recursive vs Iterative
# def test_factorial_recursive_vs_iterative():
#     assert TI.factorial_recursive(5) == 120
#     assert TI.factorial_iterative(5) == 120
#
#
# # Convert recursive to iterative
# def test_dfs_recursive_vs_iterative():
#     graph = {0: [1, 2], 1: [0, 3], 2: [0], 3: [1]}
#     assert TI.dfs_recursive(graph, 0) == TI.dfs_iterative(graph, 0)
