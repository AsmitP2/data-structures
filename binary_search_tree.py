class Bst:
    def __init__(self, data):
        self.data=data
        self.right = None
        self.left = None

    def addChild(self, data):
        if self.data == data:
            return
        elif self.data < data:
            if self.right:
                self.right.addChild(data)
            else:
                self.right = Bst(data)
        else:
            if self.left:
                self.left.addChild(data)
            else:
                self.left = Bst(data)
    
    def inOrderTraversal(self):
        elements = []
        if self.left:
            elements+=self.left.inOrderTraversal()
        elements.append(self.data)
        if self.right:
            elements+=self.right.inOrderTraversal()
        return elements
    
def createTree(elements):
    root = Bst(elements[0])
    for i in range(1, len(elements)):
        root.addChild(elements[i])
    return root

lst = [3, 6, 12, 5, 23]

root = createTree(lst)
print(root.inOrderTraversal())

#create following methods: pre-order post - order search