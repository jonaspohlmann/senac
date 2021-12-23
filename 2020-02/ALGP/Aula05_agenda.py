agenda = {}

def inserir(chave,valor)
    agenda[chave] = valor

def mostrar_agenda():
    print(agenda)

# inserir dados na agenda
'''nome = input("Nome: ")
telefone = input("Telefone: ")
agenda[nome] = [telefone]

print(agenda)

nome = input("Nome: ")
telefone = input("Telefone: ")
agenda[nome] = telefone

print(agenda)'''

inserir("ana", "11111")
mostrar_agenda()

