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

for conta in lista:
    if conta.numeroConta == numconta:
        print(conta.exibirDados())
        operação = int(input("1 - para SACAR e 2 - para DEPOSITAR: "))

        if operação == 1:
            sacar = float(input("Quanto deseja sacar: "))
            print(conta.sacar(sacar))
        if operação == 2:
            depositar = float(input("Quanto deseja depositar: "))
            print(conta.depositar(depositar))

if len(lista) > 0:
    print("Saldo de todas as contas")
    for conta in lista:
        print(conta.saldo)

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


