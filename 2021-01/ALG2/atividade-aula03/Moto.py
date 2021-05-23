from Automovel import Automovel
from Util import Util, BusinessException

class Moto(Automovel):
    def __init__(self, marca, qtdRodas, modelo, potenciaDoMotor, partidaEletrica):
        super().__init__(marca, qtdRodas, modelo, potenciaDoMotor)
        self.partidaEletrica = partidaEletrica
    
    def imprimirInformacoes(self):
        super().imprimirInformacoes()
        print(f"Partida elétrica: {Util.BooleanToStr(self.partidaEletrica)}")