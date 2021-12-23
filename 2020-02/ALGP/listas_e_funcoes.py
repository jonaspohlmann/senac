lista_nomes   = ['Pedro','Ana','Guilherme','Carla','Julia']
lista_bebidas = ['CocaCola','Guarana','CocaCola','Pepsi','Sprite']

# Exercício 1
# Desenvolva uma função que receba como parâmetro o nome da bebida e 
# Imprima todas pessoas que gostam desta bebida. 

def pessoasQueGostam(bebida):
    pessoasQueGostam = []
    for i in range(len(lista_bebidas)):
        if lista_bebidas[i] == bebida:
            pessoasQueGostam.append(lista_nomes[i])
    print(*pessoasQueGostam, sep=" - ")

pessoasQueGostam('CocaCola')

# Exercício 2
# Desenvolva uma função que receba como parâmetro o nome e a bebida preferida
# de uma pessoa e insira esses dados nas listas.

# Exercício 3
# desenvolva uma função que retorne o nome da bebida que é mais preferida.

def bebidaPreferida():
    countBebidaFavorita = 0
    bebidaFavorita = ''
    lista_bebidas_set = sorted(set(lista_bebidas))
    for bebida in lista_bebidas_set:
        if lista_bebidas.count(bebida) > countBebidaFavorita:
            countBebidaFavorita = lista_bebidas.count(bebida)
            bebidaFavorita = lista_bebidas_set[lista_bebidas_set.index(bebida)]
    print(bebidaFavorita)

bebidaPreferida()