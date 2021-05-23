# -*- coding: UTF-8 -*-
from abc import ABCMeta, abstractmethod

class Computador:
    __metaclass__ = ABCMeta
    def __init__(self, modelo, cor, preco):
        self.modelo = modelo
        self.cor = cor
        self.preco = preco
    
    def getInformacoes(self):
        return self.modelo + ' ' + self.cor + ' ' + self.preco
    
    @abstractmethod
    def cadastrar(self, modelo, cor, preco):
        self.__init__(modelo, cor, preco)
    
class Desktop(Computador):
    def __init__(self, modelo, cor, preco, potenciaDaFonte):
        super().__init__(modelo, cor, preco)
        self._potenciaDaFonte = potenciaDaFonte
    def getInformacoes(self):
        return super().getInformacoes() + ' ' + self._potenciaDaFonte

class Notebook(Computador):
    def __init__(self, modelo, cor, preco, tempoDeBateria):
        super().__init__(modelo, cor, preco)
        self.__tempoDeBateria = tempoDeBateria
    def getInformacoes(self):
        return super().getInformacoes() + ' ' + self.__tempoDeBateria
