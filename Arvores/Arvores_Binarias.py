class No:
    def __init__(self, valor):
        self.chave = valor
        self.esquerdo = None
        self.direito = None

    def __str__(self):
        return f"{self.chave},{self.esquerdo},{self.direito}"
    def __repr__(self):
        return str(self)

    def inserir_esquerdo(self, valor):
        if self.esquerdo is None:
            self.esquerdo = No(valor)
        else:
            temporario = No(valor)
            temporario.esquerdo = self.esquerdo
            self.esquerdo = temporario

    def inserir_direito(self, valor):
        if self.direito is None:
            self.direito = No(valor)
        else:
            temporario = No(valor)
            temporario.direito = self.direito
            self.direito = temporario

    def get_E(self):
        return self.esquerdo

    def get_D(self):
        return self.direito

    #atualizando o valor de determinado nó
    def set_R(self, data):
        self.chave = data
    #obtém o valor armazenado em determinado nó
    def get_R(self):
        return self.chave

    #Formas de percorrer uma Árvore binária
    #PREORDER
    """Começa na raiz, vai para a esqueda e depois para a direita"""
    def preorder(self):
        print(self.chave)#valor da raiz
        if self.esquerdo:
          self.esquerdo.preorder()
        if self.direito:
          self.direito.preorder()
    #INORDER
    """Começa por toda sub árvore a esquerda, depois vai para a raiz e
    logo em seguida para a direita"""
    #imprime valore em ordem crescente
    def inorder(self):
        if self.esquerdo:
            self.esquerdo.inorder()
        print(self.chave)
        if self.direito:
            self.direito.inorder()
    #POSTORDER
    """Comeca pela esquerda, depois para a direita e finaliza na raiz"""
    def postorder(self):
        if self.esquerdo:
            self.esquerdo.postorder()
        if self.direito:
            self.direito.postorder()
        print(self.chave)

r = No(1)
r.inserir_esquerdo(2)
r.inserir_direito(3)
r.esquerdo.inserir_esquerdo(4)
r.esquerdo.inserir_direito(5)
r.direito.inserir_esquerdo(6)
r.direito.inserir_direito(7)

r.preorder()
#r.postorder()
#r.inorder()
