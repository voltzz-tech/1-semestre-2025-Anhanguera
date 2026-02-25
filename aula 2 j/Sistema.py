from Aluno import Aluno
from Tarefa import Tarefa

alunos = []
contadorAluno = 1

def cadastrarAluno():
    nome = input("Digite o nome do aluno: ")
    aluno = Aluno(contadorAluno, nome)
    alunos.append(aluno)
    contadorAluno += 1
    print("Aluno cadastrado com sucesso!")

def cadastrarTarefa():
    idAluno = int(input("Digite o ID aluno: "))
    
    for aluno in alunos:
        if aluno.id == idAluno:
            descricao = input("Descrição da tarefa: ")
            tarefa = Tarefa(descricao)
            aluno.adicionarTarefa(tarefa)
            print("Tarefa Cadastrada")
            return
        
        print("Aluno não encotrado.")

def listarTarefas():
    idAluno = int(input("Digite o ID do aluno: "))

    for aluno in alunos:
        if aluno.id == idAluno:
            aluno.listarTarefas()
            return
    print("Aluno não encontrado.")
    