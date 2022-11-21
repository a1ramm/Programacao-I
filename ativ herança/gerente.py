from funcionario import Funcionario

class Gerente(Funcionario):

    def __init__(self, nome, cpf, salario, senha, qtde):
        super().__init__(nome, cpf, salario)
        self.__senha = senha
        self.__qtde = qtde

    def __str__(self):
        return f"Gerente:\nNome: {self._nome}\nCPF: {self._cpf}\nSalário: R${self._salario}\nSenha: {self.__senha}\nQtde Gerenciáveis: {self.__qtde}\n---"
    
    def getBonificacao(self):
        return self._salario * 1.15

    @property
    def senha(self):
        return self.senha
    
    @senha.setter
    def senha(self, senha):
        self.__senha = senha

    @property
    def qtde(self):
        return self.__qtde
    
    @qtde.setter
    def qtde(self, qtde):
        self.__qtde = qtde
