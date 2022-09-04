class Funcionario:

    def __init__(self, nome):
        self.__nome = nome
        self.__idade = None 
        self.__salario = None
    
    def __validador(self, sla):
        if sla < 0:
            return 0
        return sla
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @property
    def idade(self):
        return self.__idade
    
    @idade.setter
    def idade(self, idade):
        self.__idade = self.__validador(idade)
    
    @property
    def salario(self):
        return self.__salario
    
    @salario.setter
    def salario(self, salario):
        self.__salario = self.__validador(salario)
    
listafuncionarios = []
while True:
    nome = input("Digite seu nome (fim para parar): ")
    if nome == "fim":
        break
    
    funcionario = Funcionario(nome)

    funcionario.idade = int(input("Digite sua idade: "))
    funcionario.salario = float(input("Digite seu salario: "))

    listafuncionarios.append(funcionario)

mediaIdades = 0
for funcionario in listafuncionarios:
    mediaIdades += funcionario.idade
print(f"Média das Idades: {mediaIdades/len(listafuncionarios)}")

funcionarioVelho = -1
for funcionario in listafuncionarios:
    if funcionario.idade > funcionarioVelho:
        funcionarioVelho = funcionario.idade
        
funcionarioMenorSalario = +100000
for funcionario in listafuncionarios:
    if funcionario.salario < funcionarioMenorSalario:
        funcionarioMenorSalario = funcionario.salario

for funcionario in listafuncionarios:
    if funcionario.idade == funcionarioVelho:
        print("Dados do funcionario mais velho")
        print(f"Nome: {funcionario.nome}")
        print(f"Idade: {funcionario.idade}")
        print(f"Salario: {funcionario.salario}")
    if funcionario.salario == funcionarioMenorSalario:
        print("Dados do funcionario com menor salario")
        print(f"Nome: {funcionario.nome}")
        print(f"Idade: {funcionario.idade}")
        print(f"Salario: {funcionario.salario}")

for funcionario in listafuncionarios:
    print("=" * 20)
    print(f"Nome: {funcionario.nome}\nIdade: {funcionario.idade}\nSalario: {funcionario.salario}")