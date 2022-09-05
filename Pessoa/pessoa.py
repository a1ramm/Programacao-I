from endereço import Endereco

class Pessoa:

    def __init__(self, nome, idade, endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
    
    def exibeDados(self):
        return f'Nome: {self.nome}\nIdade: {self.idade}\nEndereço - \n\tCidade: {self.endereco.cidade}, Bairro: {self.endereco.bairro}, Rua: {self.endereco.rua}, Numero: {self.endereco.numero}'
    
    