from Atividades.Atividade13.Classes.No import No


class Pilha:
    def __init__(self):
        self.topo = None
        self.tamanho = 0

    def adicionar(self, valor):
        no = No(valor)
        no.proximo = self.topo
        self.topo = no
        self.tamanho += 1

    def remover(self):
        if self.tamanho > 0:
            self.topo = self.topo.proximo
            self.tamanho -= 1

    def imprimir_topo(self):
        if self.tamanho > 0:
            print(self.topo.dado)

    def __len__(self):
        return self.tamanho

    def __repr__(self, items=''):
        pointer = self.topo
        while pointer:
            items = f'{items}{str(pointer.dado)}, '
            pointer = pointer.proximo
        return items
