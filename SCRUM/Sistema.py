from Aluno import Aluno

class Sistema:
    def __init__(self):
        self.alunos = []
        self.contadorAluno = 1

    def cadastrarAluno(self, nome):
        aluno = Aluno(self.contadorAluno, nome)
        self.alunos.append(aluno)
        self.contadorAluno += 1

    def listarAluno(self):
        return self.alunos
    
    def buscarAluno(self, idAluno):
        for aluno in self.alunos:
            if aluno.id == idAluno:
                return aluno
        return None