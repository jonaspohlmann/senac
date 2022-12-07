#
from socket import *
TEST_MODE = True
FILE_MODE = False

def print_menu():
    if (FILE_MODE):
        menu_file = 'Receber dados em tela'
    else:
        menu_file = 'Receber dados via arquivo'
    return input('Escolha a opção desejada: \n'
                 '[1] Informações do Diretório Atual\n'
                 '[2] Ping\n'
                f'[F] {menu_file}\n'
                 '[S] Sair\n'
                 '[Q] Sair e desligar servidor\n'
                 '').upper()

def file_mode():
    if (FILE_MODE):
        input('')


def authentication():
    print('Autenticação: ')
    if (TEST_MODE):
        login = 'gerente'
        senha = '123'
    else:
        login = input('Login: ')
        senha = input('Senha: ')
    if (login == 'gerente' and senha == '123'):
        print('Usuário autenticado com sucesso.')
        return True
    else:
        print('Usuário ou senha incorretos')
        return False

serverHost = "localhost"
serverPort = 50007

menu = '0'

authenticated = False
authenticated = authentication()

while (authenticated and (menu not in ['S', 'Q'])):
    menu = print_menu()
    if (menu == 'F'):
        FILE_MODE = not FILE_MODE
    elif (menu not in ['S']):
        send = menu.encode(encoding='UTF-8')

        socketClient = socket(AF_INET, SOCK_STREAM)
        socketClient.connect((serverHost, serverPort))
        socketClient.send(send)

        recv = socketClient.recv(1024)
        if (FILE_MODE):
            continue
        else:
            print(recv.decode(encoding='UTF-8'))
        socketClient.close()