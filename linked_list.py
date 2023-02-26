class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insertBeginning(self, data):
        node = Node(data, self.head)
        self.head = node
    
    def insertEnd(self, data):
        node = Node(data, None)
        itr = self.head
        while itr.next != None:
            itr = itr.next
        itr.next = node

    def removeBeginning(self):
        self.head = self.head.next

    def removeEnd(self):
        itr = self.head
        while itr.next.next != None:
            itr = itr.next
        itr.next = None

    def length(self):
        itr = self.head
        output = 0
        while itr != None:
            output+=1
            itr = itr.next
        return output
    
    def display(self):
        itr = self.head
        ll = ""
        while itr != None:
            ll+=str(itr.data)+"->"
            itr = itr.next
        print(ll)

lst = LinkedList()
lst.insertBeginning(7)
lst.insertBeginning(8)
lst.insertBeginning(3)
lst.insertBeginning(2)
lst.insertBeginning(6)
lst.insertEnd(1)
lst.insertEnd(9)
lst.insertEnd(5)
lst.insertEnd(4)
lst.removeBeginning()
lst.removeEnd()
print(lst.length())
lst.display()