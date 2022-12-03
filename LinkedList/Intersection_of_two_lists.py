'''
Given two singly linked lists, determine if the two lists intersect. Return the intersecting 
node. Note that intersection is defined based on the reference, not value. that is if k'th 
node of the first linked list is the exact same node (by reference) as the j'th node of the
second linked list, then they are intersecting.
'''
from linked_list_class import LinkedList

def intersectionLL(llA, llB):
    if llA.tail is not llB.tail:
        return None
    lenA = len(llA)
    lenB = len(llB)

    node1 = llA.head
    node2 = llB.head

    if lenA > lenB:
        for i in range(lenA-lenB):
            node1 = node1.next
    elif lenA < lenB:
        for i in range(lenB-lenA):
            node2 = node2.next
            
    while node1 is not node2:
        node1 = node1.next
        node2 = node2.next
    return node1

# second method
# def intersectionLL(llA, llB):
#     if llA.tail is not llB.tail:
#         return None
    
#     lenA = len(llA)
#     lenB = len(llB)

#     shorter = llB if lenA > lenB else llA
#     longer = llA if lenA < lenB else llB

#     shorter = shorter.head
#     longer = longer.head
#     for i in range(abs(lenA - lenB)):
#         longer = longer.next
#     print(longer.val)
#     while shorter is not longer:
#         shorter = shorter.next
#         longer = longer.next
#     return shorter

customlist1 = LinkedList()
customlist1.generateLL(5,0,9)
customlist2 = LinkedList()
customlist2.generateLL(3,0,9)
customlist3 = LinkedList()
customlist3.generateLL(4,0,9)

customlist1.tail.next = customlist3.head
customlist1.tail = customlist3.tail
customlist2.tail.next = customlist3.head
customlist2.tail = customlist3.tail

print(customlist1)
print(customlist2)
print(intersectionLL(customlist1, customlist2))

