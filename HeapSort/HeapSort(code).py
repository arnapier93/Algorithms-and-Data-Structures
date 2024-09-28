# Lab 6 for CIS 360 -- Heap Sort

import numpy

class heap:
    keys = []           # keys indexed from 1 -> n 
    size = 0            # size can only be from 0 -> n

    def __init__(self, nums: list):
        self.keys = list(nums)     # passing nums directly causes it to be heapified when you heapify h this makes a copy to pass
        self.size = len(nums)
        self.keys.insert(0, -1)    # for a pad so index can be 1 -> n)
        

def printHeap(h: heap):
    n = h.size + 1
    depth = 0
    for i in range(1, n):
        if i == (2 ** depth):
            print("depth", depth, end=":  ")
            depth = depth + 1    
        if i == (2 ** depth) - 1:
            print(h.keys[i])
        elif i == h.size:
            print(h.keys[i])    
        else:     
            print(h.keys[i], end=", ")

def makeHeap(h: heap):          # n should be number of keys in h.keys 
    h.size = len(h.keys) - 1    # subtract 1 to account for pad
    i = h.size // 2
    while( i > 0):
        siftDown(h, i)
        i = i - 1

def heapSort(h: heap, nums: list):
    makeHeap(h)
    removeKeys(h, nums)

def siftDown(h: heap, i: int):              # to minimize the number of assignments of records                                                                                                              
    spotFound = False
    siftKey = h.keys[i]                     # siftKey is not assigned to a node until its final position is found
    parent = i

    while(2 * parent <= h.size and not spotFound):
        
        if (2 * parent < h.size and h.keys[2 * parent] < h.keys[2 * parent + 1]):
            largerChild = 2 * parent + 1    # index of right child is 1 more than twice that of parent
        else:
            largerChild = 2 * parent        # index of left chiled is twice that of parent
        
        if(siftKey < h.keys[largerChild]): 
            h.keys[parent] = h.keys[largerChild]
            parent = largerChild
        else:
            spotFound = True
    h.keys[parent] = siftKey

def getRoot(h: heap):
    root = h.keys[1]                    # get key at the root
    h.keys[1] = h.keys[h.size]          # move bottom key to root 
    h.size = h.size - 1                 # delete the bottom node
    siftDown(h, 1)                      # restore heap property
    return root

def removeKeys(h: heap, nums: list):        # nums is the unsorted array from which the heap was formed
    i = h.size
    while(i >= 1):
        nums[i-1] = getRoot(h)
        i = i - 1


# 1 impliment the linear-time makeheap algorithm: read n unsorted number and create a heap (stored as an array) to store these n number

nums1 = []                                           # unsorted array
n1 = 100
for i in range(n1): 
    nums1.append(numpy.random.randint(0,101))        # 100 random numbers 0-100
 
h1 = heap(nums1)                                     # not yet heapified
makeHeap(h1)
printHeap(h1)

# 2 implement the Heapsort algorithm with 2 test cases n = 200 and n = 500

nums2 = []
n2 = 200
for j in range(n2): 
    nums2.append(numpy.random.randint(0,101))        # 200 random numbers 0-100

h2 = heap(nums2)                                   
heapSort(h2, nums2)
print(nums2)

nums5 = []
n5 = 500
for k in range(n5): 
    nums5.append(numpy.random.randint(0,101))        # 500 random numbers 0-100

h5 = heap(nums5)                                   
heapSort(h5, nums5)
print(nums5)

