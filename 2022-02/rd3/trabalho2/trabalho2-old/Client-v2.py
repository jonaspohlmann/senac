'''
realiza a conexão com o server
verifica o menu e envia a requisição
recebe a resposta, sinaliza o recebimento
fecha conexão
'''
from socket import *

server_host = "localhost"
server_port = 50007

def recv_decode(bytes):
    retorno = bytes.decode(encoding='UTF-8')
    retorno = retorno.split('inputinput')
    
    if len(retorno) == 2:
        return input(retorno[1])
    return retorno[0]

def send_encode(string, input=False):
    return string.encode(encoding='UTF-8')

while True:
    socketClient = socket(AF_INET, SOCK_STREAM)
    socketClient.connect((server_host, server_port))
    recv = recv_decode(socketClient.recv(1024))
    #socketClient.send(recv.decode(encoding='UTF-8'))
    socketClient.close()

