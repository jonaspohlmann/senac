class Rentagulo:
    def __init__(self,altura,largura):
        self.altura = altura
        self.largura = largura
    def getresultado(self):
        return self.altura * self.largura


a = float(input("Informe a altura:"))
b = float (input("Informe a largura:"))

ret = Rentagulo(a,b)
print(ret.getresultado())