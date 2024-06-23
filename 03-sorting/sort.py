def recursives_selection_sort(A, i=None):
    # If 'i' is not provided, set it to the last index of the array A
    if i is None:
        i = len(A) - 1
    
    # Base case: If i is greater than 0, continue sorting
    if i > 0:
        # Find the index of the maximum element in the subarray A[0:i]
        j = prefix_max(A, i)
        # Swap the maximum element with the element at index i
        A[i], A[j] = A[j], A[i]
        # Recursively call selection_sort on the subarray A[0:i-1]
        selection_sort(A, i - 1)

# Helper function for recursive_selection_sort
def prefix_max(A, i):
    # Base case: If i is greater than 0, find the maximum element in A[0:i]
    if i > 0:
        # Recursively find the index of the maximum element in A[0:i-1]
        j = prefix_max(A, i - 1)
        # Compare the current element A[i] with the maximum found in A[0:i-1]
        if A[i] < A[j]:
            # If A[j] is greater, return j
            return j
    # If A[i] is greater or equal, or if i == 0, return i
    return i


def selection_sort(A):
    n = len(A)

    # find the smallest element
    for i in range(n-1): # Assume min is first element
        min_index = i

        for j in range(i + 1, n):
            if A[j] < A[min_index]:
                min_index = j
        
        if min_index != i:
            A[i], A[min_index] = A[min_index], A[i] 

"""
    Sorts a list in ascending order using the insertion sort algorithm.

    Parameters:
    arr (list): The list to be sorted.

    Returns:
    list: The sorted list.
"""
def insertion_sort(arr):
    # Iterate over the list starting from the second element
    for i in range(1, len(arr)):
        key = arr[i]  # Current element to be inserted
        j = i - 1     # Index of the previous element

        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # Insert the key into its correct position
        arr[j + 1] = key

    return arr


# Helper function for merge sort
def merge(arr1, arr2):
    result_array = []

    while arr1 and arr2:
        if arr1[0] <= arr2[0]:
            result_array.append(arr1.pop(0))  # Use pop(0) to remove the first element
        else: 
            result_array.append(arr2.pop(0))  # Use pop(0) to remove the first element
    
    # Extend the result_array with the remaining elements of arr1 and arr2
    result_array.extend(arr1)
    result_array.extend(arr2)

    return result_array


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    middle_index = len(arr) // 2

    # Recursively call merge_sort on the left and right halves of the array
    left_half = merge_sort(arr[:middle_index])
    right_half = merge_sort(arr[middle_index:])

    # Merge the sorted left and right halves
    return merge(left_half, right_half)



def quick_sort(array, low_index=0, high_index=None):
    if high_index is None:
        high_index = len(array) - 1
    if low_index < high_index:
        # Partition the array and get the pivot index
        pivot_index = partition(array, low_index, high_index)

        # Recursively sort elements before and after partition
        quick_sort(array, low_index, pivot_index - 1)
        quick_sort(array, pivot_index + 1, high_index)
    return array


def partition(array, low_index, high_index):
    # Choose the pivot as the last element of the array segment
    pivot = array[high_index]
    i = low_index - 1  # Index of smaller element

    for j in range(low_index, high_index):
        # If the current element is smaller than or equal to the pivot
        if array[j] <= pivot:
            i += 1
            # Swap array[i] and array[j]
            array[i], array[j] = array[j], array[i]

    # Swap array[i + 1] and array[high_index] (or pivot)
    array[i + 1], array[high_index] = array[high_index], array[i + 1]
    return i + 1


