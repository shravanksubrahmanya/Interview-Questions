'''
Write a program to return n'th element from last.
n will be given
'''

from linked_list_class import LinkedList

def returnNthElem(ll,n):
    # n should be greater than 0
    currentNode = ll.head
    nthNode = ll.head
    while currentNode.next:
        currentNode = currentNode.next
        if n == 1:
            nthNode = nthNode.next
        else:
            n -= 1
    if n != 1:
        return None
    return nthNode

customLL = LinkedList()
print(customLL.generateLL(10, 1, 99))
print(returnNthElem(customLL, 3))