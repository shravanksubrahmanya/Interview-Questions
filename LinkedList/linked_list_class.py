from random import randint

class Node:
    def __init__(self, val = None):
        self.prev = None
        self.val = val
        self.next = None
    
    def __str__(self):
        return str(self.val)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.nodeCount = 0

    # overriding builtin iterator  function
    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next

    # overriding builtin string method
    def __str__(self):
        values = [str(n.val) for n in self]
        return ' -> '.join(values)
    
    # overriding length function
    def __len__(self):
        return self.nodeCount

    
    # add element at end of the linked list
    def addNodeEnd(self, val):
        newNode = Node(val)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.nodeCount += 1
        return self.tail

    # generating a linked list based on random numbers
    def generateLL(self, n, minval, maxval):
        self.head = None
        self.tail = None
        for i in range(n):
            self.addNodeEnd(randint(minval, maxval))
        return self

# customLL = LinkedList()
# customLL.generateLL(10, 0, 99)
# print(customLL)


