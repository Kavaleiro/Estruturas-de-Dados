import random

class ArvoreRaiz:
    def __init__(self, chave, val, esquerdo=None, direito=None, pai=None):
        self.chave = chave #chave
        self.valor = val #valor
        self.esquerdo = esquerdo #filho esquerdo
        self.direito = direito #filho direito
        self.pai = pai #Nó pai
    #Verificando se tem ramificação esquerda
    def tem_esquerdo(self):
        return self.esquerdo
        #verificando se tem ramificação a direita
    def tem_direito(self):
        return self.direito

        #verifica se o nó é filho da esquerda de outro nó
    def e_filho_esquerdo(self):
        #tem que ter nó pai e ser uma ramificação esquerda
        return self.pai and self.pai.esquerdo == self
        #verifica se o nó é filho da direita de outro nó
    def e_filho_direito(self):
        return self.pai and self.pai.direito == self

        #verifica se o nó é Raiz
    def e_raiz(self):
        #Not null. tem que retorna TRUE
        return not self.pai
        #verifica se o nó é folha
    def e_folha(self):
        return not (self.direito or self.esquerdo)
        #Verifica se o nó tem algum filho
    def tem_filho(self):
        return self.direito or self.esquerdo
        #Verifica se ambos tem filho
    def ambos_tem_filhos(self):
        return self.direito and self.esquerdo

        #Atualizando dados de um nó
    def atualiza_dados(self, chave, valor, esquerdo, direito):
        self.chave = chave
        self.valor = valor
        self.esquerdo = esquerdo
        self.direito = direito
        if self.tem_esquerdo():#pai de seu novo filho a esquerda
            self.esquerdo.pai = self
        if self.tem_direito():#pai de seu novo filho a direita
            self.direito.pai = self
            
