from Automovel import Automovel

class Carro(Automovel):
    def __init__(self, marca, qtdRodas, modelo, potenciaDoMotor, qtdPortas):
        Automovel.__init__(self, marca, qtdRodas, modelo, potenciaDoMotor)
        self.qtdPortas = int(qtdPortas)
    
    def imprimirInformacoes(self):
        Automovel.imprimirInformacoes(self)
        print(f"Qtd de portas: {self.qtdPortas}")