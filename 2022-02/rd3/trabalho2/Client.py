'''
realiza a conexão com o server
verifica o menu e envia a requisição
recebe a resposta, sinaliza o recebimento
fecha conexão
'''
from socket import *

PRINT = '[PRINT]'
ENTER = '[ENTER]'

server_host = "localhost"
server_port = 50007

def decode(bytes):
    return bytes.decode(encoding='UTF-8')

def encode(string):
    return string.encode(encoding='UTF-8')

try:
    socketClient = socket(AF_INET, SOCK_STREAM)
    socketClient.connect((server_host, server_port))

    send = ''
    recv = ''
    while send.upper() not in ['S', 'Q']:
        recv = decode(socketClient.recv(1024))
        if (PRINT in recv):
            print(recv.replace(PRINT, ''))
        elif(ENTER in recv):
            print(recv.replace(ENTER, ''))
            input('Pressione [ENTER] para continuar')
        else:
            send = input(recv)    
            socketClient.send(encode(send))

    socketClient.close()

except Exception as e:
    print(e)
    socketClient.close()
