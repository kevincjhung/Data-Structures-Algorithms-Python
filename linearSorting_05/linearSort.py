from typing import List

def counting_sort(arr: List[int]) -> List[int]:
    """
    Counting Sort Algorithm

    :param arr: List of integers to be sorted
    :return: Sorted list of integers
    """
    if not arr:
        return []

    # Find the maximum and minimum values in the array
    max_val = max(arr)
    min_val = min(arr)

    # Create a count array to store the count of each unique number
    count_array = [0] * (max_val - min_val + 1)

    # Count the occurrences of each number
    for num in arr:
        count_array[num - min_val] += 1

    # Build the sorted array
    sorted_index = 0
    for i in range(len(count_array)):
        while count_array[i] > 0:
            arr[sorted_index] = i + min_val
            sorted_index += 1
            count_array[i] -= 1

    return arr

from typing import List

def get_digit(num: int, place: int) -> int:
    """
    Get the digit at a specific place value

    :param num: The number from which to extract the digit
    :param place: The place value (0 for units, 1 for tens, etc.)
    :return: The digit at the specified place value
    """
    return abs(num) // (10 ** place) % 10

def digit_count(num: int) -> int:
    """
    Count the number of digits in a number

    :param num: The number to count digits
    :return: The number of digits in the number
    """
    if num == 0:
        return 1
    return len(str(abs(num)))

def most_digits(nums: List[int]) -> int:
    """
    Find the maximum number of digits in an array of numbers

    :param nums: The array of numbers
    :return: The maximum number of digits found in the array
    """
    max_digits = 0
    for num in nums:
        max_digits = max(max_digits, digit_count(num))
    return max_digits

def radix_sort(nums: List[int]) -> List[int]:
    """
    Radix Sort Algorithm

    :param nums: List of integers to be sorted
    :return: Sorted list of integers
    """
    max_digit_count = most_digits(nums)

    # Loop through each digit place (units, tens, hundreds, etc.)
    for k in range(max_digit_count):
        # Create buckets for each digit (0 to 9)
        digit_buckets = [[] for _ in range(10)]

        # Place each number in the corresponding bucket based on the current digit
        for num in nums:
            digit = get_digit(num, k)
            digit_buckets[digit].append(num)

        # Flatten the buckets back into the array
        nums = [num for bucket in digit_buckets for num in bucket]

    return nums

# Example usage
arr2 = [170, 45, 75, 90, 802, 24, 2, 66]
print(radix_sort(arr2))  # Output: [2, 24, 45, 66, 75, 90, 170, 802]


# Example usage
arr1 = [4, 2, 2, 8, 3, 3, 1]
print(counting_sort(arr1))  # Output: [1, 2, 2, 3, 3, 4, 8]
