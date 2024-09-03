class No:
  def __init__(self,chave):
    self.altura = 1
    self.chave = chave
    self.esquerdo = None
    self.direito = None
  def __str__(self):
    return str(self.chave)
  def __repr__(self):
    return str(self.chave)

class ArvoreAVL:
    def inserir(self, raiz,chave):
        if not raiz:
            return No(chave)
        if chave < raiz.chave:
            raiz.esquerdo = self.inserir(raiz.esquerdo, chave)
        else:
            raiz.direito = self.inserir(raiz.direito, chave)
        
        #Atualizando a altura da subávore
        raiz.altura = 1 + max(self._altura(raiz.esquerdo), self._altura(raiz.direito))
        #verificando o balanceamento
        balanco = self._balanceamento(raiz)
        
        # Rotação à esquerda
        if balanco > 1 and chave < raiz.esquerdo.chave:
            return self._rotacao_direito(raiz)
        # Rotação à direita
        if balanco < -1 and chave > raiz.direito.chave:
            return self._rotacao_esquerdo(raiz)
        # Rotação dupla (esquerda-direita)
        if balanco > 1 and chave > raiz.esquerdo.chave:
            raiz.esquerdo = self._rotacao_esquerdo(raiz.esquerdo)
            return self._rotacao_direito(raiz)
        # Rotação dupla (direita-esquerda)
        if balanco < -1 and chave < raiz.direito.chave:
            raiz.direito = self._rotacao_direito(raiz.direito)
            return self._rotacao_esquerdo(raiz)

        return raiz
    
    def remover(self, raiz, chave):
        
    
        if not raiz:
            return raiz
        if chave < raiz.chave:
            raiz.esquerdo = self.remover(raiz.esquerdo, chave)
        elif chave > raiz.chave:
            raiz.direito = self.remover(raiz.direito, chave)
        else:
            if raiz.esquerdo is None:
                return raiz.direito
            elif raiz.direito is None:
                return raiz.esquerdo
            temp = self._get_min_value_node(raiz.direito)
            raiz.chave = temp.chave
            raiz.direito = self.remover(raiz.direito, temp.chave)

        if not raiz:
            return raiz

        # Atualizando a altura da subárvore
        raiz.altura = 1 + max(self._altura(raiz.esquerdo), self._altura(raiz.direito))
        # Verificando o balanceamento
        balanco = self._balanceamento(raiz)

        # Rotação à esquerda
        if balanco > 1 and self._balanceamento(raiz.esquerdo) >= 0:
            return self._rotacao_direito(raiz)
        # Rotação à direita
        if balanco < -1 and self._balanceamento(raiz.direito) <= 0:
            return self._rotacao_esquerdo(raiz)
        # Rotação dupla (esquerda-direita)
        if balanco > 1 and self._balanceamento(raiz.esquerdo) < 0:
            raiz.esquerdo = self._rotacao_esquerdo(raiz.esquerdo)
            return self._rotacao_direito(raiz)
        # Rotação dupla (direita-esquerda)
        if balanco < -1 and self._balanceamento(raiz.direito) > 0:
            raiz.direito = self._rotacao_direito(raiz.direito)
            return self._rotacao_esquerdo(raiz)

        return raiz      

    def buscar(self, raiz, chave):
        if not raiz or raiz.chave == chave:
            return raiz
        if chave < raiz.chave:
            return self.buscar(raiz.esquerdo, chave)
        return self.buscar(raiz.direito, chave)

    #Funcões auxiliares
    def _altura(self, raiz):
        if not raiz:
            return 0
        return raiz.altura
    
    def _balanceamento(self, raiz):
        if not raiz:
            return 0
        return self._altura(raiz.esquerdo) - self._altura(raiz.direito)
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

#exemplos de uso    
avl = ArvoreAVL()
raiz = None
# Inserindo valores 
raiz = avl.inserir(raiz, 10)
raiz = avl.inserir(raiz, 20)
raiz = avl.inserir(raiz, 30)
raiz = avl.inserir(raiz, 40)
raiz = avl.inserir(raiz, 50)
raiz = avl.inserir(raiz, 25)
print("Árvore após inserções:")
print("Raiz:", raiz)
print("Esquerdo da raiz:", raiz.esquerdo)
print("Direito da raiz:", raiz.direito)
print(15*"-")
# Removendo valores
raiz = avl.remover(raiz, 40)
raiz = avl.remover(raiz, 50)
print("Árvore após remoções:")
print("Raiz:", raiz)
print("Esquerdo da raiz:", raiz.esquerdo)
print("Direito da raiz:", raiz.direito)
print(15*"-")
#Buscando valores
print("Busca pelo valor 20:", avl.buscar(raiz, 20))
print("Busca pelo valor 40:", avl.buscar(raiz, 40))
print("Busca pelo valor 25:", avl.buscar(raiz, 25))