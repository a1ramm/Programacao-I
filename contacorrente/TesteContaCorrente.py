from Cliente import Cliente
from ContaCorrente import ContaCorrente

lista = []
while True:
    numeroConta = input("Digite seu número da conta: ")
    if numeroConta == "0":
        break
    saldo = float(input("Digite seu saldo: "))
    nome = input("Digite seu nome: ")
    cpf = input("Digite seu cpf: ")

    cliente = Cliente(nome, cpf)
    contacorrente = ContaCorrente(numeroConta, saldo, cliente)

    lista.append(contacorrente)

print('')
numconta = input("Digite numero da conta: ")

conta_existe = False
for conta in lista:
    if conta.numeroConta == numconta:
        conta_existe = True

if conta_existe:
    for conta in lista:
        if conta.numeroConta == numconta:
            print(conta.exibirDados())
            operação = int(input("1 - para SACAR e 2 - para DEPOSITAR: "))

            if operação == 1:
                valorSaque = float(input("Quanto deseja sacar: ")) 
                if conta.sacar(valorSaque) == True:
                    print(f"Saque realizado com sucesso. Saldo atual {conta.saldo}")
                else:
                    print(f"Saque não realizado. Saldo atual {conta.saldo}")
            if operação == 2:
                valorDeposito = float(input("Quanto deseja depositar: "))
                if conta.depositar(valorDeposito) == True:
                    print(f"Depósito realizado com sucesso. Saldo atual {conta.saldo}")
                else:
                    print(f"Depósito não realizado. Saldo atual {conta.saldo}")
else:
    print("conta n existe")

print("")
saldodetodos = 0
if len(lista) > 0:
    for conta in lista:
        saldodetodos += conta.saldo
    print(f"Saldo de todas as contas: {saldodetodos}")

    maior = -1
    for conta in lista:
        if conta.saldo > maior:
            maior = conta.saldo
    print(f"Maior saldo: {maior}")

    menor = 9999999
    for conta in lista:
        if conta.saldo < menor:
            menor = conta.saldo
    print(f"Menor saldo: {menor}")
