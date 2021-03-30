class Veiculo:
    def __init__(self, marca, qtdRodas, modelo):
        self.marca = marca
        self.qtdRodas = int(qtdRodas)
        self.modelo = modelo
        self.velocidade = 0
    
    def imprimirInformacoes(self):
        print(f"Marca:  {self.marca}")
        print(f"Qtd Rodas: {self.qtdRodas}")
        print(f"Modelo: {self.modelo}")
        print(f"Velocidade: {self.velocidade}")
    
    def acelerar(self, valor):
        self.velocidade += valor

    def frear(self, valor):
        self.velocidade -= valor