class Node:
    #inicializa a árvore
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data 
        
         
    #insere um valor à esquerda ou à direita do nó 
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

    #preorder - imprime o valor armazenado em um nó e em seguida repete recursivamente para a esquerda e para a direita (imprime na ordem de inserção)
    def preval(self):
        print(str(self.data))
        if self.left:
            self.left.preval()
        if self.right:
            self.right.preval()
    
    #postorder - imprime o valor armazenado em um nó depois de visitar a esquerda e direita de forma recursiva
    def postorderval(self):
        if self.left:
            self.left.postorderval()
        if self.right:
            self.right.postorderval()
        print(self.data)

    #inorder - imprime os valores ordenados da esquerda para a direita (do menor ao maior valor)
    def inorderval(self):
        if self.left:
            self.left.inorderval()
        print(self.data)
        if self.right:
            self.right.inorderval()


#instancia a árvore
root = Node(10)
root.insert(7)
root.insert(11)
root.insert(6)
root.insert(8)
root.insert(9)
root.insert(1)
root.insert(11)
root.insert(20)
root.insert(14)
root.insert(22)

#imprime os dados armazenados na árvore

root.preorderval()
root.inorderval()
root.postorderval()

#verifica existência dos valores
print(root.find(17))
print(root.find(14))
