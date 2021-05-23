from Pessoa import Pessoa

class Juridica(Pessoa):
    def __init__(self, cnpj, inscricaoEstadual, quantidadeFuncionarios):
        self.__cnpj = str(cnpj)
        self.__inscricaoEstadual = str(inscricaoEstadual)
        self.quantidadeFuncionarios = int(quantidadeFuncionarios)
    
    def imprimeCNPJ(self):
        print(self.__cnpj)
    
    def __emitirNotaFiscal(self):
        pass