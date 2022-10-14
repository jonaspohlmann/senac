from subprocess import PIPE, Popen
import utils
from datetime import datetime

path = 'C:/workspace-pessoal/senac/2022-02/rd3/trabalho1'

def execute_cmd(cmd):
    process = Popen(args=cmd, stdout=PIPE, shell=True, encoding='latin1', universal_newlines=True)
    return process

start_program = True
values = [] #url, ip, status, time

def result(values):
    file = ''
    file += utils.print_OS('URL | IP | Status | Data | Hora', ' ') + '\r\n'
    for value in values:
        file += utils.print_OS(f'{value[0]} | {value[1]} | {value[2]} | {value[3]}', ' ') + '\r\n'
    save_file(file)

def save_file(texto):
    file = open(f'{path}/logIps.txt','w')
    file.seek(0)
    file.write(str(texto))
    file.close()

utils.print_OS('Bem Vindo')
file = open(f'{path}/arquivo.txt','r')
for line in file:
    if utils.not_is_Empty(line):
        url = line.rstrip()
        ping = ''

        utils.print_OS(f'PINGANDO URL: {url}')
        ping = execute_cmd(['ping', '-n', '4', url]).communicate()[0]
        print(ping)

        #valor entre os colchetes []
        ip = ping[ping.find('[')+1:ping.find(']')]

        status = ''
        time = datetime.now().strftime('%H:%M')
        if (ping.find('Recebidos = 4') != -1):
            status = 'ATIVO'
        else:
            status = 'INATIVO'
            ip = 'N/A'

        utils.print_OS('URL | IP')
        utils.print_OS(f'{url} | {ip}')
        values.append([url, ip, status, time])

result(values)
utils.print_OS('FIM DE PROGRAMA')

