lista_de_marcas = ['FORD', 'GM', 'VW']
escolha = ''


def validarMarca():
    while True:
        nova_marca = input('...Digite uma nova marca: ').upper()
        if nova_marca not in lista_de_marcas:
            return nova_marca
        else:
            input("---ERRO. Marca já cadastrada")

def cadastrarMarcas():
    lista_de_marcas.append(validarMarca())

def listarMarcas():
    print(*lista_de_marcas, sep=" - ")


def indiceCorreto():
    while True:
        marca_para_alterar = input('...Digite a marca a ser alterada').upper()
        if marca_para_alterar in lista_de_marcas:
            return lista_de_marcas.index(marca_para_alterar)
        else:
            input('--ERRO. Não existe marca com esta descrição')

def alterarMarca():
    lista_de_marcas[indiceCorreto()] = validarMarca()
    print()

def marcaCorreta():
    while True:
        marca = input('...Digite a marca a ser excluída').upper()
        if marca in lista_de_marcas:
            return marca
        else:
            input('--ERRO. Não existe marca com esta descrição')

def deletarMarca():
    lista_de_marcas.remove(marcaCorreta)

while escolha != '0':
    escolha = input('''
    0- Finalizar o Programa
    1- Cadastrar as marcas
    2- Listas as marcas cadastradas
    3- Alterar alguma marca digitada erroneamente
    4- Excluir uma marca da lista
    Escolha: ''')

    if escolha == '1':
        cadastrarMarcas()
    elif escolha == '2':
        listarMarcas()
    elif escolha == '3':
        alterarMarca()
    elif escolha == '4':
        deletarMarca()
    else:
        input('--ERRO. Opção inválida')