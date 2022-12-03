'''
You have two numbers represented by a linked list, where each node contains a single digit.
The digits are stored in reverse order, such that the first digit is at the head of the list.
write a function that adds two numbers and return sum as a linked list.
'''
from linked_list_class import LinkedList

# def returnSumLL(ll1, ll2):
#     node1 = ll1.head
#     node2 = ll2.head
#     total = 0

#     while node1 and node2:
#         total += node1.val + node2.val
#         node1.val = total % 10
#         total = total // 10

#         node1 = node1.next
#         node2 = node2.next
    
#     if total != 0:
#         ll1.addNodeEnd(total)
    
#     return ll1

# another method
def returnSumLL(ll1, ll2):
    n1 = ll1.head
    n2 = ll2.head
    total = 0
    result = LinkedList()
    while n1 or n2:
        if n1:
            total += n1.val
            n1 = n1.next
        if n2: 
            total += n2.val
            n2 = n2.next

        result.addNodeEnd(total % 10)
        total = total // 10
    return result

customll1 = LinkedList()
print(customll1.generateLL(5,0,9))
customll2 = LinkedList()
print(customll2.generateLL(3,0,9))

print(returnSumLL(customll1, customll2))