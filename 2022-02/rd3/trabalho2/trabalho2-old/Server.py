from socket import *
import datetime, os, pathlib

def current_date():
    return datetime.datetime.now().strftime('%d/%m/%y')

def current_time():
    return datetime.datetime.now().strftime('%H:%M:%S')

def log(message, type_message = 'INFO'):
    color_message = '\033[39m' #RESET
    if (type_message == 'INFO'):
        color_message = '\033[34m' #BLUE
    elif(type_message == 'SERVER'):
        color_message = '\033[31m' #RED
    # '\033[32m' GREEN
    print(f'{color_message}{current_date()} - {current_time()} {type_message} -> {message}')

def concat(array):
    r = ''
    for a in array:
        r += a
    return r

def current_directory():
    path = os.getcwd()
    files = []
    pathSplit = path.split('\\')
    currentFolder = pathSplit[len(pathSplit)-1]
    
    for file in pathlib.Path('.').iterdir():
        if file.is_file():
            files.append(file.name)

    r = concat([f'\nInformações do Diretório Atual: {path}',
                f'\nQuantidade de arquivos: {len(files)}',
                f'\nArquivos: {files}',
                f'\nUnidade de Disco: {path[0:2]}',
                f'\nPasta Atual: {currentFolder}'])
    #r = f'\nInformações do Diretório Atual: {path}\nQuantidade de arquivos: {len(files)}\nArquivos: {files}\nUnidade de Disco: {path[0:2]}\nPasta Atual: {currentFolder}'

    return r

myHost = 'localhost'
myPort = 50007

socketServer = socket(AF_INET,SOCK_STREAM)
socketServer.bind((myHost, myPort))

client_number = 0

recv = b''

while recv != b'Q': 
    socketServer.listen(1)
    
    log('Listening...', 'SERVER')
    connection, address = socketServer.accept()
    client_number += 1
    log('Connected', 'SERVER')
    ip = address[0]
    id = address[1]

    log(ip)
    log(id)
    log(f'Client connected: {client_number}')

    recv = connection.recv(1024)
    log('Client message received')
    
    #'[1] Informações do Diretório Atual\n'
    #'[2] Ping\n'
    send = b'Opcao invalida'
    if (recv == b'1'):
        send = current_directory().encode('UTF-8') 
    elif (recv == b'2'):
        send = b'' 
    
    if (recv == b'Q'):
        log(f'Client {ip} requested server shutdown', 'SERVER')
    else:
        connection.send(send)
        log('Sending the requested information to the client', 'SERVER')

    connection.close()