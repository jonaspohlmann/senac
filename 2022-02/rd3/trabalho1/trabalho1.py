from subprocess import PIPE, Popen
import utils
from datetime import datetime

def execute_cmd(cmd):
    process = Popen(args=cmd, stdout=PIPE, shell=True, encoding='latin1', universal_newlines=True)
    return process


start_program = True
values = [] #url, ip, status, time

def result(values):
    utils.print_OS('URL | IP | Status| Data| Hora', ' ')
    for value in values:
        utils.print_OS(f'{value[0]} | {value[1]} | {value[2]} | {value[3]}', ' ')


while(start_program):
    utils.print_OS('Bem Vindo')
    #url = 'google.com.br'
    url = input('Digite uma URL: ')
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

    start_program = input('Deseja Continuar? ').lower() in ['s', 'sim']

result(values)
utils.print_OS('FIM DE PROGRAMA')

