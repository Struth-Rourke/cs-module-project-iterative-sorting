# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        # setting cur_index
        cur_index = i
        # setting smallest_index equal to the cur_index
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here

        # loop through the elements in the list
        for j in range(cur_index + 1, len(arr)):
            # if the element is < the current smallest
            if arr[j] < arr[smallest_index]:
                # set the smallest index value equal to j
                smallest_index = j
                # print(arr)

        # swap the minimum with the current position
        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]

        ## ALT Code:
        # # tracker value for an element in the array
        # smallest_value = arr[i]
        # # for a value in the length of the array, that is len(arr) - 1
        # # ** referencing the index
        # for j in range(i, len(arr)):
        #     # if that value is less than the smallest
        #     if arr[j] < smallest_value:
        #         # set the smallest_index equal to j
        #         smallest_index = j
        #         # set the smallest_value equal to the array value
        #         smallest_value = arr[j]

        # # TO-DO: swap
        # # Your code here
        # # temp tracker variable
        # temp = arr[cur_index]
        # # set the cur_index equal to the smallest_index
        # arr[cur_index] = arr[smallest_index]
        # # set the smallest_index equal to the temp
        # arr[smallest_index] = temp

    return arr


## CHECK TEST:
# arr = [1,7,3,8,4,2,9,6,10,5]
# print(selection_sort(arr))


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Set swap variable
    swapped = True
    # while swapped = True
    while swapped:
        # are the elements swapped?
        swapped = False
        # loop through n-1 elements (last element has nothing to it's right)
        for i in range(0, len(arr) - 1):
            # set element positions (left)
            left = i
            # set element positions (right)
            right = i + 1
            # if left > right
            if arr[left] > arr[right]:
                # swap positions
                arr[left], arr[right] = arr[right], arr[left]
                # set swapped equal to True to reiterate through the list
                swapped = True

    # ## ALT Code:
    # # Your code here
    # # loop through n-1 elements
    # for i in range(0, len(arr) - 1):
    #     # elements in ((n-1) - (n+1))
    #     for j in range(0, len(arr) - (i + 1)):
    #         # if the element indexed higher in the list is lower than the
    #         # current element value in the list
    #         if arr[j] > arr[j + 1]:
    #             # set a temp variable to the array value j
    #             temp = arr[j]
    #             # set the array value j as equal to the value that was indexed higher
    #             arr[j] = arr[j + 1]
    #             # and set the indexed higher value as the temo 
    #             arr[j + 1] = temp

    return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''

def counting_sort(arr, maximum=None):
    # if the max is None
    if maximum is None:
        # set maximum as 0
        maximum = 0
        # loop through the array
        for i in range(0, len(arr)):
            # if the value in the array is greater than max
            if arr[i] > maximum:
                # set max as equal to the value in the array
                maximum = arr[i]
    
    # else: 
    # buckets are equal to the value at the first index multiplied by one
    # more than the maximum
    buckets = [0] * (maximum + 1)
    # instantiate a sortedIndex
    sortedIndex = 0
    
    # for an element in the array
    for i in range(0, len(arr)):
        # check if element is negative
        if arr[i] < int(0):
            # print
            print("Error, negative numbers not allowed in Count Sort")
        
        else:
            # buckets += 1 for each corresponding element in this array
            buckets[arr[i]] += 1

    # for a particular bucket in buckets
    for j in range(0, len(buckets)):
        # while the bucket value is greater than 0
        while buckets[j] > 0:
            # the sortedIndex of arr equals 1
            arr[sortedIndex] = j
            # add sortedIndex
            sortedIndex += 1
            # subtract from the specific bucket
            buckets[i] -= 1
    
    return arr
