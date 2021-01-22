class Node:
    #inicializa a árvore
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data 
        
    #imprime os valores armazenados na árvore binária de forma recursiva
    def PrintValue(self):
        if self.left:
            self.left.PrintValue()
        if self.right:
            self.right.PrintValue()
        print(self.data)
        
    #insere um valor à esquerda ou à direita do nó raíz
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
    
    #encontra um valor na árvore e retorna uma string
    def find(self, value):
        if value < self.data:
            if self.left is None:
                return str(value)+" Não foi encontrado"
            return self.left.findval(value)
        elif value > self.data:
            if self.right is None:
                return str(value)+"Não foi encontrado"
            return self.right.findval(value)
        else:
            print(str(self.data) + ' Foi encontrado')



#instancia a árvore
root = Node(10)
root.insert(5)
root.insert(6)
root.insert(81)
root.insert(17)

root.PrintValue()

#verifica existência dos valores
print(root.find(17))
print(root.find(14))
