'''
Write a program to partition the linked list around a given value x such that all the nodes 
whose values less than the given value x comes before all nodes greater or equal to x
'''

from linked_list_class import LinkedList

def partition(ll, x):
    currentNode = ll.head
    ll.tail = ll.head

    while currentNode:
        nextNode = currentNode.next
        currentNode.next = None
        if currentNode.val < x:
            currentNode.next = ll.head
            ll.head = currentNode
        else:
            ll.tail.next = currentNode
            ll.tail = currentNode
        currentNode = nextNode
    
    if ll.tail.next is not None:
        ll.tail.next = None

customLL = LinkedList()
print(customLL.generateLL(10,1,99))
partition(customLL, 40)
print(customLL)