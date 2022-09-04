class Pessoa:
    
    def __init__(self, nome):
        self.__nome = nome
        self.__idade = None
        self.__peso = None

    def validar_valor(self, valor):
        if valor < 0:
            return 0
        return valor

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
        self.__idade = self.validar_valor(idade)

    @property
    def peso(self):
        return self.__peso

    @peso.setter
    def peso(self, peso):
        self.__peso = self.validar_valor(peso)

    
pessoas = []
while True:
    nome = input("Nome: ")
    if nome == "Fim":
        break

    pessoa = Pessoa(nome)
    
    idade = int(input("Idade: "))
    peso = float(input("Peso: "))

    pessoa.idade = idade
    pessoa.peso = peso
    pessoas.append(pessoa)

media_peso = 0
mais_leve = 9999999999
mais_velho = -1

if len(pessoas) > 0:
    for pessoa in pessoas:
        media_peso += pessoa.peso
        if (pessoa.idade > mais_velho):
            mais_velho = pessoa.idade
        if (pessoa.peso < mais_leve):
            mais_leve = pessoa.peso
print(f"Média peso: {media_peso / len(pessoas)}")

for pessoa in pessoas:
    if pessoa.peso == mais_leve:
        print(f"Pessoa mais leve: {pessoa.nome}, {pessoa.peso}") 
    if pessoa.idade == mais_velho:
        print(f"Pessoa mais velha: {pessoa.nome}, {pessoa.idade}")
        
for pessoa in pessoas:
    print(f"Nome: {pessoa.nome} - Idade: {pessoa.idade} - Peso: {pessoa.peso}")

