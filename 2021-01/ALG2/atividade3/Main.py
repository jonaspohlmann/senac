from Util import Util, BusinessException

from Veiculo import Veiculo
from Bicicleta import Bicicleta
from Automovel import Automovel
from Moto import Moto
from Carro import Carro

veiculo = None

def menuPrincipal():
    return Util.validarInputVazio(f"1 - Cadastrar\n2 - Acelerar\n3 - Frear\n0 - Sair do programa\nDigite a opção desejada: ")

def menuVeiculos():
    return Util.validarInputVazio(f"1 - Bicicleta\n2 - Moto\n3 - Carro\n0 - Voltar\nDigite a opção desejada: ")

def cadastrarVeiculo(menuVeiculo):
    marca = Util.validarInputVazio("Marca: ")
    qtdRodas = int(Util.validarInputVazio("Qtd Rodas: "))
    modelo = Util.validarInputVazio("Modelo: ")

    if (menuVeiculo == 1):
        numMarchas = Util.validarInputVazio("Número de Marchas: ")
        bagageiro = Util.validarSimOuNao("Bagageiro: ")
        return Bicicleta(marca, qtdRodas, modelo, numMarchas, bagageiro)
    elif (menuVeiculo == 2 or menuVeiculo == 3):
        potenciaDoMotor = Util.validarInputVazio("Potência do Motor: ")
        if (menuVeiculo == 2):
            partidaEletrica = Util.validarSimOuNao("Partida Elétrica: ")
            return Moto(marca, qtdRodas, modelo, potenciaDoMotor, partidaEletrica)
        elif (menuVeiculo == 3):
            qtdPortas = Util.validarInputVazio("Qtd Portas: ")
            return Carro(marca, qtdRodas, modelo, potenciaDoMotor, qtdPortas)

def acelerar():
    valor = Util.validarInputVazio("Digite o valor a acelerar: ")
    veiculo.acelerar(int(valor))

def frear():
    valor = Util.validarInputVazio("Digite o valor a frear: ")
    veiculo.frear(int(valor))

try:
    menu = -1
    while (menu != 0):
        Util.clear()
        menu = int(menuPrincipal())
        
        if (Util.validarMenu(menu, 0, 3)):
            if (menu == 1):
                menuVeiculo = int(menuVeiculos())
                if (menuVeiculo != 0):
                    veiculo = cadastrarVeiculo(menuVeiculo)
                    #bicicleta.imprimirInformacoes(bicicleta)
            elif (menu == 2):
                acelerar()
            elif (menu == 3):
                frear()
            if (menu != 0):
                veiculo.imprimirInformacoes()
                Util.enter()
except:
    pass
    #raise