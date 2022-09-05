from pessoa import Pessoa
from endereço import Endereco

listaPessoas = []
while True:
    nome = input("Digite seu nome: ")
    if nome == "fim":
        break
    idade = int(input("Digite seu idade: "))
    cidade = input("Digite o nome da sua cidade: ")
    bairro = input("Digite o nome do seu bairro: ")
    rua = input("Digite o nome da sua rua: ")
    numero = int(input("Digite o num da sua casa: "))
    
    endereco = Endereco(cidade, bairro, rua, numero)
    pessoa = Pessoa(nome, idade, endereco)
    
    listaPessoas.append(pessoa)

mediaIdades = 0
if len(listaPessoas) > 0:
    for pessoa in listaPessoas:
        mediaIdades += pessoa.idade
print("")
print(f"Média das Idades: {mediaIdades / len(listaPessoas)}")

for pessoa in listaPessoas:
    print("=" * 20)
    print(pessoa.exibeDados())

print("")
c = 0
cidade = input("Digite o nome de uma cidade: ")
for pessoa in listaPessoas:
    if pessoa.endereco.cidade == cidade:
        c += 1
print(f"Tem {c} pessoas cadastradas nessa cidade")