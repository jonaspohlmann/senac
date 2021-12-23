from os import system, name

#Função externa - https://www.geeksforgeeks.org/clear-screen-python/
def clear(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear')

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

#Menus principal e de notas
def menuPrincipal():
    try:
        return int(input("0 - Finaliza o Programa \n"
                        +"1 - Cadastrar avaliador \n"
                        +"2 - Realizar avaliação \n"
                        +"3 - Relatório de avaliadores \n"
                        +"4 - Relatório de produtos \n"
                        +"Digite a opção desejada: \n"))
    except:
        mensagemErro("Opção incorreta")

def menuNotas():
    try:
        return int(input("1 - Péssimo\n"
                        +"2 - Ruim\n"
                        +"3 - Regular\n"
                        +"4 - Bom\n"
                        +"5 - Ótimo\n"))
    except:
        mensagemErro("Nota incorreta")

def inputUpper(mensagem):
    return input(mensagem).upper()

def printArray(array):
    print(*array, sep=" - ")

def mensagemEnter():
    input("Pressione [Enter] para continuar\n")

def mensagemErro(mensagem):
    print(f"ERRO! - {mensagem}!")
    mensagemEnter()

def mensagemSucesso(mensagem):
    print(mensagem)
    mensagemEnter()

def validaIntervalo(valor, inicio, fim):
    if (inicio > valor or fim < valor) and valor != None:
        mensagemErro("Opção inválida")
        return False
    return True

#Função utilizada tanto no cadastro quanto na validação da avaliação
def lerAvaliador(cadastro = False):
    if not cadastro:
        printArray(lista_de_avaliadores)
    avaliador = inputUpper("Digite o avaliador: ")
    if isNotEmpty(avaliador) and (avaliador in lista_de_avaliadores or cadastro):
        return avaliador
    else:
        mensagemErro("Avaliador Inválido")

def lerProduto(avaliador):
    printArray(lista_de_produtos)
    produto = inputUpper("Escolha o produto a ser avaliado: ")
    if avaliador in pesquisa and produto in pesquisa[avaliador]:
        mensagemErro("Avaliador já avaliou este produto")
    else:
        if produto in lista_de_produtos:
            return produto
        else:
            mensagemErro("Produto inválido")

def cadastrarAvaliacao(avaliador, produto, nota):
    if (avaliador in pesquisa): pesquisa[avaliador] += [produto, nota]
    else: pesquisa[avaliador] = [produto, nota]
    mensagemSucesso("Avaliação cadastrada com sucesso!")

def verificaListaAvaliadores():
    if len(lista_de_avaliadores) == 0:
        resposta = input("Não há avaliadores cadastrados, deseja cadastrá-lo agora? S/N: ")
        cadastrarAvaliador() if resposta == "S" else ""
        return False
    return True

#Funções de Menu
def cadastrarAvaliador():
    avaliador = lerAvaliador(True)
    if isNotEmpty(avaliador):
        lista_de_avaliadores.append(avaliador)
        mensagemSucesso("Avaliador cadastrado com sucesso!")

def realizarAvaliacao():
    if verificaListaAvaliadores():
        print("Indique o avaliador")
        avaliador = lerAvaliador()
        if isNotEmpty(avaliador):
            print("Indique o produto a ser avaliado")
            produto = lerProduto(avaliador)
            if isNotEmpty(produto):
                nota = menuNotas()
                if validaIntervalo(nota, 1, 5):
                    cadastrarAvaliacao(avaliador, produto, nota)

def relatorioAvaliadores():
    for avaliador in pesquisa:
        #todo produto tem dois indices, nome do produto e nota, dividindo por 2, eu tenho a quantidade de avaliações que aquele produto recebeu
        print(f"{avaliador} avaliou {str(int(len(pesquisa[avaliador])/2))} bebida(s)")
    mensagemEnter()

def relatorioProdutos():
    for produto in lista_de_produtos:
        soma = 0
        for avaliador in lista_de_avaliadores:
            if avaliador in pesquisa and produto in pesquisa[avaliador]:
                #procurando pelo nome do produto e somando +1 ao seu indice, obtenho a nota do produto
                soma += int((pesquisa[avaliador][pesquisa[avaliador].index(produto)+1]))
        if soma == 0:
            print(f"O produto {produto} ainda não recebeu nota")        
        else:
            print(f"O produto {produto} recebeu a nota total de {str(soma)}")
    mensagemEnter()

menu = -1
carregarArquivo()
while menu != 0:
    clear()
    #print(pesquisa)
    #print(lista_de_avaliadores)
    try:
        menu = menuPrincipal()
        if validaIntervalo(menu, 0, 4):
            if menu == 1:
                cadastrarAvaliador()
            elif menu == 2:
                realizarAvaliacao()
            elif menu == 3:
                relatorioAvaliadores()
            elif menu == 4:
                relatorioProdutos()
    except:
        pass
salvarArquivo(formatarTextoArquivo())