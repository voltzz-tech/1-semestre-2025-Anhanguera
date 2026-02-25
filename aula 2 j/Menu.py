from Aluno import Aluno
from Tarefa import Tarefa
from Sistema import Sistema

sistema = Sistema()

while True:
    print("1 - Cadastrar Aluno")
    print("2 - Cadastrar Tarefas")
    print("3 - Listar Tarefas")
    print("4 - Concluir Tarefas")
    print("0 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        sistema.cadastrarAluno()
    elif opcao == "2":
        sistema.cadastrarTarefa()
    elif opcao == "3":
        sistema.listarTarefas()
    elif opcao == "4":
        sistema.concluirTarefa()
    elif opcao == "0":
        break
    else:
        print("Opção Invalida.")