continuar = True
while continuar:
    nomeCompleto = input('Digite seu nome completo: ')
    totalCaracteres = len(nomeCompleto)
    totalVogais = 0
    totalConsoantes = 0
    totalMaiusculas = 0
    totalMinusculas = 0

    for char in nomeCompleto:
        if (char.upper() in 'AEIOU'):
            totalVogais += 1
        elif (not (char in ' ')):
            totalConsoantes += 1
        if (char == char.upper() and not (char in ' ')):
            totalMaiusculas += 1
        elif (char == char.lower() and not (char in ' ')):
            totalMinusculas += 1
        


    print(f'Vogais: {totalVogais}')
    print(f'Consoantes: {totalConsoantes}')
    print(f'Maiúsculas: {totalMaiusculas}')
    print(f'Minúsculas: {totalMinusculas}')
    print(f'Total de caracteres: {totalCaracteres}')

    continuar = input('Deseja Continuar? [S]im [N]ão: ').upper() == 'S'