
import pytest
from code.interview.graph_algorithm import GraphAlgorithm

# Dijkstra's Shortest Path
def test_dijkstra_case1():
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'C': 2, 'D': 5},
        'C': {'D': 1},
        'D': {}
    }
    assert GraphAlgorithm.dijkstra(graph, 'A', 'D') == 4

def test_dijkstra_case2():
    assert GraphAlgorithm.dijkstra({'A': {'B': 1}}, 'A', 'B') == 1

def test_dijkstra_case3():
    graph = {'A': {'B': 1}, 'B': {'C': 2}, 'C': {'D': 1}, 'D': {}}
    assert GraphAlgorithm.dijkstra(graph, 'A', 'D') == 4

def test_dijkstra_case4():
    assert GraphAlgorithm.dijkstra({'A': {}}, 'A', 'A') == 0

def test_dijkstra_case5():
    assert GraphAlgorithm.dijkstra({'A': {'B': 5}, 'B': {}, 'C': {'D': 1}}, 'A', 'C') == float('inf')
