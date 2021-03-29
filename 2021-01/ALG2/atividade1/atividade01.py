'''
Construir um algoritmo que contenha 3 listas:
•  Nomes de produtos
•  Preços de cada produto
•  Quantidades de cada produto
Construir uma função para imprimir um dos produtos da lista e uma função para retirar um dos produtos das listas

'''
nomeProdutos = ["COCACOLA", "GUARANÁ", "PEPSI", "FANTA", "SPRITE"]
precoProdutos = [0.10, 0.15, 0.20, 0.25, 0.30]
qtdProdutos = [10, 15, 20, 25, 30]

def imprimirNomesProdutos():
    for nomeProduto in nomeProdutos:
        print(nomeProduto)

def imprimirProdutoDetalhado(nome):
    i = nomeProdutos.index(nome)
    print(f"Nome: {nomeProdutos[i]}\tPreço: {precoProdutos[i]}\tQuantidade: {qtdProdutos[i]}")

def deletarProduto(nome):
    i = nomeProdutos.index(nome)
    nomeProdutos.pop(i)
    precoProdutos.pop(i)
    qtdProdutos.pop(i)
    print("Produto deletado com sucesso")

def inputEnter():
    input("Aperte [ENTER] para continuar")

opcao = -1
menu = f"1 - Detalhar Produto\n2 - Deletar Produto\n0 - Sair do programa"
while (opcao != 0):
    print(menu)
    opcao = int(input("Digite a opção desejada: "))

    if (opcao == 1):
        imprimirNomesProdutos()
        imprimirProdutoDetalhado(input("Digite o nome do produto a ser detalhado: ").upper())
        inputEnter()
    elif (opcao == 2):
        imprimirNomesProdutos()
        deletarProduto(input("Digite o nome do produto a ser deletado: ").upper())
        inputEnter()