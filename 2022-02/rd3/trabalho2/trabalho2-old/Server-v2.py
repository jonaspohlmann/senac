'''
menu
realiza conexão
recebe e envia a requisição
autenticação
diretório atual (current directory)
ping
'''
from socket import *
from datetime import datetime, timedelta
import threading
import os, pathlib

TEST_MODE = True
LOGIN_TIMEOUT = 900

host = 'localhost'
port = 50007

client_count = 0
thread_count = 0


#ip = auth[0] 
#date = auth[1]
auths = []

def r(array):
    r = ''
    for a in array:
        r += a
    return r

def send_encode(string, input=False):
    input = ''
    if input:
        input = 'inputinput'

    retorno = input + '' + string
    return retorno.encode(encoding='UTF-8')

def current_date():
    return datetime.now().strftime('%d/%m/%y')

def current_time():
    return datetime.now().strftime('%H:%M:%S')

def log(message, type_message = 'INFO'):
    color_message = '\033[39m' #RESET
    if (type_message == 'INFO'):
        color_message = '\033[34m' #BLUE
    elif(type_message == 'ERROR'):
        color_message = '\033[31m' #RED
    elif(type_message == 'SUCCESS'):
        color_message = '\033[32m' #GREEN
    print(f'{color_message}{current_date()} - {current_time()} {type_message} SERVER -> {message}')

def request_auth(connection, ip):
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
                log('TIMEOUT HAS EXPIRED', 'ERROR')
                auths.pop(i)
            else:
                request_auth = False
        i += 1
    if (request_auth):
        authentication(connection, ip)


def authentication(connection, ip):
    log('Request authentication')
    #connection.send(send_encode('Autenticacao: '))
    #connection.send(send_encode('Login: ', True))
    connection.send('Login: '.encode(encoding='UTF-8'))
    username = connection.recv(1024)
    connection.send(send_encode('Password: ', True))
    password = connection.recv(1024)

    if (TEST_MODE):
        username = 'gerente'
        password = '123'
    if (username == 'gerente' and password == '123'):
        auths.append([ip, datetime.now()])
        connection.send(send_encode('Autenticacao concluida com sucesso'))
        return True
    return False

socketServer = socket(AF_INET,SOCK_STREAM)
socketServer.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
socketServer.bind((host, port))
while True: 

    
    log('Listening...')
    socketServer.listen(5)
    connection, address = socketServer.accept()
    client_count += 1
    log('Connected')
    ip = address[0]
    id = address[1]

    log(f'IP: {ip}')
    log(f'ID: {id}')
    log(f'Client number: {client_count}')

    
    connection.send('Login: '.encode(encoding='UTF-8'))
    #Authentication
    authentication_handler = threading.Thread(
        target=request_auth,
        args=(connection, ip)
    )
    authentication_handler.start()
    thread_count += 1

    #request_auth(connection, ip, auths)
    
    #connection.send(send.encode('UTF-8'))
    log('Sending to the client')

    connection.close()        

    
    
    #recv = connection.recv(1024)
    #log('Client message receivssiied')
    #'[1] Informações do Diretório Atual\n'
    #'[2] Ping\n'
    #send = 'Opcao invalida'
    #if (recv == b'1'):
    #    send = current_directory().encode('UTF-8') 
    #elif (recv == b'2'):
    #    send = b'' 
    
    #if (recv == b'Q'):
    #    log(f'Client {ip} requested server shutdown')