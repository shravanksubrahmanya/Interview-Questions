'''
This program demonstrates the following problem.
Write a code to remove duplicate elements from unsorted linked list.
'''

from linked_list_class import LinkedList

def removeDuplicate(ll):
    visited = set()
    if ll.head is not None:
        currentNode = ll.head
        visited.add(currentNode.val)
        while currentNode.next:
            if currentNode.next.val in visited:
                currentNode = currentNode.next.next
            else:
                visited.add(currentNode.next.val)
                currentNode = currentNode.next
    return ll

customLL = LinkedList()
print(customLL.generateLL(10,0,99))
print(removeDuplicate(customLL))
