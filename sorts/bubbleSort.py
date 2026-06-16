"""
    This file implements Bubble sort algorithm.
    Author: Shatroopa Saxena
"""
# User defined functions
def bubbleSort(nums):
    """
        This function sorts the given array of numbers in place using Bubble Sorting Algorithm implemented iteratively.
        Time Complexity: O(n^2)
        Space Complexity: O(1)

        @param nums                 [List] Given array of numbers

        @returnValue nums           [List] Sorted nums
    """

    n = len(nums)

    for i in range(n-1):
        swapped = False
        for j in range(n-1-i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                swapped = True
        
        if not swapped:                 # Avoid unnecessary iterations once the array is sorted.
            break

    return nums


def bubbleSortRecursive(nums):
    """
        This function sorts the given array of numbers in place using Bubble Sorting Algorithm implemented recursively.
        Time Complexity: O(n^2)
        Space Complexity: O(1)

        @param nums                 [List] Given array of numbers

        @returnValue nums           [List] Sorted nums
    """

    n = len(nums)
    if n == 1:
        return nums
    
    for i in range(n-1):
        if nums[i] > nums[i+1]:
            nums[i], nums[i+1] = nums[i+1], nums[i]
    
    nums[:n-1] = bubbleSortRecursive(nums[:n-1])
    return nums


if __name__ == '__main__':
    nums = [float(n) for n in input("Enter numbers you want to sort separated a space: ").split()]
    # sorted_nums = bubbleSort(nums)
    sorted_nums = bubbleSortRecursive(nums)
    print(f"Sorted numbers are: {sorted_nums}")

    print("\nDone.\n")