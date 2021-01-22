class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data 
    
    def PrintValue(self):
        if self.left:
            self.left.PrintValue()
        if self.right:
            self.right.PrintValue()
        print(self.data)
        

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None: 
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:            
            self.data = data




root = Node(10)
root.insert(5)
root.insert(6)
root.insert(81)
root.insert(17)

root.PrintValue()
