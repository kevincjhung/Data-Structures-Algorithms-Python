import os
import sys
import unittest
import pytest


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# from _07_avlTree.avlTree import AVLTree
from _08_binaryHeap.binaryHeap import BinaryHeap

    
class TestHeapInitialization:
    def test_default_initialization(self):
        heap = BinaryHeap()
        assert heap.heap_type == 'min'
        assert len(heap) == 0

    def test_custom_initialization(self):
        min_heap = BinaryHeap('min')
        max_heap = BinaryHeap('max')
        assert min_heap.heap_type == 'min'
        assert max_heap.heap_type == 'max'
        assert len(min_heap) == 0
        assert len(max_heap) == 0

class TestHeapInsertion:
    def test_single_insertion(self):
        heap = BinaryHeap('min')
        heap.insert(3)
        assert heap.peek() == 3
        assert len(heap) == 1

    def test_multiple_insertion(self):
        heap = BinaryHeap('min')
        heap.insert(10)
        heap.insert(5)
        heap.insert(20)
        heap.insert(40)
        heap.insert(60)
        heap.insert(80)
        heap.insert(90)
        
        assert heap.peek() == 5
        assert len(heap) == 7

    def test_heap_property(self):
        min_heap = BinaryHeap('min')
        min_heap.insert(10)
        min_heap.insert(5)
        min_heap.insert(20)
        assert min_heap.peek() == 5
        
        max_heap = BinaryHeap('max')
        max_heap.insert(10)
        max_heap.insert(5)
        max_heap.insert(20)
        assert max_heap.peek() == 20

class TestHeapExtraction:
    def test_extract_root(self):
        heap = BinaryHeap('min')
        heap.insert(10)
        heap.insert(5)
        heap.insert(20)
        assert heap.extract_root() == 5
        assert heap.peek() == 10
        assert len(heap) == 2

    def test_extract_multiple(self):
        heap = BinaryHeap('max')
        heap.insert(10)
        heap.insert(20)
        heap.insert(5)
        assert heap.extract_root() == 20
        assert heap.extract_root() == 10
        assert heap.extract_root() == 5
        assert len(heap) == 0

    def test_extract_empty_heap(self):
        heap = BinaryHeap('min')
        with pytest.raises(IndexError):
            heap.extract_root()

class TestHeapPeek:
    def test_peek_non_empty_heap(self):
        heap = BinaryHeap('min')
        heap.insert(5)
        assert heap.peek() == 5

    def test_peek_empty_heap(self):
        heap = BinaryHeap('min')
        with pytest.raises(IndexError):
            heap.peek()

    
if __name__ == '__main__':
    unittest.main()