# Exercício Aula03 - Solução

# declaração das listas
lista_de_marcas = []
lista_de_modelo = []
lista_de_marcas = ["FIAT","GM","VW","FORD","FIAT"]
lista_de_modelo = ["UNO" ,"OPALA","GOL","FIESTA","TORO"]


#=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-  01
def cadastrar_marcas_modelos():
    print("----- CADASTRO -----")
    lista_de_marcas.append(ler_marca("...Digite a marca: "))
    lista_de_modelo.append(modelo_valido("...Digite o novo modelo: "))

def ler_marca(mensagem):
    return input(mensagem).upper()

def modelo_valido(mensagem):
    while True:
        modelo = input(mensagem).upper()
        if modelo in lista_de_modelo:
            input("---Erro. Modelo já existente. [Enter]")
            continue
        return modelo




#=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-  02
def relatorio_de_marcas_e_modelos():
    print("----- RELATORIO GERAL -----")
    for ind in range(len(lista_de_modelo)):
        print(f"    Marca: {lista_de_marcas[ind].ljust(5)} Modelo: {lista_de_modelo[ind]}")
    input("[Enter] Continua.")




#=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-  03
def alterar_marca():
    print("----- ALTERAÇÃO DE MARCAS -----")
    marca_a_ser_alterada = validar_marca("...Digite a marca a ser alterada: ")
    nova_marca           = ler_marca("...Digite a marca correta: ")

    for marca in lista_de_marcas:
        if marca == marca_a_ser_alterada:
            lista_de_marcas[lista_de_marcas.index(marca_a_ser_alterada)] = nova_marca

def validar_marca(mensagem):
    while True:
        marca = ler_marca(mensagem)    #input(mensagem).upper()
        if marca in lista_de_marcas:
            return marca
        input("---Erro. Marca não existe. [Enter]")




#=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-  04
def alterar_modelo():
    print("----- ALTERAÇÃO DE MODELOS -----")
    lista_de_modelo[indice()] = modelo_valido("...Digite o novo modelo: ")

def indice():
    while True:
        modelo_velho = input("...Digite o modelo a ser alterado: ").upper()
        if modelo_velho in lista_de_modelo:
            return lista_de_modelo.index(modelo_velho)
        input("---Erro. Modelo não existente. [Enter]")




#=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-  05
def relatorio_por_marca():
    marca_escolhida = marca_valida("... Digite uma marca: ")
    print("----- RELATÓRIO DE MODELOS POR MARCA -----")
    print("-----Os Modelos desta mara são:")
    for ind, marca in enumerate(lista_de_marcas):
        if marca == marca_escolhida:
            print("\t-",lista_de_modelo[ind])
    input("[Enter]")

def marca_valida(mensagem):
    while True:
        marca = ler_marca(mensagem)
        if marca in lista_de_marcas:
            return marca
        input("---Erro. Marca não encontrada. [Enter] ")





#=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-  06
def escluir_marca():
    print("----- EXCLUIR MARCA -----")
    marca_a_excluir = marca_valida("...Digite a marca a ser excluida: ")   #ler_marca("...Digite a marca a ser excluida: ")
    for ind, marca in enumerate(lista_de_marcas):
        if marca == marca_a_excluir:
            lista_de_marcas.pop(ind)
            lista_de_modelo.pop(ind)
    input("...Exclusão realizada. [Enter] ")



# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Programa principal
while True:
    escolha = input('''
    Menu
        0-	Finalizar o Programa
        1-	Cadastrar as marcas e modelos
        2-	Listar as marcas cadastradas e modelos cadastrados
        3-	Alterar marca
        4-	Alterar modelo
        5-  Relatório por marca
        6-  Excluir uma marca da lista
    Escolha: ''')
    if escolha == "0": break
    elif escolha == '1': cadastrar_marcas_modelos()
    elif escolha == '2': relatorio_de_marcas_e_modelos()
    elif escolha == '3': alterar_marca()
    elif escolha == '4': alterar_modelo()
    elif escolha == '5': relatorio_por_marca()
    elif escolha == '6': escluir_marca()
    else: input("---Erro. Escolha inválida. [Enter]")
