class Autor:
    def __init__(self, id, nome):
        self._id = id
        self.nome = nome

    def setId(self, id):
        self._id = id

class Livro:
    def __init__(self, id, titulo, autor):
        self.id = id
        self.titulo = titulo
        self.autor = autor

class No:
    def __init__(self,dado):
        self.dado = dado
        self.proximo = None

class Pilha:
    def __init__(self):
        self.topo = None
        self.tamanho = 0

    def insert(self,valor):
        no = No(valor)
        no.proximo = self.topo
        self.topo = no
        self.tamanho+= 1

    def delete(self):
        if self.tamanho > 0:
            no = self.topo
            self.topo = self.topo.proximo
            self.tamanho -= 1

autor1 = Autor(1, 'Jonas')
autor2 = Autor(2, 'Luzia')
autor3 = Autor(3, 'Bruna')

livro1 = Livro(1, 'Memórias Póstumas de Jonas', autor1)
livro2 = Livro(2, 'MagazineLuzia', autor2)
livro3 = Livro(3, 'O Senhor dos Anéis: A sociedade da Bruna', autor3)

pilha = Pilha()
pilha.insert(livro1)
pilha.insert(livro2)
pilha.insert(livro3)

pilha.delete()
print(pilha.tamanho)