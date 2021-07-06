"""
Construa o algoritmo em Python de uma lista duplamente encadeada que possui uma função para inserir elementos, uma para
imprimir os elementos na ordem que foram inseridos e uma função para imprimir os elementos na ordem inversa a que foram
inseridos.
"""

# Imports
from Classes.Pilha import Pilha
from ClassesAuxiliares.AuxMethods import AuxMethods
from ClassesAuxiliares.FormatFonts import FormatFonts
from ClassesAuxiliares.Messages import Messages

pilha = Pilha()
aux = AuxMethods()
fonte = FormatFonts()
msg = Messages()

# Constantes para centralizar o nome dos menus
MENU = 'MENU'
ADICIONAR = 'ADICIONAR ITEM NA PILHA'
REMOVER = 'REMOVER ITEM NA PILHA'
IMPRIMIR = 'IMPRIMIR PILHA'


# Métodos referentes as opções dos menus
def menu(desc_menu):
    aux.clear_screen_menu(desc_menu)

    return input(f'''
    {fonte.green('0.')} Finalizar o programa
    {fonte.green('1.')} Adicionar ao topo
    {fonte.green('2.')} Remover do topo
    {fonte.green('3.')} Imprimir topo da Pilha

Escolha a opção desejada: ''')


def adicionar_item(desc_menu):
    aux.clear_screen_menu(desc_menu)
    aux.insert_line()

    add = aux.input_int(f'Informe um número: ')
    pilha.adicionar(add)

    aux.print_message('Número adicionado ao topo da pilha com sucesso.')
    aux.press_enter()


def remover_item(desc_menu):
    aux.clear_screen_menu(desc_menu)
    aux.insert_line()

    if pilha.__len__() == 0:
        print('A lista está vazia.')
    else:
        pilha.remover()
        print('Número removido do topo da pilha com sucesso.')
    aux.press_enter()


def imprimir(desc_menu):
    aux.clear_screen_menu(desc_menu)
    aux.insert_line()

    if pilha.__len__() == 0:
        print('A lista está vazia.')
    else:
        print('O topo da lista é:')
        pilha.imprimir_topo()

        aux.print_message('Itens da lista:')
        print(pilha)
    aux.press_enter()


# Programa
while True:
    opcao = menu(MENU)

    if opcao == '0':
        aux.finish_program(MENU)
        break
    elif opcao == '1':
        adicionar_item(ADICIONAR)
    elif opcao == '2':
        remover_item(REMOVER)
    elif opcao == '3':
        imprimir(IMPRIMIR)
    else:
        aux.invalid_option(MENU)
