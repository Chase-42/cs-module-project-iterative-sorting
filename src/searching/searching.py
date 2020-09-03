def linear_search(arr, target):
    # Your code here
    for i in range(0, len(arr)):
        if arr[i] == target: 
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    if len(arr) == 0: 
        return -1

    left = 0 
    right = len(arr)
    while left <= right: 
        middle = int(left + (right - 1) / 2)
        if arr[middle] == target: 
            return middle 
        elif arr[middle] < target: 
            left = middle + 1
        else: 
            right = middle - 1

    return -1  # not found
