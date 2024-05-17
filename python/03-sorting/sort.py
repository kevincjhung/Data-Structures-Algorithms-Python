testArray = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 1, 2, 3, 4, 5, 6, 7]

def selection_sort(A, i=None):
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



print(testArray)
selection_sort(testArray)
print(testArray)
