'''
Construa um algoritmo para implementar a classe Aluno que contém os atributos código, nome e matrícula. 
A classe Aluno possui duas subclasses, sendo a classe AlunoEnsinoMedio, que tem o atributo ano como seu atributo próprio e a 
classe AlunoGraduacao que tem o atributo semestre como atributo próprio. As duas subclasses herdam todos atributos da classe Aluno. 
As três classes possuem o método construtor e também o método imprimir, que imprime na tela os valores de todos os atributos da sua 
respectiva classe.
'''

def inputEnter():
    input(f"Aperte [ENTER] para continuar\n")

class Aluno:
    def __init__(self, codigo, nome, matricula):
        self.codigo = codigo
        self.nome = nome
        self.matricula = matricula

    def imprimir(self):
        print(f"{self.codigo}, {self.nome}, {self.matricula}")
        inputEnter()

class AlunoEnsinoMedio(Aluno):
    def __init__(self, codigo, nome, matricula, ano):
        Aluno.__init__(self, codigo, nome, matricula)
        self.ano = ano

    def imprimir(self):
        print(f"Código: {self.codigo}\nNome: {self.nome}\nMatrícula: {self.matricula}\nAno: {self.ano}")
        inputEnter()


class AlunoGraduacao(Aluno):
    def __init__(self, codigo, nome, matricula, semestre):
        Aluno.__init__(self,codigo, nome, matricula)
        self.semestre = semestre

    def imprimir(self):
        print(f"Código: {self.codigo}\nNome: {self.nome}\nMatrícula: {self.matricula}\nSemestre: {self.semestre}")
        inputEnter()

def cadastrarAlunoEnsinoMedio():
    codigo = input("Digite o código: ").upper()
    nome = input("Digite o nome: ").upper()
    matricula = input("Digite a matrícula: ").upper()
    ano = input("Digite o ano: ")
    return AlunoEnsinoMedio(codigo, nome, matricula, ano)

def cadastrarAlunoGraduacao():
    codigo = input("Digite o código: ").upper()
    nome = input("Digite o nome: ").upper()
    matricula = input("Digite a matrícula: ").upper()
    semestre = input("Digite o semestre: ")
    return AlunoGraduacao(codigo, nome, matricula, semestre)

opcao = -1
menu = f"1 - ALUNO DE ENSINO MEDIO\n2 - ALUNO DE GRADUAÇÃO\n0 - Sair do programa"

while (opcao != 0):
    print(menu)
    opcao = int(input("Digite a opção desejada: "))

    if (opcao == 1):
        alunoEnsinoMedio = cadastrarAlunoEnsinoMedio()
        alunoEnsinoMedio.imprimir()
    elif (opcao == 2):
        alunoGraduacao = cadastrarAlunoGraduacao()
        alunoGraduacao.imprimir()