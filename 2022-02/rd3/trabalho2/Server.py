from socket import *
from datetime import datetime, timedelta
from subprocess import PIPE, Popen
import pathlib, re, os, psutil

TEST_MODE = False
FILE_MODE = False
LOGIN_TIMEOUT = 900

PRINT = '[PRINT]'
ENTER = '[ENTER]'

RESET = ['RESET', '\033[39m']
INFO = ['INFO', '\033[34m']
ERROR = ['ERROR', '\033[31m']
SUCCESS = ['SUCCESS', '\033[32m']
FUNCTION = ['FUNCTION', '\033[35m']

host = 'localhost'
port = 50007

#ip = auth[0] 
#date = auth[1]
auths = []
request_auth = True
authenticated = False
path = f'{pathlib.Path().resolve()}\\trabalho2'
log_file = []

menu_option = ''
client_count = 0

def current_date():
    return datetime.now().strftime('%d/%m/%y')

def current_time():
    return datetime.now().strftime('%H:%M:%S')

def log(message, type_message = INFO):
    returnn = f'{current_date()} - {current_time()} SERVER {type_message[0]} -> {message}'
    log_file.append(returnn)
    print(f'{type_message[1]}{returnn}{RESET[1]}')

def decode(bytes):
    return bytes.decode(encoding='UTF-8')

def encode(string, option = ''):
    string = f'{option}{string}'
    return string.encode(encoding='UTF-8')

def request_auth(ip):
    log('Looking for authentication')
    i = 0
    request_auth = True

    for auth in auths:
        ip_auth = auth[0] 
        date_auth = auth[1]
        if (ip == ip_auth):
            log('IP found')
            timeout = date_auth + timedelta(seconds=LOGIN_TIMEOUT)
            if (datetime.now() >= timeout):
                log('TIMEOUT HAS EXPIRED', ERROR)
                auths.pop(i)
            else:
                request_auth = False
        i += 1
    return request_auth

def authentication(username, password):
    if (TEST_MODE):
        username = 'gerente'
        password = '123'
    if (username == 'gerente' and password == '123'):
        auths.append([ip, datetime.now()])
        return True
    return False

def concat(array):
    returnn = ''
    index = 0
    char = '\n'
    last_index = len(array)-1

    for a in array:
        if (index == last_index):
            char = ''
        returnn += f'{a}{char}'
        index += 1
    return returnn

def print_menu():
    if (FILE_MODE):
        menu_file = 'Receber dados em tela'
    else:
        menu_file = 'Receber dados via arquivo'
    return concat(['MENU',
                 '[1] Informações do Diretório Atual',
                 '[2] Ping',
                 '[3] Uso de CPU',
                 '[4] Uso de RAM',
                f'[F] {menu_file}',
                 '[S] Sair',
                 '[Q] Sair e desligar servidor',
                 'Escolha a opção desejada: '])

def current_directory():
    files = []
    pathSplit = path.split('\\')
    currentFolder = pathSplit[len(pathSplit)-1]
    
    for file in pathlib.Path(path).iterdir():
        if file.is_file():
            files.append(file.name)
    
    returnn = concat([f'Informacoes do Diretorio Atual: {path}',
                f'Quantidade de arquivos: {len(files)}',
                f'Arquivos: {files}',
                f'Unidade de Disco: {path[0:2]}',
                f'Pasta Atual: {currentFolder}'])

    if (FILE_MODE):
        log('Save file saida_diretorio.txt', SUCCESS)
        save_file('saida_diretorio.txt', returnn, True)
        return ''
    else:
        log('Current directory date successfully exported', SUCCESS)
        return returnn

def ping(url):
    ping = Popen(args=['ping', '-n', '4', url], stdout=PIPE, shell=True, encoding='latin1', universal_newlines=True).communicate()[0]

    begin = re.search(r'\[', ping).span()[0]+1
    end = re.search(r'\]', ping).span()[0]
    ip = ping[begin:end]

    if (re.search(r'Perdidos = 4', ping)):
        status = 'INATIVO'
        ip = 'N/A'
    else:
        status = 'ATIVO'
    returnn = concat([f'URL: {url}',
                      f'IP: {ip}',
                      f'Status: {status}',
                      f'Data: {current_date()}',
                      f'Hora: {current_time()}'])

    if (FILE_MODE):
        log('Save file saida_ping.txt', SUCCESS)
        save_file('saida_ping.txt', returnn, True)
        return ''
    else:
        log('Ping date successfully exported', SUCCESS)
        return returnn    

