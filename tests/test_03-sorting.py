import pytest
from python._3_sorting.sort import recursive_selection_sort, selection_sort, insertion_sort, merge_sort, quick_sort

# Test data
unsorted_list = [5, 3, 8, 6, 2, 7, 1, 4]
sorted_list = [1, 2, 3, 4, 5, 6, 7, 8]

def test_recursive_selection_sort():
    # Make a copy of unsorted_list to preserve the original
    arr = unsorted_list.copy()
    recursive_selection_sort(arr)
    assert arr == sorted_list

def test_selection_sort():
    # Make a copy of unsorted_list to preserve the original
    arr = unsorted_list.copy()
    selection_sort(arr)
    assert arr == sorted_list

def test_insertion_sort():
    # Make a copy of unsorted_list to preserve the original
    arr = unsorted_list.copy()
    result = insertion_sort(arr)
    assert result == sorted_list

def test_merge_sort():
    # Make a copy of unsorted_list to preserve the original
    arr = unsorted_list.copy()
    result = merge_sort(arr)
    assert result == sorted_list

def test_quick_sort():
    # Make a copy of unsorted_list to preserve the original
    arr = unsorted_list.copy()
    result = quick_sort(arr)
    assert result == sorted_list