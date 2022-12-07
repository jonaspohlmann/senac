from socket import *

serverHost = "localhost"
serverPort = 50007

#Mensagem da requiscao pronta
#msg = [b'Sextou']
#troca hipotetica
### inserir / trocar a linha 7 por um input


### DAQUI ATÉ LINHA 19 - LOGISTICA DE CRIACAO E PEDIDO DE CONEXAO ####
#Criar o objeto socket do cliente 
socketClient = socket(AF_INET, SOCK_STREAM) #SOCKET IP/TCP
print('Cliente solicitando conexão com o servidor ...')
#cliente solicita conexao com o servidor
socketClient.connect((serverHost, serverPort))
print('Cliente conectado com o servidor ...')
#######################################################################


#conexao aceita
#msg precisa ser enviada para o servidor
while True:
    mensagem = input("Cliente diz: ") 
    socketClient.send(mensagem.encode("utf-8"))
    #depois que ele manda a msg, ele aguarda por uma resposta do servidor
    msgServidor = socketClient.recv(1024)
    print("Servidor disse: ", msgServidor.decode("utf-8"))

#Encerrando a conexao 
socketClient.close()