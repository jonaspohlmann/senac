from socket import *
import socketserver
import datetime

#fazendo uma funcao generica que pega a data formatada 
def currentDate(): #currentDate
    return datetime.datetime.today().date().strftime('%d/%m/%y')



#nome host
myHost = 'localhost'

#porta
myPort = 50007

#Etapas 
#1. Criar um socket - objeto
#Duas constantes sao necessarias: 
#1. Familia do endereco (AF_INET)
#2. Indicar se o stream da conversa eh padrao ou datagram: padrao SOCK_STREAM
    # Padrão: SOCK_STREAM --> utilizado
    # Datragram (UDP): SOCK_DGRAM

#Configuracoes necessarias: 
# Protocolo IP - AF_INET
# Protocolo da camada de transporte (TCP - UDP): SOCK_STREAM


### AGORA PODEMOS CRIAR O NOSSO SOCKET SERVER (QUE EH UM OBJETO)
socketServer = socket(AF_INET,SOCK_STREAM) #combinacao = Server TCP/IP


##Depois de criado e configurado o Socket do Servidor, 
# precisa vincular ele com porta e host
socketServer.bind((myHost, myPort))

#criando a variável contador
contador = 0 

while True: #para que ele fique sempre escutando  
    # Socket server criado, socket vinculado a um host e a uma porta 
    # Socket apto para comecar a escutar
    socketServer.listen(1)
    #Na escuta
    print("Servidor na escuta...")

    #Aceita as solicitacoes?! 
    #se sim, retorna o -id- do cliente que pediu a conexao
    connection, address = socketServer.accept()
    contador += 1
    #verificando com quem o servidor se conectou
    print('Server connected: ', id)
    #'127.0.0.1', 62124
    ip = address[0]
    id = address[1]

    #data = currentDate()
    print("###### Data: ", currentDate())
    print("###### IP: ", ip)
    print("###### ID: ", id)
    print('Cliente Conectado: ', contador)
    ##################################################
    

    ##### ENVIO E RECEBIMENTO DE MSGS DO SERVER ACONTECE AQUI 
    while True: #estrutura de envio e recebimento de msgs entre servidor e cliente
        msgRecv = connection.recv(1024).decode("utf-8")
        print("Cliente disse: ", msgRecv)
        msgSend = input("Servidor diz: ")
        connection.send(msgSend.encode("utf-8"))

    connection.close() 


    ''''
    ##neste momento ja temos um cliente em conexao com ele 
    # recebe msg enviada pelo cliente - primeira vez 
    msg = connection.recv(1024)

    #recebeu msg do cliente
    print("Servidor diz: Mensagem do cliente recebida com sucesso")

    #Papel do servidor aqui: dar um 'echo' na msg que recebe do cliente
    #enviar a msg com o echo para o cliente
    connection.send(b'Echo =>' + msg)
    '''
   
    print("Servidor diz: Solicitacao atendida!")

    #fecha conexao 
    connection.close()




