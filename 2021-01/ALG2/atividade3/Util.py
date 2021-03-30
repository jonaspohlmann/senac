'''
from Util import Util, BusinessException
'''

from os import system, name
import os.path

class Util:
    #Função externa - https://www.geeksforgeeks.org/clear-screen-python/
    @staticmethod
    def clear(): 
        # for windows 
        if name == "nt": 
            _ = system("cls") 
        # for mac and linux(here, os.name is "posix") 
        else: 
            _ = system("clear")

    @staticmethod
    def enter():
        input(f"Aperte [ENTER] para continuar\n")

    @staticmethod
    def printAviso(mensagem):
        print(f"{mensagem}!")
        Util.enter()

    @staticmethod
    def isEmpty(x):
        return x == "" or x == None
    
    @staticmethod
    def BooleanToStr(x):
        if x: return "Sim" 
        else: return "Não"

    @staticmethod
    def validarMenu(opcao, intervaloMinimo, intervaloMaximo):
        if int(opcao) < int(intervaloMinimo) or int(opcao) > int(intervaloMaximo):
            BusinessException("Opção Inválida")
        return True

    @staticmethod    
    def validarSimOuNao(mensagem):
        return Util.validarInputVazio(f"{mensagem} - S/N? ", "Opção inválida").upper() == 'S'

    @staticmethod
    def validarInputVazio(mensagem, casoVazio = "Valor inválido"):
        x = input(mensagem).upper()
        if Util.isEmpty(x):
            BusinessException(casoVazio)
        return x

class BusinessException:
    def __init__(self, mensagem):
        print(f"ERRO! {mensagem}")
        Util.enter()
        raise ValueError