def save_file(file, text, replace=False):
    if (replace): 
        mode = 'w'
    else: 
        mode = 'w'
    file = open(f'{path}\{file}', mode)
    if (not replace): 
        file.truncate(0)
    file.write(text + "\n")
    file.close()

def ram():
    return concat(['MEMORIA RAM',
                      f'TOTAL: {round(psutil.virtual_memory()[0]/1000000000, 2)} GB',
                      f'Usado: {round(psutil.virtual_memory()[3]/1000000000, 2)} GB',
                      f'Usado: {round(psutil.virtual_memory()[2], 2)} %',
                      f'Livre: {round(psutil.virtual_memory()[4]/1000000000, 2)} GB'])

def cpu():
    return f'CPU USADO: {round(psutil.cpu_percent(4), 2)} %'

try:
    socketServer = socket(AF_INET,SOCK_STREAM)
    socketServer.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    socketServer.bind((host, port))
    log('Listening...')
    socketServer.listen(5)
    connection, address = socketServer.accept()
    client_count += 1

    while (menu_option.upper() not in ['Q']): 
        log('Connected')
        ip = address[0]
        id = address[1]

        log(f'IP: {ip}')
        log(f'ID: {id}')
        log(f'Client number: {client_count}')

        ###AUTHENTICATION####
        if (request_auth(ip)):
            log('Request authentication')
            connection.send(encode('Autenticacao', PRINT))
            connection.send(encode('Login: '))
            username = decode(connection.recv(1024))
            connection.send(encode('Password: '))
            password = decode(connection.recv(1024))

            authenticated = authentication(username, password)
            if (authenticated):
                log('Authenticated', SUCCESS)
                connection.send(encode('Autenticacao concluida com sucesso', PRINT))
            else:
                connection.send(encode('Acesso negado', PRINT))
        else:
            authenticated = True
        

        if (authenticated):
            connection.send(encode(print_menu()))
            menu_option = decode(connection.recv(1024)).upper()

            ###CURRENT_DIRECTORY####
            if (menu_option == '1'):
                log('START CURRENT_DIRECTORY', FUNCTION)
                connection.send(encode(current_directory(), ENTER))
                log('END CURRENT_DIRECTORY', FUNCTION)

            ###PING####
            elif (menu_option == '2'):
                log('START PING', FUNCTION)
                connection.send(encode('PING', PRINT))
                connection.send(encode('Digite a URL/IP: '))
                url = decode(connection.recv(1024))
                connection.send(encode(ping(url), ENTER))
                log('END PING', FUNCTION)

            ###CPU USAGE####
            elif (menu_option == '3'):
                log('START CPU USAGE', FUNCTION)
                connection.send(encode(cpu(), ENTER))
                log('END CPU USAGE', FUNCTION)

            ###RAM USAGE####
            elif (menu_option == '4'):
                log('START RAM USAGE', FUNCTION)
                connection.send(encode(ram(), ENTER))
                log('END RAM USAGE', FUNCTION)

            ###FILE_MODE####
            elif (menu_option == 'F'):
                FILE_MODE = not FILE_MODE
                if (FILE_MODE):
                    log('FILE_MODE ON', FUNCTION)
                else:
                    log('FILE_MODE OFF', FUNCTION)

            ###CLIENT OFF####
            elif (menu_option == 'S'):
                log('CLIENT OFF', FUNCTION)
                log('Save log file')
                save_file('log.txt', concat(log_file))
                connection, address = socketServer.accept()

            ###SERVER OFF####
            elif (menu_option == 'Q'):
                log('SERVER OFF', FUNCTION)
                continue

    connection.close()
except Exception as e:
    log(e, ERROR)
    print(e)
    connection.close()