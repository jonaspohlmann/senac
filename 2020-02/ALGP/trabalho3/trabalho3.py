from os import system, name
import os.path

#Função externa - https://www.geeksforgeeks.org/clear-screen-python/
def clear(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear')

#Variáveis globais
lst_estado = []
lst_cidade = []

#Tratamento de mensagens
def inputEnter():
    input("Aperte [ENTER] para prosseguir\n")

def printDescritivo(mensagem):
    print("")
    separador = "="*10
    
    print(f"{separador} {mensagem.upper()} {separador}")

def printAviso(mensagem):
    print(f"{mensagem}!")
    inputEnter()

#Validações
def isEmpty(x):
    return x == '' or x == None

def inputValidaVazio(mensagem, casoVazio):
    x = input(mensagem).upper()
    if isEmpty(x):
        BusinessException(casoVazio)
    return x

def validarIntervaloOpcao(opcao, min, max):
    if int(opcao) < int(min) or int(opcao) > int(max):
        BusinessException("Opção Inválida")
    return True

def validarConfirmacao(mensagem):
    return inputValidaVazio(f"{mensagem} - S/N? ", "Opção inválida").upper() == 'S'

#Classes
class Estado:
    def __init__(self, nome_estado, sigla, pais, qt_estado):
        self.nome_estado = str(nome_estado)
        self.sigla = str(sigla)
        self.pais = str(pais)
        self.qt_estado = int(qt_estado)
    
    def __str__(self):
        return f'''Estado: {self.nome_estado}\nUF: {self.sigla}'''

    def getNomeEstado(self):
        return self.nome_estado

    def setNomeEstado(self, nome_estado):
        self.nome_estado = nome_estado
    
    def getSigla(self):
        return self.sigla
    
    def setSigla(self, sigla):
        self.sigla = sigla
    
    def getPais(self):
        return self.pais
    
    def setPais(self, pais):
        self.pais = pais

    def getQtEstado(self):
        return self.qt_estado
    
    def setQtEstado(self, qt_estado):
        self.qt_estado = qt_estado

class Cidade:
    def __init__(self, nome, estado, qt_casos):
        self.nome = str(nome)
        self.estado = estado
        self.qt_casos = int(qt_casos)

    def __str__(self):
        return f'''Nome: {self.nome}\nEstado: {self.estado.sigla}'''

    def acrescentarCasos(self, qt_casos):
        self.qt_casos += qt_casos
        self.estado.qt_estado += qt_casos

    def getNome(self):
        return self.nome
    
    def setNome(self, nome):
        self.nome = nome
    
    def getEstado(self):
        return self.estado
    
    def setEstado(self, estado):
        self.estado = estado
    
    def getQtCasos(self):
        return self.qt_casos
    
    def setQtCasos(self, qt_casos):
        self.qt_casos = qt_casos

class BusinessException:
    def __init__(self, mensagem):
        print(f"ERRO! {mensagem}")
        inputEnter()
        raise ValueError

#Funções Estado
def existeEstado(nome="", sigla=""):
    #Validação tanto para nome quanto sigla para otimização do sistema
    for estado in lst_estado:
        if estado.getNomeEstado() == nome or estado.getSigla() == sigla:
            return estado
    return None

def selecionaEstado():
    printDescritivo("SELECIONE O ESTADO")
    for estado in lst_estado:
        print(estado.getSigla())
    sigla = inputValidaVazio("UF do estado da cidade: ", "UF inválida")
    return existeEstado("", sigla)

def cadastrarEstado():
    nome = inputValidaVazio("Nome do estado: ", "Nome não pode ser vazio")

    sigla = inputValidaVazio("UF: ", "Sigla não pode ser vazia")

    if existeEstado(nome, sigla) != None: 
        BusinessException("Estado/UF já cadastrado")

    estado = Estado(nome, sigla, "BRASIL", 0)
    
    printDescritivo("Confirmação")
    print(estado)
    if validarConfirmacao("Confirma estado?"):
        lst_estado.append(estado)
        printAviso("Estado cadastrado com sucesso")
    else:
        printAviso("Estado não cadastrado")

def relatorioEstados():
    if len(lst_estado) == 0:
        BusinessException("Não há estados cadastrados")

    relatorio = ""
    for estado in lst_estado:
        pontos = "."*(50-len(f"{estado.getNomeEstado()}"))
        relatorio += f"{estado.getNomeEstado()}{pontos} - total de Casos: {estado.getQtEstado()}\n"
    print(relatorio)
    inputEnter()

#Funções Cidade
def existeCidade(nome):
    for cidade in lst_cidade:
        if cidade.getNome() == nome:
            return cidade
    return None

def selecionaCidade():
    printDescritivo("SELECIONE A CIDADE")
    for cidade in lst_cidade:
        print(f"{cidade.getNome()} - Número de casos: {cidade.getQtCasos()}")
    nome = inputValidaVazio("Digite a cidade desejada: ", "Cidade não pode ser vazia").upper()
    return existeCidade(nome)

def cadastrarCidade():
    if len(lst_estado) == 0:
        BusinessException("Não há estados cadastrados")

    nome = inputValidaVazio("Nome da cidade: ", "Cidade não pode ser vazia")

    if existeCidade(nome) != None:
        BusinessException("Cidade já cadastrada")

    estado = selecionaEstado()
    if estado == None:
        BusinessException("Estado não cadastrado")
    
    cidade = Cidade(nome, estado, 0)
    printDescritivo("Confirmação")
    print(cidade)
    if validarConfirmacao("Confirma cidade?"):
        lst_cidade.append(cidade)
        print("Cidade cadastrada com sucesso")
    else:
        printAviso("Cidade não cadastrada")

def relatorioCidades():
    if len(lst_cidade) == 0:
        BusinessException("Não há cidades cadastradas")

    relatorio = ""
    for cidade in lst_cidade:
        pontos = "."*(50-len(f"{cidade.getNome()} - {cidade.getEstado().getSigla()}"))
        relatorio += f"{cidade.getNome()} - {cidade.getEstado().getSigla()}{pontos} - Casos Registrados: {cidade.getQtCasos()}\n"
    print(relatorio)
    inputEnter()

def atualizarCasos():
    if len(lst_cidade) == 0:
        BusinessException("Não há cidades cadastradas")
    cidade = selecionaCidade()
    if cidade == None:
        BusinessException("Cidade não cadastrada")
    
    nr_novos_casos = inputValidaVazio("Digite a quantidade de novos casos na cidade: ", "Quantidade não pode ser vazia")
    nr_novos_casos = int(nr_novos_casos)
    if nr_novos_casos < 0:
        BusinessException("Valor inválido digite um número correto")
    
    if validarConfirmacao("Confirma dados?"):
        cidade.acrescentarCasos(nr_novos_casos)
        printAviso("Dados atualizados com sucesso")
    else:
        printAviso("Dados não foram atualizados")

#Arquivos
def formatarArquivo(): 
    arquivo = ""
    
    if len(lst_estado) != 0:
        arquivo += "ESTADOS"
        for estado in lst_estado:
            arquivo += f"\n{estado.getNomeEstado()};{estado.getSigla()}"

    if len(lst_cidade) != 0:
        arquivo += "\nCIDADES"
        for cidade in lst_cidade:
            arquivo += f"\n{cidade.getNome()};{cidade.getQtCasos()};{cidade.getEstado().getSigla()}"
    return arquivo

def salvarArquivo():
    arquivo = open('db.csv','w')
    arquivo.seek(0)
    arquivo.write(str(formatarArquivo()))
    arquivo.close()

def carregarArquivo():
    if (os.path.isfile('db.csv')):
        arquivo = open('db.csv','r')
        fluxoEstado = False
        fluxoCidade = False
        for linha in arquivo:
            if not isEmpty(linha):
                linha = linha.rstrip()
                if fluxoEstado and linha != "ESTADO" and linha != "CIDADES":
                    splitEstado = linha.split(";")
                    nome = splitEstado[0]
                    sigla = splitEstado[1]

                    estado = Estado(nome, sigla, "BRASIL", 0)
                    lst_estado.append(estado)
                elif fluxoCidade and linha != "ESTADO" and linha != "CIDADES":
                    splitCidade = linha.split(";")
                    nome = splitCidade[0]
                    qt_casos = int(splitCidade[1])
                    sigla = splitCidade[2]

                    estado = existeEstado("", sigla)
                    if estado != None:
                        cidade = Cidade(nome, estado, 0)
                        cidade.acrescentarCasos(qt_casos)
                        lst_cidade.append(cidade)

                if linha == "ESTADOS":
                    fluxoEstado = True
                    fluxoCidade = False
                elif linha == "CIDADES":
                    fluxoEstado = False
                    fluxoCidade = True
        arquivo.close()

#Menu
def menuPrincipal():
    printDescritivo("MENU")
    return int(inputValidaVazio('''   0 - Finalizar o Programa
   1 - Cadastrar Estados
   2 - Cadastrar Cidades
   3 - Relatório de Estados
   4 - Relatório de Cidades
   5 - Atualizar números de casos
Escolha: ''', "Opção inválida"))

#Main    
try:
    menu = -1
    carregarArquivo()
    while (menu != 0 ):
        try:
            clear()

            #print(lst_estado)
            #print(lst_cidade)
            menu = menuPrincipal()
            if validarIntervaloOpcao(menu, 0, 5):
                if menu == 1:
                    printDescritivo("Cadastro de Estado")
                    cadastrarEstado()
                elif menu == 2:
                    printDescritivo("Cadastro de Cidades")
                    cadastrarCidade()
                elif menu == 3:
                    printDescritivo("Relatório de Estados")
                    relatorioEstados()
                elif menu == 4:
                    printDescritivo("Relatório de Cidades")
                    relatorioCidades()
                elif menu == 5:
                    printDescritivo("Atualizar números de casos")
                    atualizarCasos()
        except:
            pass
            #raise
    salvarArquivo()
except:
    pass
    #raise