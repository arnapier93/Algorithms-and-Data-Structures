# Lab 8 for CIS-360
# Explores 3 different quick sort algorithms and compares them among different sized data sets

count = 0

def swap(nums: list[int], a: int, b: int):
    c = nums[a]
    nums[a] = nums[b]
    nums[b] = c

# uses leftmost item as pivot point
def partition1(low: int, high: int, nums: list[int]):
    pivotPoint = nums[low]    # set pivotPoint to leftmost item in array
    i = low + 1                # i and j are indexes
    j = high
    
    while i < j:
        while i < high and nums[i] <= pivotPoint:
            i += 1
        while j > low and nums[j] >= pivotPoint:
            j -= 1
        if i < j:
            swap(nums, i, j)

    if i > j:                   # adjust i to its previous position: the end of the sub-array
        i -= 1
    
    if nums[low] > nums[i]:   # swap pivot with the last element in the left sub-array
        swap(nums, low, i)
    
    pivotPoint = i
    
    return pivotPoint

# uses median of 3 as pivot point
def partition2(low: int, high: int, nums: list[int]):
    middle = (low + high) // 2
    p_points = [nums[low], nums[middle], nums[high]]
    p_points.sort()
    median = p_points[1]

    pivotPoint = median    # set pivotPoint to the111
    i = low + 1                # i and j are indexes
    j = high
    
    while i < j:
        while i < high and nums[i] <= pivotPoint:
            i += 1
        while j > low and nums[j] >= pivotPoint:
            j -= 1
        if i < j:
            swap(nums, i, j)

    if i > j:                   # adjust i to its previous position: the end of the sub-array
        i -= 1
    
    if nums[low] > nums[i]:   # swap pivot with the last element in the left sub-array
        swap(nums, low, i)
    
    pivotPoint = i
    
    return pivotPoint


class quickSorter:

    def __init__(self):
        self.counter = 0

    # quicksort for part 1
    def quickSort1(self, low: int, high: int, nums: list):
        self.counter += 1
        if high > low:
            pivotpoint = partition1(low, high, nums)
            self.quickSort1(low, (pivotpoint - 1), nums)
            self.quickSort1(pivotpoint + 1, high, nums)   


    # quickSort for part 2
    def quickSort2(self, low: int, high: int, nums: list):
        self.counter += 1
        if high > low:
            pivotpoint = partition2(low, high, nums)
            self.quickSort2(low, (pivotpoint - 1), nums)
            self.quickSort2(pivotpoint + 1, high, nums)   


    # quickSort for part 3:
    def quickSort3(self, low: int, high: int, nums: list):
        self.counter += 1
        if high > low:
            pivotpoint = partition2(low, high, nums)
            if ((pivotpoint - 1) - low) < 10:
                self.insertionSort(low, (pivotpoint - 1), nums)
            else:
                self.quickSort3(low, (pivotpoint - 1), nums)
            
            if high - (pivotpoint + 1) < 10:
                self.insertionSort((pivotpoint + 1), high, nums)
            else:
                self.quickSort3((pivotpoint + 1), high, nums)

    # for sorting arrays with len < 10
    # kept within object to keep count going
    def insertionSort(self, low: int, high: int, nums: list):
        self.counter += 1
        i = low + 1
        for index in range(i, (high + 1)):
            x = nums[i]        
            j = i - 1
            while j > 0 and nums[j] > x:
                nums[j + 1] = nums[j]
                j -= 1
            nums[j + 1] = x




import numpy

# PART 1
print("Part 1:")
n100 = numpy.random.randint(1000, size=100).tolist()
n5k = numpy.random.randint(1000, size=5000).tolist()
n50k = numpy.random.randint(1000, size=50000).tolist()
n100k = numpy.random.randint(1000, size=100000).tolist()

qs = quickSorter()

qs.counter = 0
qs.quickSort1(low= 0, high= 99, nums= n100)
print("List sorted in", qs.counter, "iterations.")

qs.counter = 0
qs.quickSort1(low= 0, high= 4999, nums= n5k)
print("List sorted in", qs.counter, "iterations.")

qs.counter = 0
qs.quickSort1(low= 0, high= 49999, nums= n50k)
print("List sorted in", qs.counter, "iterations.")

qs.counter = 0
qs.quickSort1(low= 0, high= 99999, nums= n100k)
print("List sorted in", qs.counter, "iterations.")


# PART 2
print("Part 2:")
n100 = numpy.random.randint(1000, size=100).tolist()
n5k = numpy.random.randint(1000, size=5000).tolist()
n50k = numpy.random.randint(1000, size=50000).tolist()
n100k = numpy.random.randint(1000, size=100000).tolist()


qs.counter = 0
qs.quickSort2(low= 0, high= 99, nums= n100)
print("List sorted in", qs.counter, "iterations.")

qs.counter = 0
qs.quickSort2(low= 0, high= 4999, nums= n5k)
print("List sorted in", qs.counter, "iterations.")

qs.counter = 0
qs.quickSort2(low= 0, high= 49999, nums= n50k)
print("List sorted in", qs.counter, "iterations.")

qs.counter = 0
qs.quickSort2(low= 0, high= 99999, nums= n100k)
print("List sorted in", qs.counter, "iterations.")


# PART 3
print("Part 3:")
n100 = numpy.random.randint(1000, size=100).tolist()
n5k = numpy.random.randint(1000, size=5000).tolist()
n50k = numpy.random.randint(1000, size=50000).tolist()
n100k = numpy.random.randint(1000, size=100000).tolist()


qs.counter = 0
qs.quickSort3(low= 0, high= 99, nums= n100)
print("List sorted in", qs.counter, "iterations.")

qs.counter = 0
qs.quickSort3(low= 0, high= 4999, nums= n5k)
print("List sorted in", qs.counter, "iterations.")

qs.counter = 0
qs.quickSort3(low= 0, high= 49999, nums= n50k)
print("List sorted in", qs.counter, "iterations.")

qs.counter = 0
qs.quickSort3(low= 0, high= 99999, nums= n100k)
print("List sorted in", qs.counter, "iterations.")