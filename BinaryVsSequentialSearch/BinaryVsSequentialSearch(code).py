# Press Shift+F10 to execute

# Lab 1 for CIS360 - Andrew Napier - Sequential Search vs. Binary Search

import numpy


class SearchResults:    # stores results of seq_search and bin_search
    count = 0           # number of iterations to find result
    index = 0           # index of the found search num in the array
    found = False       # bool to report a failure to find the search num


def seq_search(num, array_of_nums):     # sequential search algorithm
    results = SearchResults()
    for x in array_of_nums:
        results.count = results.count + 1
        if num == x:
            results.found = True
        else:
            results.index = results.index + 1
        if results.found:
            return results  # breaks loop when num is found
    return results  # returns results for failure too check with results.found


def bin_search(num, array_of_nums):     # binary search algorithm
    array_of_nums = numpy.sort(array_of_nums)     # sorts the array
    results = SearchResults()
    high = array_of_nums.size
    low = 0
    mid = round((high + low) / 2)
    count = 1
    while num != array_of_nums[mid]:
        count = count + 1
        if num < array_of_nums[mid]:
            high = mid
            mid = round((high + low) / 2)
        elif num > array_of_nums[mid]:
            low = mid
            mid = round((high + low) / 2)
        elif high == low:           # failure state nowhere left to search
            return results
    if num == array_of_nums[mid]:   # double checks success
        results.index = mid
        results.count = count
        results.found = True
        return results
    else:                           # should never get here something went wrong
        print("bin_search ERROR")
        return results


array_sizes = [1000, 100000, 1000000]   # the 3 sizes given

for y in array_sizes:

    s_array = numpy.random.randint(1, y, y)     # creates array of random integers from 1 - y to search
    key = numpy.random.randint(1, y)            # chooses 1 random integer from 1 - y to find in the array

    # first sequential search is performed and results are reported
    seq_searching = True  # end searching when results.found == True
    while seq_searching:
        seq_results = seq_search(key, s_array)
        if not seq_results.found:               # in case of failure on seq_search it just chooses a new key
            key = numpy.random.randint(1, y)
        else:
            print("The key, ", key, ", was found at location ", seq_results.index)
            print("It took ", seq_results.count, " iterations to find using sequential search.\n")
            seq_searching = False               # results.found must be True so searching ends

    # then binary search is performed with the same key and same array for proper comparisons
    bin_searching = True        # end searching when results.found == True
    while bin_searching:
        bin_results = bin_search(key, s_array)
        if not bin_results.found:   # should never get here
            print("bin_search ERROR: Key has been confirmed to be in the array by seq_search")
        else:
            print("The key, ", key, ", was found at location ", bin_results.index, )
            print("It took ", bin_results.count, " iterations to find using binary search.\n")
            bin_searching = False
