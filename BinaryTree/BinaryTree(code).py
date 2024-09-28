# Lab 5 for CIS 360 -- Binary Trees
# Uses a binary tree to find the numbers in an array that fall within a certain range i.e. 100-250

import numpy

class BinaryNode:                   
    # for use in binary tree 

    def __init__(self, value: int):     # creates new root node
        self.value = value
        self.parent = None
        self.left = None
        self.right = None
        self.subSize = 1                # size of the subtree at that root

    def hasLeft(self):              # verifies existance of left child
        result = False
        if self.left is not None:
            result = True
        return result
                 
    def hasRight(self):             # verifies existance of right child
        result = False
        if self.right is not None:
            result = True
        return result                 

    def depth(self):
        depth = 0                       # root node is at depth 0 but height 1
        node = self
        while node.parent is not None:
            node = node.parent
            depth = depth + 1
        return depth    


def addLeft(c: BinaryNode, p: BinaryNode):           # adds new left child
    p.left = c
    #p.subSize += 1
    c.parent = p


def addRight(c: BinaryNode, p: BinaryNode):           # adds new right child
    p.right = c
    #p.subSize += 1
    c.parent = p


def addToTree(child: BinaryNode, parent: BinaryNode):       # adds the node to the tree in proper order under the parent node
    parent.subSize += 1
    if parent.left is None and child.value <= parent.value:
        addLeft(child, parent)
        child.parent = parent
    elif parent.right is None and child.value > parent.value:
        addRight(child, parent)
        child.parent = parent
    elif child.value <= parent.value:  
        addToTree(child, parent.left)
    elif child.value > parent.value:   
        addToTree(child, parent.right)


def printTree(root: BinaryNode):
    node = root
    if node.hasLeft() and node.hasRight():
        print(node.value, " (", node.left.value, ", ", node.right.value, ")", sep="", end="; ")
        printTree(node.left)
        printTree(node.right)
    elif node.left is None and node.right is None:
        print(node.value, "(e, e)", end= "; ")
    elif node.left is None:
        print(node.value, "(e, ", node.right.value, ")", sep ="", end="; ")
        printTree(node.right)
    elif node.right is None:
        print(node.value, " (", node.left.value, ", e)",  sep="", end="; ")
        printTree(node.left)


def getNodes(root: BinaryNode, nodes: list):
    node = root
    if node.hasLeft() and node.hasRight():
        nodes.append(node)
        getNodes(node.left, nodes)
        getNodes(node.right, nodes)
    elif node.left is None and node.right is None:
        nodes.append(node)
    elif node.left is None:
        nodes.append(node)
        getNodes(node.right, nodes)
    elif node.right is None:
        nodes.append(node)
        getNodes(node.left, nodes)


def select(index: int, root: BinaryNode):
    # searches the tree or subtree from root for a node of given index and returns it
    if index == 1 and not root.hasLeft():
        return root.value
    elif root.hasLeft():
        size = root.left.subSize
        if index == size + 1:
            return root.value
        elif index > size and root.hasRight():
            index -= size   # accounts fot the left subtree
            index -= 1      # accounts for the root
            return select(index, root.right)
        elif index <= size:
            return select(index, root.left)        # while moving left the index doesnt change
    elif root.hasRight():
        index -= 1          # accounts for the root
        return select(index, root.right)


def rangeQuery(min: int, max: int, n: BinaryNode, inRange: list):
    key = n.value
    if min <= key and key <= max:   
        inRange.append(n)
        if n.hasLeft() and n.hasRight():
            rangeQuery(min, max, n.left, inRange)
            rangeQuery(min, max, n.right, inRange)
        elif n.hasRight():
            rangeQuery(min, max, n.right, inRange)
        elif n.hasLeft():
            rangeQuery(min, max, n.left, inRange)
    elif key < min and n.hasRight():
        rangeQuery(min, max, n.right, inRange)
    elif key > max and n.hasLeft():
        rangeQuery(min, max, n.left, inRange)


def getHeight(leaves: list[BinaryNode]):
    height = 1
    for leaf in leaves:    
        h = leaf.depth() + 1
        if h > height:
            height = h
    return height

    
leaves = []                                     # empty list for nodes other than root
n = 19                                          # total number of nodes - 1 for root

root = BinaryNode(numpy.random.randint(0, 1000))  
print ("root =", root.value)
print("number of nodes =", n + 1)

print("nodes =", end=" ")
print("[", root.value, sep="", end=", ")
for l in range(n):
    node = BinaryNode(numpy.random.randint(0, 1000))     # fills leaves[] with random values        
    leaves.append(node)                                # prints neatly as it's being filled
    if l == n-1:
        print(node.value, "]", sep="", end="\n\n")
    else:
        print(node.value, end=", ")
for node in leaves:                                     
    addToTree(node, root)

print("Tree:", end=" ")
printTree(root)
print("")

height = getHeight(leaves)                                   
print("")
print("Height: ", height)

nodesInRange = []                                           # passes an empty list to be filled in the rangequery()
min = 100; max = 250
rangeQuery(min, max, root, nodesInRange) 
values = []

for node in nodesInRange:
    values.append(node.value)

print("All nodes in range, 100-250:", values)

i = 7
ith = select(i, root)

print(ith, " is the ", i, "th node.", sep="")