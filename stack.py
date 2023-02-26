class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, value):
        self.stack.append(value)
    
    def pop(self):
        if self.stack == []:
            return "underflow"
        return self.stack.pop(-1)

    def peek(self):
        if self.stack == []:
            return "underflow"
        return self.stack[-1]
    
    def display(self):
        for i in range(len(self.stack)-1, -1, -1):
            print(self.stack[i])



firstStack = Stack()
firstStack.push(6)
firstStack.push(2)
firstStack.push(8)
firstStack.push(9)
firstStack.display()
print(firstStack.pop())
print(firstStack.peek())
firstStack.display()