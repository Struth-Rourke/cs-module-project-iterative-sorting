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
    ## v1
    # if maximum is None:
    #     maximum = 0
    #     for i in range(0, len(arr)):
    #         if arr[i] > maximum:
    #             maximum = arr[i]
    
    # buckets = [0] * (maximum + 1)
    # sortedIndex = 0

    # for i in range(0, len(arr)):
    #     if arr[i] > 0:
    #         buckets[arr[i]] += 1
    #     else: 
    #         print("Error, negative numbers not allowed in Count Sort")
    
    # for i in range(0, len(buckets)):
    #     while (buckets[i] > 0):
    #         arr[sortedIndex] = i
    #         sortedIndex += 1
    #         buckets[i] -= 1

    # ## v2
    # m = maximum + 1
    # # instantiate counter
    # count = [0] * m

    # # for an element in the array
    # for e in arr:
    #     # add count of occurences
    #     count[e] += 1
    
    # # instantiate index
    # index = 0
    # # for element in m
    # for e in range(m):
    #     # for i in the count of e
    #     for i in range(count[e]):
    #         # set the value as the element e
    #         arr[i] = e
    #         # add to index
    #         index[m] += 1

    ## v3
    # if there is no array
    if not arr:
        # return array
        return arr
    # if any value in the array is negative
    if any(x < 0 for x in arr):
        # return error message
        return "Error, negative numbers not allowed in Count Sort"
    # else instantiate an array of 0s whose length is the max value + 1
    # (+1 because we start the count at 0)
    else:
        buckets = [0] * (max(arr) + 1)
    # loop through the items in the array
    for i in range(len(arr)):
        # count array to store the count of each unique object
        buckets[i] += 1
        # Modify the count array such that each element at each index 
        # stores the sum of previous counts (keeping a running count)
        buckets[i] += buckets[i - 1]
        # Output each object from the input sequence followed by 
        # decreasing its count by 1
        arr[i] = buckets[i] - 1

    return arr
