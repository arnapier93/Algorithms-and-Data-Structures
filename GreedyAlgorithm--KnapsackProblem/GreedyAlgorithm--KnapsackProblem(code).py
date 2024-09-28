# CIS-360 -- Lab 10 -- Greedy Algorithm / "Knapsack Problem"

import numpy


class item:

    def __init__(self, n: int, w: int, p: int):
        self.num = n
        self.weight = w
        self.profit = p
        self.ratio = p/w
        print("Item #", n, " Weight= ", w, " Profit= ", p, " Ratio = ", p/w, sep= "")
    
    
class knapsack:

    def __init__(self, weightLimit: int):   # initializes knapsack with a specified max fill weight
        self.contents = []                  # empty list for items
        self.weight = 0                     # total weight of all items in knapsack
        self.profit = 0                     # total potential profit for selling all items in knapsack 
        self.maxFill = weightLimit          # total weight the knapsack can hold

    def add_to(self, i: item):              # places a specified item into the knapsack
        self.contents.append(i)
        self.weight += i.weight
        self.profit += i.profit

    def print_contents(self):               # specially formatted print for the knapsack
        n = len(self.contents)
        print("Items in knapsack:", end= " ")          
        for i in range(n):
            if i != n-1:
                print(self.contents[i].num, end= ", ")
            else:
                print(self.contents[i].num)
        print("Total profits =", self.profit)
        print("Total weight =", self.weight, "out of a max weight of:", self.maxFill)


def greedyPack(k: knapsack, items: list):   # adds items with the highest p/w ratio in order of whichever it finds first  
                                            # does not take into account the final highest p/w ratio just adds whichever item has the highest until full
    while len(items) > 0:
        itemToAdd = items[0]
        j = 0
        for j in range(len(items)):
            if items[j].ratio > itemToAdd.ratio:
                itemToAdd = items[j]
        if k.weight + itemToAdd.weight > k.maxFill:         # empties list of all items regardless of wether they are being added to the knapsack
            items.remove(itemToAdd)                         # this ensures small items with bad ratios that still fit in the knapsac get added
        else:                                               # the bigger items with better ratios won't fit so they're just removed
            items.remove(itemToAdd)                         # the items being added also have to be removed as to not add them over and over again
            k.add_to(itemToAdd)        


items1 = []
items2 = []
items3 = []

# arbitrarily decided max weights for 3 different knapsacks, increasing based on size of items list
k1 = knapsack(15)
k2 = knapsack(25)
k3 = knapsack(50)

# fills the 3 items lists from above with items
# each item has weight 1-15 and potential profit 1-15
n1 = 10
for i in range(n1): 
    items1.append(item(i + 1, numpy.random.randint(1,16), numpy.random.randint(1,16)))
n2 = 50
for i in range(n2): 
    items2.append(item(i + 1, numpy.random.randint(1,16), numpy.random.randint(1,16))) 
n3 = 100
for i in range(n3): 
    items3.append(item(i + 1, numpy.random.randint(1,16), numpy.random.randint(1,16))) 


# Filling and printing knapsack 1
greedyPack(k1, items1)
print("-- Knapsack 1 Contents --")
k1.print_contents() 


# Filling and printing knapsack 2
greedyPack(k2, items2)
print("\n-- Knapsack 2 Contents --")
k2.print_contents() 

# Filling and printing knapsack 3
greedyPack(k3, items3)
print("\n-- Knapsack 3 Contents --")
k3.print_contents() 