#implementando a Árvore binária de busca
class BinaryTree:
    #Construtor
    def __init__(self):
        self.raiz = None
        self.size = 0

    #Mostrando 2 métodos para verificar o número de nós na árvore
    #def length(self):#Método 1
    #  return self.raiz.size
    #Usando a função built-in len() do Python
    def __len__(self):#Método 2
        return self.size

    """Esse método verifica se a Árvore já tem raiz. Caso não tenha, será criado
    uma raiz. Se a raiz existir, é chamado a função _put() para enconrtrar o local
    do elemento da árvore"""
    def put(self, chave, valor):
        if self.raiz:#se a raiz existir
            #adiciona um elemento a partir da raiz
            self._put(chave, valor, self.raiz)
        else:
            #caso não tenha, é criado uma raiz
            self.raiz = ArvoreRaiz(chave,valor)
        #colocando um número de nós
        self.size = self.size + 1
    #Criando a função auxiliar
    def _put(self, chave, valor, corrente):
        if chave < corrente.chave: #Caso a chave seja menor que raiz
            #verifica se tem filho esquerdo
            if corrente.tem_esquerdo():
                self._put(chave, valor, corrente.esquerdo)
            else: #caso não tenha
                corrente.esquerdo = ArvoreRaiz(chave, valor, pai=corrente)
        if chave > corrente.chave:#Caso a chave seja maior que raiz
            if corrente.tem_direito():
                self._put(chave,valor,corrente.direito)
            else:
                corrente.direito = ArvoreRaiz(chave, valor, pai=corrente)

    #Sobrecarga usando colchetes
    #T['a'] = 123
    def __setitem__(self,chave,valor):
        self.put(chave,valor)
    #Buscando elementos da árvore usando a chave
    def get(self, chave):
        #Se tem raiz
        if self.raiz:
            res = self._get(chave, self.raiz)
            if res:
                return res.valor
            else:
                return None
        else:
            return None
    #Função auxiliar que ajuda na busca da Árvore
    def _get(self,chave,corrente):
        if not corrente:#se não existe elemento ou chave
            return None
        elif corrente.chave == chave:#Se a chave for igual a o elemento
            return corrente
        elif chave < corrente.chave:#Se a chave for menor que o elemento
            #Busca a árvore a esquerda
            return self._get(chave, corrente.esquerdo)
        else:
            return self._get(chave, corrente.direito)
        
    #Sobrecarga usando colchetes
    #T['a'] para retornar o valor da chave 'a'
    def __getitem__(self,chave):
        return self.get(chave)
    #Permite usar o operar 'in'
    # 'a' in T
    def __contains__(self,chave):
        if self._get(chave,self.raiz):
            return True
        else:
            return False

    """PERCORRENDO A ÁRVORE"""
    #PREORDER
    def preorder(self, corrente_chave):
        #impirme o valor da raiz
        print(corrente_chave.chave)
        #Visitando a subávore esquerda
        if corrente_chave.tem_esquerdo(): #modificado
            self.preorder(corrente_chave.esquerdo)
        #Visita a subávore direita
        if corrente_chave.tem_direito():#modificado
            self.preorder(corrente_chave.direito)

    #INORDER*ordem crescente
    def inorder(self, corrente_chave):
        if corrente_chave.tem_esquerdo():#modificado
            self.inorder(corrente_chave.esquerdo)
        print(corrente_chave.chave)
        if corrente_chave.tem_direito():#modificado
            self.inorder(corrente_chave.direito)

    #POSTORDER
    def postorder(self, corrente_chave):
        if corrente_chave.tem_esquerdo():
            self.postorder(corrente_chave.esquerdo)
        if corrente_chave.tem_direito():
            self.postorder(corrente_chave.direito)
        print(corrente_chave.chave)

  #deleta o elemento de um nó da árvore
    def delete(self, chave):
        #Se a árvore contém mais de um nó#
        if self.size> 1:
                #Procura pelo elemento que será removido
            raiz_to_remove = self._get(chave, self.raiz)
                #se encontrou o elemento
            if raiz_to_remove:
                self.remove(raiz_to_remove)#Função remove()#
                self.size = self.size - 1
            else:
                #Se não, retorna um erro
                raise KeyError("Essa chave não existe na árvore")
        elif self.size == 1 and self.raiz.chave == chave: #se a chave tiver apenas 1 nó
            self.raiz = None
            self.size = self.size - 1
        else:
            raise KeyError("Essa chave não existe na árvore")

    def __delitem__(self,chave):
        self.delete(chave)

    """Casos a ser observados para a implementação da funca remove()"""
    #[1] - O NÓ A SER REMOVIDO É UMA FOLHA
    #[2] - O NÓ A SER REMMOVIDO TEM 1 FILHO
    #[3] - O NÓ A SER REMOVIDO TEM 2 FILHOS
    
    def remove(self, corrente_chave):
        #Caso [1]
        if corrente_chave.e_folha():
            #verificando se o nó é um filho a esquerda ou a direita
            if corrente_chave == corrente_chave.pai.esquerdo:
                corrente_chave.pai.esquerdo = None #"Mato" o elemento existente
            else:
                corrente_chave.pai.direito = None#"Mato" o elemento existente
    
        #Caso[2]
        #Se o nó corrente tem filho a esquerda
        if corrente_chave.tem_esquerdo():
            #Se o ó corrente é filho a esquerda
            if corrente_chave.e_filho_esquerdo():
                #corrente a ser removida
                corrente_chave.esquerdo.pai = corrente_chave.pai
                #filho esquerdo do nó a ser removido
                corrente_chave.pai.esquerdo = corrente_chave.esquerdo
            #Se o nó corrente é filho a direita
            elif corrente_chave.e_filho_direito():
                corrente_chave.esquerdo.pai = corrente_chave.pai
                corrente_chave.pai.direito = corrente_chave.esquerdo
            else:
            #se não tem filho nem a direita e ne a esquerda é raiz
                corrente_chave.atualiza_dados(corrente_chave.esquerdo.chave,
                                            corrente_chave.esquerdo.valor,
                                            corrente_chave.esquerdo.esquerdo,
                                            corrente_chave.esquerdo.direito)
        if corrente_chave.tem_direito():
            #Se o ó corrente é filho a esquerda
            if corrente_chave.e_filho_esquerdo():
                #corrente a ser removida
                corrente_chave.direito.pai = corrente_chave.pai
                #filho direito do nó a ser removido
                corrente_chave.pai.esquerdo = corrente_chave.direito
                #Se o nó corrente é filho a direita
            elif corrente_chave.e_filho_direito():
                corrente_chave.direito.pai = corrente_chave.pai
                corrente_chave.pai.direito = corrente_chave.direito
            else:
                #se não tem filho nem a direita e ne a esquerda é raiz
                corrente_chave.atualiza_dados(corrente_chave.direito.chave,
                                            corrente_chave.direito.valor,
                                            corrente_chave.direito.esquerdo,
                                            corrente_chave.direito.direito)

        #caso [3]
        else:
            sucessor = corrente_chave.direito
            while sucessor.tem_esquerdo():
                sucessor = sucessor.esquerdo
            corrente_chave.chave = sucessor.chave
            corrente_chave.valor = sucessor.valor
            self.remove(sucessor)
            
"""EXEMPLOS DE USO DESTE CÓDIGO"""
#inserindo elementos 
arvore = BinaryTree()
arvore.put(10, "Raiz")
arvore.put(5, "Filho Esquerdo")
arvore.put(15, "Filho Direito")
arvore.put(3, "Filho Esquerdo do Filho Esquerdo")
arvore.put(7, "Filho Direito do Filho Esquerdo")
arvore.put(12, "Filho Esquerdo do Filho Direito")
arvore.put(18, "Filho Direito do Filho Direito")


"""#Buscando Valores"""

print(f"Usando colchetes: {arvore[7]}")#Método[2]
print(15*"-")
"""Removendo Valores"""
print("antes da Remoção")
arvore.inorder(arvore.raiz)
print(15*"-")
print("Removendo o nó com chave 5 (com filhos)...")
arvore.delete(5)
print(15*"-")
print("Depois da remoção")
arvore.inorder(arvore.raiz)
#percorrendo a ÁRVORE
#print("PREORDER")
#arvore.preorder(arvore.raiz)
#print("INORDER")
#arvore.inorder(arvore.raiz)
#print("POSTORDER")
#arvore.postorder(arvore.raiz)
#chave = 7
#valor = arvore.get(chave)
#print(f"Valor associado à chave {chave}: {valor}")#Método[1]