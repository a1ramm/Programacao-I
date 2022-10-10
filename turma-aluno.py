class Aluno:

    def __init__(self, matricula, nome):
        self.matricula = matricula
        self.nome = nome

class Turma:

    def __init__(self, codigo, descricao):
        self.codigo = codigo
        self.descricao = descricao
        self.alunos = []
    
    def addAluno(self, aluno):
        if aluno in self.alunos:
            return f"{aluno.matricula}/{aluno.nome} já está matriculado na turma {self.codigo}/{self.descricao}"
        else:
            self.alunos.append(aluno)
            return f"{aluno.matricula}/{aluno.nome} foi matriculado na turma {self.codigo}/{self.descricao}"

    def delAluno(self, aluno):
        if aluno not in self.alunos:
            return f"{aluno.matricula}/{aluno.nome} não está matriculado na turma {self.codigo}/{self.descricao}"
        else:
            self.alunos.remove(aluno)
            return f"{aluno.matricula}/{aluno.nome} removido da turma {self.codigo}/{self.descricao}"

#Turmas:
programacaoI = Turma("POO", "Programacao I")
historia = Turma("HIS", "História")
engenhariaSoft = Turma("ENG", "Engenharia de Software")

#Alunos:
joao = Aluno('001', 'João da Silva')
maria = Aluno('002', 'Maria dos Santos')
henrique = Aluno('003', 'Henrique Mattos')
pedro = Aluno('004', 'Pedro Gonçalves')
felipe = Aluno('004', 'Felipe Martins')

#Matriculas e cancelamentos
print(programacaoI.addAluno(joao))
print(programacaoI.addAluno(maria))
print(programacaoI.addAluno(henrique))
print(programacaoI.addAluno(henrique))
print(programacaoI.delAluno(joao))
print(programacaoI.delAluno(felipe))
print(historia.addAluno(joao))
print(historia.delAluno(henrique))
print(historia.addAluno(felipe))

