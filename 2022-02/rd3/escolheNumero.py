numeros = []

numeros.append(int(input("Digite um valor: ")))
numeros.append(int(input("Digite um valor: ")))
numeros.append(int(input("Digite um valor: ")))
numeros.append(int(input("Digite um valor: ")))
numeros.append(int(input("Digite um valor: ")))

print(f"Lista: {numeros}")
numeroEscolhido = int(input("Número desejado: "))
print(f"--> Saída {numeros[numeroEscolhido-1]}")