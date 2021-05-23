from No import No

class Lista:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def listaVazia(self):
        return self.inicio is None
    
    def adicionar(self, valor):
        no = No(valor)
        if self.listaVazia():
            self.inicio = no
            self.fim = no
        else:
            no.anterior = self.fim
            no.proximo = None
            self.fim.proximo = no
            self.fim = no

    def imprimir(self): 
        print(f"Lista Duplcamente Encadeada:")
        no = self.inicio

        lista = ""
        while no is not None:
            if lista == "":
                lista += "|"
            lista += f" {str(no.dado)} |"
            
            no = no.proximo
        print(lista)

    def imprimirInverso(self):
        print(f"Lista Duplcamente Encadeada Inversa:")
        no = self.fim

        lista = ""
        while no is not None:
            lista += f"| {str(no.dado)} "
            
            no = no.anterior
        
        if lista != "":
            lista += "|"
        print(lista)
    