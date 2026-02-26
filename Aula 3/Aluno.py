from Tarefa import Tarefa

class Aluno:
    def __init__(self, id, nome):
        if not nome:
            raise ValueError("Nome não pode estar vazio.")
        self.id = id
        self.nome = nome
        self.tarefas = []

    def adicionarTarefas(self, tarefas):
        self.tarefas.append(tarefa)

    def listarTarefas(self):
        if not self.tarefas:
            print("Nenhuma tarefa cadastrada.")
            return
    
        for tarefa in self.tarefas:
            print(tarefa)
        

    def __str__(self):
        return f"{self.id} - {self.nome}"