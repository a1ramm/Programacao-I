class Funcionario: 

    def __init__(self, nome, salario, codigoCargo):
        self.nome = nome
        self.salario = salario
        self.codigoCargo = codigoCargo
    
    def aumentarSalario(self, porcentualDeAumento):
        self.salario *= (porcentualDeAumento / 100) + 1
    
listafuncionarios = []
while True:
    nome = input("Digite seu nome: ")
    if nome == "":
        break
    salario = float(input("Digite seu salário: "))
    codigoCargo = int(input("Digite seu código de cargo: "))
        
    funcionario = Funcionario(nome, salario, codigoCargo)
    listafuncionarios.append(funcionario)

somasalarios = 0
for funcionario in listafuncionarios:
    somasalarios += funcionario.salario
print(f"Soma de todos os salários: {somasalarios}")

somasalariosaumento = 0
for funcionario in listafuncionarios:
    if funcionario.codigoCargo == 1:
        funcionario.aumentarSalario(5)
    elif funcionario.codigoCargo == 2:
        funcionario.aumentarSalario(10)
    else:
        funcionario.aumentarSalario(8)
    somasalariosaumento += funcionario.salario
print(f"Soma de todos os salários mais aumento: {somasalariosaumento}")