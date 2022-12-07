from socket import *

serverHost = "localhost"
serverPort = 50007

#Mensagem da requiscao pronta
msg = [b'Sextou']

#Criar o objeto socket do cliente 
socketClient = socket(AF_INET, SOCK_STREAM) #SOCKET IP/TCP

print('Cliente solicitando conexão com o servidor ...')
#cliente solicita conexao com o servidor
socketClient.connect((serverHost, serverPort))
print('Cliente conectado com o servidor ...')


#conexao aceita
#msg precisa ser enviada para o servidor
#envio sera enviado linha por linha 
for linha in msg: 
    socketClient.send(linha)
    #depois que ele manda a msg, ele aguarda por uma resposta do servidor
    msgServidor = socketClient.recv(1024)
    print("A mensagem enviado pelo servidor foi: ", msgServidor)

#Encerrando a conexao 
socketClient.close()