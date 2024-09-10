class Contato:
    def __init__(self,id,telefone,nome):
        self.id = id
        self.telefone = telefone
        self.nome = nome
        self.esquerdo = None
        self.direito = None
        self.altura = 1
    def __str__(self):
        return f"{self.id}, Nome: {self.nome}, Telefone: {self.telefone}"

    def __repr__(self):
        return str(self.id)
  
class Avl:

    def inserir(self, raiz, contato):
        # Insere o nó e atualiza a altura
        # Verifica o balanceamento e realiza rotações se necessário
        if not raiz:
            return contato
        if contato.id < raiz.id:
            raiz.esquerdo = self.inserir(raiz.esquerdo, contato)
        else:
            raiz.direito = self.inserir(raiz.direito, contato)
    
        #Atualizando a altura da subárvore
        raiz.altura = 1 + max(self._altura(raiz.esquerdo), self._altura(raiz.direito))
        #Verificando o balanceamento
        balanco = self._balanceamento(raiz)
        
        #rotação esquerda
        if balanco > 1 and contato.id < raiz.esquerdo.id:
            return self._rotacao_direito(raiz)
        #rotação direita
        elif balanco < -1  and contato.id > raiz.direito.id:
            return self._rotacao_esquerdo(raiz)
        #rotação dupla(esquerda-direita)
        elif balanco > 1 and contato.id > raiz.esquerdo.id:
            raiz.esquerdo = self._rotacao_esquerdo(raiz.esquerdo)
            return self._rotacao_direito(raiz)
        #rotação dupla(direita-esquerda)
        elif balanco < -1 and contato.id < raiz.direito.id:
            raiz.direito = self._rotacao_direito(raiz.direito)
            return self._rotacao_esquerdo(raiz)
        return raiz
    
    def remover(self, raiz, id):
        # usando o ID remove o nó e realiza rotações se necessário
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
    
    #Faz a busca por Nomes
    def buscar(self, raiz, nome):
        if not raiz:
            return []
        result = []
        if nome.lower() in raiz.nome.lower():
            result.append(raiz)
        result += self.buscar(raiz.esquerdo, nome)
        result += self.buscar(raiz.direito, nome)
        return result

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

    def _get_value(self, raiz):
        while raiz.esquerdo is not None:
            raiz = raiz.esquerdo
        return raiz
    def inorder(self, raiz):
        if raiz:
            if raiz.esquerdo:
                self.inorder(raiz.esquerdo)
            print(f"ID: {raiz.id}, Nome: {raiz.nome}, Telefone: {raiz.telefone}")
            if raiz.direito:
                self.inorder(raiz.direito)
        
"""EXEMPLOS DE USO"""
add = Avl()
raiz = None
#adiçõa
contato1 = Contato(10, "1234-5678", "João")
contato2 = Contato(9, "9876-54321", "Maria")
contato3 = Contato(8, "4567-51562", "Felipe")

raiz = add.inserir(raiz, contato1)
raiz = add.inserir(raiz, contato2)
raiz = add.inserir(raiz, contato3)
add.inorder(raiz)
print(15*"--")
#removendo
raiz = add.remover(raiz, 9)
add.inorder(raiz)
print(15*"--")
#Busca
result = add.buscar(raiz, "felipe")
for contato in result:
    print(contato)