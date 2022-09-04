class Aluno:

    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf 
        self.__nota1 = None
        self.__nota2 = None
        self.__nota3 = None
    
    def calcularMedia(self):
        return (self.__nota1 + self.__nota2 + self.__nota3) / 3
    
    def __notaValida(self, nota):
        if nota < 0:
            return 0
        if nota > 10:
            return 10
        return nota
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf 
    
    @property
    def nota1(self):
        return self.__nota1
    
    @nota1.setter
    def nota1(self, nota1):
        self.__nota1 = self.__notaValida(nota1)
    
    @property
    def nota2(self):
        return self.__nota2
    
    @nota2.setter
    def nota2(self, nota2):
        self.__nota2 = self.__notaValida(nota2)
    
    @property
    def nota3(self):
        return self.__nota3
    
    @nota3.setter
    def nota3(self, nota3):
        self.__nota3 = self.__notaValida(nota3)
    
listaAlunos = []
while True:
    nome = input("Digite seu nome: ")
    if nome == "fim":
        break
    cpf = input("DIgite seu cpf: ")

    aluno = Aluno(nome, cpf)

    aluno.nota1 = float(input("Digite a nota 1: "))
    aluno.nota2 = float(input("Digite a nota 2: "))
    aluno.nota3 = float(input("Digite a nota 3: "))

    listaAlunos.append(aluno)

mediaturma = 0
for aluno in listaAlunos:
    mediaturma += aluno.calcularMedia()

print(f"Média da Turma: {mediaturma/len(listaAlunos)}")
    
for alunos in listaAlunos:
    print(f"Aluno: {alunos.nome}\n CPF: {alunos.cpf}\n Média do Aluno: {aluno.calcularMedia()}")

