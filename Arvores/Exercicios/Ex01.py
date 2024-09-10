class Biblioteca:
    def __init__(self,id, titulo,autor):
        self.altura = 1
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.esquerdo = None
        self.direito = None

    #Representção do objeto como string
    def __str__(self):
        return f"{self.id}: {self.titulo} por {self.autor}"
    
    #Função auxiliar para a representação em listas 
    def __repr__(self):
        return str(self)
    
class Livro:
    
    def inserir(self,raiz, id, titulo, autor):
        # Insere o nó e atualiza a altura
        # Verifica o balanceamento e realiza rotações se necessário
        if not raiz:
            return Biblioteca(id, titulo, autor)
        elif id < raiz.id:
            raiz.esquerdo = self.inserir(raiz.esquerdo, id, titulo, autor)
        else:
            raiz.direito = self.inserir(raiz.direito, id, titulo, autor)  
        
        #Atualizando a altura da subárvore
        raiz.altura = 1 + max(self._altura(raiz.esquerdo), self._altura(raiz.direito))
        #Verificando o balanceamento
        balanco = self._balanceamento(raiz)
        
        #rotação esquerda
        if balanco > 1 and id < raiz.esquerdo.id:
            return self._rotacao_direito(raiz)
        #rotação direita
        elif balanco < -1  and id > raiz.direito.id:
            return self._rotacao_esquerdo(raiz)
        #rotação dupla(esquerda-direita)
        elif balanco > 1 and id > raiz.esquerdo.id:
            raiz.esquerdo = self._rotacao_esquerdo(raiz.esquerdo)
            return self._rotacao_direito(raiz)
        #rotação dupla(direita-esquerda)
        elif balanco < -1 and id < raiz.direito.id:
            raiz.direito = self._rotacao_direito(raiz.direito)
            return self._rotacao_esquerdo(raiz)
        return raiz
    
    def remover(self, raiz, id):
        # Remove o nó e realiza rotações se necessário para manter o balanceamento
        if not raiz:
            return raiz
        elif id < raiz.id:#busca do nó esquerdo
            raiz.esquerdo = self.remover(raiz.esquerdo, id)
        elif id > raiz.id:#busca do nó direito
            raiz.direito = self.remover(raiz.direito, id)
        else:#Encontrou o nó a ser removido
            if raiz.esquerdo is None:
                return raiz.direito
            elif raiz.direito is None:
                return raiz.esquerdo
            temporario = self._get_value(raiz.direito)
            raiz.id = temporario.id
            raiz.direito = self.remover(raiz.direito, temporario.id)
        if not raiz:
            return raiz
        
        #Atualizando a altura da subárvore
        raiz.altura = 1 + max(self._altura(raiz.esquerdo), self._altura(raiz.direito))
        #Verificando o balanceamento
        balanco = self._balanceamento(raiz)

        #rotação esquerda
        if balanco > 1 and self._balanceamento(raiz.esquerdo) >= 0:
            return self._rotacao_direito(raiz)
        #rotação direita
        if balanco < -1  and self._balanceamento(raiz.direito) <= 0:
            return self._rotacao_esquerdo(raiz)
        #rotação dupla
        if balanco > 1 and self._balanceamento(raiz.esquerdo) < 0:
            raiz.esquerdo = self._rotacao_esquerdo(raiz.esquerdo)
            return self._rotacao_direito(raiz)
        if balanco < -1 and self._balanceamento(raiz.direito) > 0:
            raiz.direito = self._rotacao_direito(raiz.direito)
            return self._rotacao_esquerdo(raiz)
        return raiz
    #busca pelo ID do livro
    def buscar(self, raiz, id):
        if not raiz or raiz.id == id:
            return raiz
        if id < raiz.id:
            return self.buscar(raiz.esquerdo, id)
        return self.buscar(raiz.direito, id)

    ## FUNÇOES AUXILIARES
    def _altura(self, raiz):
        if not raiz:
            return 0
        return raiz.altura
    def _balanceamento(self, raiz):
        if not raiz:
            return 0
        return self._altura(raiz.esquerdo) - self._altura(raiz.direito)

    def _rotacao_esquerdo(self, z):
        y = z.direito
        T2 = y.esquerdo
        y.esquerdo = z
        z.direito = T2
        z.altura = 1 + max(self._altura(z.esquerdo), self._altura(z.direito))
        y.altura = 1 + max(self._altura(y.esquerdo), self._altura(y.direito))
        return y
    
    def _rotacao_direito(self, z):
        y = z.esquerdo
        T3 = y.direito
        y.direito = z
        z.esquerdo = T3
        z.altura = 1 + max(self._altura(z.esquerdo), self._altura(z.direito))
        y.altura = 1 + max(self._altura(y.esquerdo), self._altura(y.direito))
        return y

    #Retorna o nó com o menor valor em uma subárvore
    def _get_value(self, raiz):
        while raiz.esquerdo is not None:
            raiz = raiz.esquerdo
        return raiz

      #imprime valore em ordem crescente
    def inorder(self, raiz):
        if raiz:
            if raiz.esquerdo:
                self.inorder(raiz.esquerdo)
            print(f"{raiz.id}: {raiz.titulo} por {raiz.autor}")
            if raiz.direito:
                self.inorder(raiz.direito)
            
livros = Livro()
raiz = None
#Inserindo Livros
raiz = livros.inserir(raiz, 1, "O Senhor dos Anéis", "J.R.R. Tolkien")
raiz = livros.inserir(raiz, 2, "Harry Potter", "J.K. Rowling")
raiz = livros.inserir(raiz, 3, "1984", "George Orwell")
#Mostrando os livros em ordem crescente 
livros.inorder(raiz)
#removendo o livro pelo Id
raiz = livros.remover(raiz, 2)
print(30*"-")
livros.inorder(raiz)
print(30*"-")
# Buscando um livro pelo ID
livro_encontrado = livros.buscar(raiz, 1)
if livro_encontrado:
    print(f"Livro encontrado: {livro_encontrado}")
else:
    print("Livro não encontrado")



    