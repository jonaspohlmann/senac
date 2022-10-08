from  subprocess import PIPE, Popen

def printOS(message):
    print('-'*26 + f' {message} ' + '-'*26)

def executeCmd(cmd):
    process = Popen(args=cmd, stdout=PIPE, shell=True, encoding='latin1', universal_newlines=True)
    return process
    
startProgram = True

while(startProgram):
    printOS("Bem Vindo")
    url = 'google.com.br'
    #url = input("Digite uma URL: ")

    printOS("PINGANDO")
    ping = executeCmd(['ping', '-n', '4', url]).communicate()[0]
    print(ping)

    #valor entre os colchetes []
    ip = ping[ping.find('[')+1:ping.find(']')]

    printOS("URL | IP")
    print(' '*(30-len(url)) + url + ' | ' + ip)

    startProgram = input('Deseja Continuar? ').lower() in ['s', 'sim']

printOS('FIM DE PROGRAMA')

