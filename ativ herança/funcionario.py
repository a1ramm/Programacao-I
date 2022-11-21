class Funcionario:
    
    def __init__(self, nome, cpf, salario):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario

    def __str__(self):
        return f"Funcionário:\nNome: {self._nome}\nCPF: {self._cpf}\nSalário: R${self._salario}\n---"

    def getBonificacao(self):
        return self._salario * 1.10

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        self.nome = nome
    
    @property
    def cpf(self):
        return self._cpf
    
    @nome.setter
    def cpf(self, cpf):
        self.cpf = cpf

    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, salario):
        self._salario = salario

    
