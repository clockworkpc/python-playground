
import pytest
from code.interview.tree_algorithm import TreeAlgorithm, TreeNode

# Lowest Common Ancestor
def test_lowest_common_ancestor_case1():
    root = TreeNode.build_bst([6,2,8,0,4,7,9,3,5])
    assert TreeAlgorithm.lowest_common_ancestor(root, 2, 8) == 6

def test_lowest_common_ancestor_case2():
    root = TreeNode.build_bst([6,2,8,0,4,7,9,3,5])
    assert TreeAlgorithm.lowest_common_ancestor(root, 2, 4) == 2

def test_lowest_common_ancestor_case3():
    root = TreeNode.build_bst([1,2])
    assert TreeAlgorithm.lowest_common_ancestor(root, 1, 2) == 1

def test_lowest_common_ancestor_case4():
    root = TreeNode.build_bst([5,3,8,2,4,7,9])
    assert TreeAlgorithm.lowest_common_ancestor(root, 4, 7) == 5

def test_lowest_common_ancestor_case5():
    root = TreeNode.build_bst([5])
    assert TreeAlgorithm.lowest_common_ancestor(root, 5, 5) == 5
