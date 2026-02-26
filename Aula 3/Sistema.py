from Aluno import Aluno
from Tarefa import Tarefa

class Sistema:
    def __init__(self):
        self.alunos = []
        self.contadorAluno = 1

    def cadastrarAluno(self, nome):
        aluno = Aluno(self.contadorAluno, nome)
        self.alunos.append(aluno)
        self.contadorAluno += 1
        print("Aluno cadastrado com sucesso!")

    def listarAlunos(self):
        if not self.alunos:
            print("Nenhum aluno cadastrado")
            return
        
        for aluno in self.alunos:
            print(aluno)


    def castrarTarefa(self, idAluno, descricao):
        for aluno in self.alunos:
            if aluno.id == idAluno:
                tarefa = Tarefa(self.contadorAluno, descricao)
                aluno.adicionarTarefa(tarefa)
                self.contadorTarefa += 1
                print("Tarefa cadastrada!")
                return
    print("Aluno não encontrado!")
