from Veiculo import Veiculo

class Automovel(Veiculo):
    def __init__(self, marca, qtdRodas, modelo, potenciaDoMotor):
        super().__init__(marca, qtdRodas, modelo)
        self.potenciaDoMotor = float(potenciaDoMotor)

    def imprimirInformacoes(self):
        super().imprimirInformacoes()
        print(f"Potência: {self.potenciaDoMotor}")