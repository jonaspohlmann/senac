from Veiculo import Veiculo

class Automovel(Veiculo):
    def __init__(self, marca, qtdRodas, modelo, potenciaDoMotor):
        Veiculo.__init__(self, marca, qtdRodas, modelo)
        self.potenciaDoMotor = float(potenciaDoMotor)

    def imprimirInformacoes(self):
        Veiculo.imprimirInformacoes(self)
        print(f"Potência: {self.potenciaDoMotor}")