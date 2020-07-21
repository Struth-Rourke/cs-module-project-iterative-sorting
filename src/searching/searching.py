def linear_search(arr, target):
    # for value in the len(arr)
    for i in range(0, len(arr)):
        # if the value equals the target
        if arr[i] == target:
            # return the index value
            return i

    # # ALT Code:
    # for index, j in enumerate(arr):
    #     if j == target:
    #         return index

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # Your code here
    # setting lowest element index
    low_idx = 0
    # setting highest element index
    high_idx = len(arr) - 1
    # while the low_idx is less than the high_one
    while low_idx < high_idx:
        # find the mid_idx
        mid_idx = int((low_idx + high_idx) / 2)
        # if the value is equal to the target
        if arr[mid_idx] == target:
            # return the index
            return mid_idx
        # if the value is too low
        if arr[mid_idx] < target:
            # equate the low_idx and the mid_idx so that you can search the lower
            # half of the distribution
            low_idx = mid_idx
        # else the value is too high
        else:
            # equate the high_idx and the mid_idx so that you can search the upper
            # half of the distribution
            high_idx = mid_idx

    return -1  # not found
