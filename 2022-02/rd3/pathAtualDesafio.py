import os, pathlib

autenticado = False

def diretorioAtual(usuario):
    caminho = os.getcwd()
    arquivos = []
    caminhoSplit = caminho.split("\\")
    pastaAtual = caminhoSplit[len(caminhoSplit)-1]
    
    for arquivo in pathlib.Path(".").iterdir():
        if arquivo.is_file():
            arquivos.append(arquivo.name)
    
    print(f"Diretório atual: {caminho}")
    print(f"Quantidade de arquivos: {len(arquivos)}")
    print(f"Arquivos: {arquivos}")
    print(f"Unidade de Disco: {caminho[0:2]}")
    print(f"Nome de Usuário: {usuario}")
    print(f"Pasta Atual: {pastaAtual}")

while not autenticado:
    print("##### Seja Bem vindo ######")
    usuario = input("Usuário: ")
    senha = input("Senha: ")
    
    if usuario == "root" and senha == "redes":
        diretorioAtual(usuario)
    