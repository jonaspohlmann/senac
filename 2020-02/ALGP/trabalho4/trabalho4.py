lista_alunos = []
lista_cidades = []

def inputEnter():
    input("Digite [ENTER] para continuar")

class Aluno:
    def __init__(self, nome, telefone, cidade):
        self.nome = str(nome).upper()
        self.telefone = str(telefone).upper()
        self.cidade = cidade
    
    def getNome(self):
        return self.nome
    def setNome(self, nome):
        self.nome = nome

    def getTelefone(self):
        return self.telefone
    def setTelefone(self, telefone):
        self.telefone = telefone

    def getCidade(self):
        return self.cidade
    def setCidade(self, cidade):
        self.cidade = cidade
    
    def getNomeCidade(self):
        return self.cidade.getNome()
    
    def getEstadoCidade(self):
        return self.cidade.getEstado()
    

class Cidade:
    def __init__(self, nome, estado):
        self.nome = str(nome).upper()
        self.estado = str(estado).upper()

    def getNome(self):
        return self.nome
    def setNome(self, nome):
        self.nome = nome
    
    def getEstado(self):
        return self.estado
    def setEstado(self, estado):
        self.estado = estado

def procurarCidade(nome):
    for cidade in lista_cidades:
        if cidade.getNome() == nome:
            return cidade
    return None   

def selecionarCidade():
    for cidade in lista_cidades:
        print(f"{cidade.getNome()} - {cidade.getEstado()}")
    nome = input("Digite o nome da cidade: ").upper()
    return procurarCidade(nome)

def listarAlunoPorCidade(cidade):
    for aluno in lista_alunos:
        if aluno.getCidade() == cidade:
            print(f"{aluno.getNome()} - {aluno.getTelefone()} - {aluno.getNomeCidade()} - {aluno.getEstadoCidade()}")

def cadastrarCidade():
    nome = input("Digite o nome da cidade: ")
    estado = input("Digite o estado da cidade: ")

    lista_cidades.append(Cidade(nome, estado))

    print("Cidade cadastrada com sucesso!")
    inputEnter()

def cadastrarAluno():
    nome = input("Digite o nome do aluno: ")
    telefone = input("Digite o telefone do aluno: ")
    cidade = selecionarCidade()
    
    lista_alunos.append(Aluno(nome, telefone, cidade))

    print("Aluno cadastrado com sucesso!")
    inputEnter()

def relatorioAluno():
    for aluno in lista_alunos:
        print(f"{aluno.getNome()} - {aluno.getTelefone()} - {aluno.getNomeCidade()} - {aluno.getEstadoCidade()}")
    inputEnter()

def relatorioCidade():
    for cidade in lista_cidades:
        print(f"{cidade.getNome()} - {cidade.getEstado()}")
    inputEnter()

def relatorioAlunoPorCidade():
    cidade = selecionarCidade()
    listarAlunoPorCidade(cidade)
    inputEnter()

#Menu
def menuPrincipal():
    print("MENU")
    return int(input('''    0- Finalizar o Programa
    1- Cadastrar Cidades
    2- Cadastrar Alunos
    3- Relatório de Alunos
    4- Relatório de Cidades
    5- Relatório de Alunos por cidade
Escolha: '''))


try:
    menu = -1
    while (menu != 0):
        
        print(lista_alunos)
        print(lista_cidades)

        menu = menuPrincipal()
        if (menu < 0 and menu > 5):
            print("Opção inválida!") 
            inputEnter()
        else:
            if menu == 1:
                cadastrarCidade()
            elif menu == 2:
                cadastrarAluno()
            elif menu == 3:
                relatorioAluno()
            elif menu == 4:
                relatorioCidade()
            elif menu == 5:
                relatorioAlunoPorCidade()
except:
    #pass
    raise
