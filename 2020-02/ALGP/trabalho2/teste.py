#ARQUIVO UTILIZADO PARA TESTE DAS NOVAS FUNCIONALIDADES

#Declaração de variáveis
pesquisa = {} 
lista_de_produtos = ["COCACOLA", "GUARANÁ", "PEPSI", "FANTA", "SPRITE"]
lista_de_avaliadores = []

def isNotEmpty(x):
    if x != '' and x != None:
        return True
    return False

#Manipulando arquivos
def cadastraAvaliadorPorArquivo(avaliador):
    if avaliador not in lista_de_avaliadores:
        lista_de_avaliadores.append(avaliador)

def formatarTextoArquivo(): 
    arquivo = ""
    primeiraLinha = True
    for avaliador, produtoNota in pesquisa.items():
        if primeiraLinha:
            arquivo = str(avaliador)
        else:
            arquivo += "\n" + str(avaliador)
        for i in produtoNota:
            arquivo += ", " + str(i)
        primeiraLinha = False
    return arquivo

def salvarArquivo(texto):
    print("Salvando arquivo")
    arquivo = open('db.txt','w')
    arquivo.seek(0)
    arquivo.write(str(texto))
    arquivo.close()

def carregarArquivo():
    arquivo = open('db.txt','r')
    for linha in arquivo:
        if isNotEmpty(linha):
            linha = linha.rstrip()
            avaliadorProdutos = linha.split(", ")

            #O primeiro indice sempre será o avaliador
            linhaDicionario = {str(avaliadorProdutos[0]): []}
            cadastraAvaliadorPorArquivo(str(avaliadorProdutos[0]))
            for produtoNota in avaliadorProdutos:
                if avaliadorProdutos[0] != produtoNota:
                    linhaDicionario[avaliadorProdutos[0]] += [produtoNota] 
            
            pesquisa.update(linhaDicionario)

    arquivo.close()

pesquisa = {'AVALIADOR_A': ['COCACOLA', 5, 'PEPSI', 4],
            'AVALIADOR_B': ['COCACOLA', 1, 'PEPSI', 2, 'GUARANÁ', 3, 'FANTA', 3]}

salvarArquivo(formatarTextoArquivo())

carregarArquivo()

print(pesquisa)