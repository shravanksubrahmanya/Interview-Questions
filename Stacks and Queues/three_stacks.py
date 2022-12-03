'''
Write a pythoj program to implement three stacks in a single list
'''

class MultiStack:
    def __init__(self, stackSize) -> None:
        self.numberOfStacks = 3
        self.custList = [0] * (stackSize * self.numberOfStacks)
        self.sizes = [-1] * self.numberOfStacks
        self.stackSize = stackSize
    
    def isFull(self, stackNumber):
        return self.sizes[stackNumber-1] == self.stackSize - 1
    
    def isEmpty(self, stackNumber):
        return self.sizes[stackNumber-1] == -1
    
    def peekIndex(self, stackNumber):
        offset = (stackNumber - 1) * self.stackSize
        index = self.sizes[stackNumber-1]
        return offset + index

    def peek(self, stackNumber):
        if not self.isEmpty(stackNumber):
            return self.custList[self.peekIndex(stackNumber)]
        return "Stack is Empty"
    
    def push(self, stackNumber, val):
        if not self.isFull(stackNumber):
            self.custList[self.peekIndex(stackNumber)] = val
            self.sizes[stackNumber-1] += 1
        else:
            print("stack overflow")
    
    def pop(self, stackNumber):
        if not self.isEmpty(stackNumber):
            elem = self.custList[self.peekIndex(stackNumber)]
            self.sizes[stackNumber-1] -= 1
            return elem
        print("stack underflow")
    

customStack = MultiStack(3)
print(customStack.isFull(1))
print(customStack.isEmpty(2))
customStack.push(1,10)
customStack.push(1, 36)
customStack.push(2,56)
customStack.push(3,78)
print(customStack.custList)
print(customStack.peek(1))
print(customStack.pop(1))
