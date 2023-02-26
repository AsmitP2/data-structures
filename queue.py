class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, value):
        self.queue.append(value)
    
    def dequeue(self):
        if self.queue == []:
            return "Underflow"
        return self.queue.pop(0)
    
    def peek(self):
        return self.queue[0]
    
    def display(self):
        print(self.queue)

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())
print(queue.peek())
queue.display()