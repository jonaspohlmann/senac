class Pessoa:
    def __init__(self, codigo, nome, endereco, telefone):
        
        self.__codigo = int(codigo)
        self.nome = str(nome)
        self._endereco = str(endereco)
        self.__telefone = str(telefone)
    
    def imprimeNome(self):
        return self.nome
    
    def __imprimeTelefone(self):
        print(self.__telefone)