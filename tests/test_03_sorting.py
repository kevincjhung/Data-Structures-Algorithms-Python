import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from _03_sorting.sort import (
    selection_sort,
    insertion_sort,
    merge_sort,
    quick_sort
)

### Helper Function for Tests ###

def assert_sorted(arr):
    """Helper function to assert that a list is sorted."""
    assert all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

### Tests for selection_sort ###

def test_selection_sort_basic():
    """Basic test case for selection_sort."""
    arr = [3, 2, 1]
    selection_sort(arr)
    assert arr == [1, 2, 3]

def test_selection_sort_already_sorted():
    """Test case for selection_sort with an already sorted list."""
    arr = [1, 2, 3]
    selection_sort(arr)
    assert arr == [1, 2, 3]

def test_selection_sort_reverse_sorted():
    """Test case for selection_sort with a reverse sorted list."""
    arr = [3, 2, 1]
    selection_sort(arr)
    assert arr == [1, 2, 3]

def test_selection_sort_empty_list():
    """Test case for selection_sort with an empty list."""
    arr = []
    selection_sort(arr)
    assert arr == []

def test_selection_sort_single_element():
    """Test case for selection_sort with a single-element list."""
    arr = [1]
    selection_sort(arr)
    assert arr == [1]

def test_selection_sort_duplicates():
    """Test case for selection_sort with duplicate elements."""
    arr = [3, 1, 2, 3, 2, 1]
    selection_sort(arr)
    assert arr == [1, 1, 2, 2, 3, 3]

### Tests for insertion_sort ###

def test_insertion_sort_basic():
    """Basic test case for insertion_sort."""
    arr = [3, 2, 1]
    result = insertion_sort(arr)
    assert result == [1, 2, 3]
    assert_sorted(result)



### Tests for merge_sort ###

def test_merge_sort_basic():
    """Basic test case for merge_sort."""
    arr = [3, 2, 1]
    result = merge_sort(arr)
    assert result == [1, 2, 3]
    assert_sorted(result)



### Tests for quick_sort ###

def test_quick_sort_basic():
    """Basic test case for quick_sort."""
    arr = [3, 2, 1]
    result = quick_sort(arr)
    assert result == [1, 2, 3]
    assert_sorted(result)



