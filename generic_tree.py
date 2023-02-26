class TreeNode:
    def __init__(self, data):
        self.data = data
        self.childrens = []
        self.parent = None

    def addChild(self, child):
        self.childrens.append(child)
        child.parent = self

    def getLevel(self):
        level = 0
        p = self.parent
        while p:
            p = p.parent
            level +=1
        return level

    def displayTree(self):
        spaces = "   "*self.getLevel()
        symbol = spaces + "\__"
        print(symbol+self.data)
        if self.childrens:
            for child in self.childrens:
                child.displayTree()

finder = TreeNode("finder")
documents = TreeNode("documents")
desktop = TreeNode("desktop")
C_Drive = TreeNode("C Drive")
personal = TreeNode("personal")
work = TreeNode("work")
iCloud = TreeNode("iCloud")
oneDrive = TreeNode("work")
document1 = TreeNode("personal")
document2 = TreeNode("work")

finder.addChild(documents)
finder.addChild(desktop)
finder.addChild(C_Drive)

documents.addChild(document2)
documents.addChild(document1)

desktop.addChild(iCloud)
desktop.addChild(oneDrive)

C_Drive.addChild(personal)
C_Drive.addChild(work)

finder.displayTree()