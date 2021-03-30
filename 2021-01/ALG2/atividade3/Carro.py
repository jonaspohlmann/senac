from Automovel import Automovel

class Carro(Automovel):
    def __init__(self, marca, qtdRodas, modelo, potenciaDoMotor, qtdPortas):
        super().__init__(marca, qtdRodas, modelo, potenciaDoMotor)
        self.qtdPortas = int(qtdPortas)
    
    def imprimirInformacoes(self):
        super().imprimirInformacoes()
        print(f"Qtd de portas: {self.qtdPortas}")