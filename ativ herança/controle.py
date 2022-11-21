from funcionarioo import Funcionario
from gerente import Gerente

class ControleDeBonificacoes:
    
    def __init__(self):
        self.__totalBonificacao = 0
        self.__listaFuncionarios = list()
    
    def registra(self, funcionario):
        self.__listaFuncionarios.append(funcionario)
        
    def getTotalBonificacoes(self):
        for funcionario in self.__listaFuncionarios:
            self.__totalBonificacao += (funcionario.getBonificacao() - funcionario.salario)
        return f"Total Bonificações: R${self.__totalBonificacao:.2f}"

f1 = Funcionario("Maria", "111.222.333-44", 100)
f2 = Funcionario("Lucas", "123.123.123-12", 200)
g1 = Gerente("Heloisa", "321.321.321-32", 4000, "12345", 10)

listaFuncionarios = [f1, f2, g1]
c = ControleDeBonificacoes()
c.registra(f1)
c.registra(f2)
c.registra(g1)
for funcionario in listaFuncionarios:
    print(funcionario)
print(c.getTotalBonificacoes())