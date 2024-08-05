import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# from _07_avlTree.avlTree import AVLTree
from _08_binaryHeap.binaryHeap import BinaryHeap


def test_min_heap():
    # Instantiate a min-heap
    min_heap = BinaryHeap('min')
    
    # Insert elements
    min_heap.insert(10)
    min_heap.insert(5)
    min_heap.insert(3)
    
    # Check the root (should be the smallest element)
    assert min_heap.peek() == 3
    
    # Extract root and check the new root
    assert min_heap.extract_root() == 3
    assert min_heap.peek() == 5
    
    # Extract remaining elements
    assert min_heap.extract_root() == 5
    assert min_heap.extract_root() == 10
    
    # Check if heap is empty
    assert len(min_heap) == 0