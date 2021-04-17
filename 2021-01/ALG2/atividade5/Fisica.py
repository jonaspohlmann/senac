from Pessoa import Pessoa

class Fisica(Pessoa):
    def __init__(self, cpf, idade, peso, altura):
        self.__cpf = str(cpf)
        self.idade = int(idade)
        self.peso = float(peso)
        self.altura = float(altura)

    def imprimeCpf(self):
        return self.__cpf

    def __calculaIMC(self):
        return float(self.peso/(self.altura*self.altura))