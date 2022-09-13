from Cliente import Cliente

class ContaCorrente:

    def __init__(self, numeroConta, saldo, cliente):
        self.numeroConta = numeroConta
        self.saldo = saldo
        self.cliente = cliente
    
    def sacar(self, valor):
        if (self.saldo - valor) > 0:
            self.saldo -= valor
            return True
        else:
            return False
        
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            return True
        else:
            return False


    def exibirDados(self):
        return f"Nome: {self.cliente.nome}\nCPF: {self.cliente.cpf}\nNúmero da conta: {self.numeroConta}\nSaldo: {self.saldo}"
