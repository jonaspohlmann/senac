
#minha função
def minhaFuncao(idade):
    if idade < 14:
        resultado = "Criança"
    elif idade < 18:
        resultado = "Adolescente"
    elif idade < 65:
        resultado = "Adulto"
    else:
        resultado = "Idoso"
    return resultado
    
#programa principal
seuNome = input("Digite seu nome: ")
suaIdade = int(input("Digite sua idade:"))
print(seuNome, "você é", minhaFuncao(suaIdade))
