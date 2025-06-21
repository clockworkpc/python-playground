import pytest
from code.module4_abstract_data_types import Module4

def test_stack_operations():
    assert Module4.stack_operations(['push', 'push', 'pop']) == [1]

def test_queue_operations():
    assert Module4.queue_operations(['enqueue', 'enqueue', 'dequeue']) == [1]

def test_priority_queue_insert():
    assert Module4.priority_queue_insert([3, 1, 2]) == [1, 2, 3]

def test_linked_list_insert():
    assert Module4.linked_list_insert([1, 2, 3], 4) == [1, 2, 3, 4]

def test_tree_traversal_inorder():
    assert Module4.tree_traversal_inorder([1, 2, 3]) == [2, 1, 3]
