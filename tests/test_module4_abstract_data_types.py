import pytest
from code.module4.abstract_data_types import AbstractDataTypes


def test_stack_operations():
    assert AbstractDataTypes.stack_operations(["push", "push", "pop"]) == [1]


def test_queue_operations():
    assert AbstractDataTypes.queue_operations(["enqueue", "enqueue", "dequeue"]) == [1]


# def test_priority_queue_insert():
#     assert AbstractDataTypes.priority_queue_insert([3, 1, 2]) == [1, 2, 3]
#
#
# def test_linked_list_insert():
#     assert AbstractDataTypes.linked_list_insert([1, 2, 3], 4) == [1, 2, 3, 4]
#
#
# def test_tree_traversal_inorder():
#     assert AbstractDataTypes.tree_traversal_inorder([1, 2, 3]) == [2, 1, 3]
