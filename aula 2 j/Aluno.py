class Aluno:
    def __init__(self, id, nome):
        if not nome:
            raise ValueError("Nome não pode estra vazio")
        self.id = id
        self.nome = nome
        self.tarefas = []

    def adicionarTarefa(self, tarefa):
        self.tarefas.append(tarefa)

    def listarTarefas(self):
        for tarefa in self.tarefas:
            status = "ok" if tarefa.concluida else "x"
            print(f"{tarefa.id} - {tarefa.descricao} [{status}]")