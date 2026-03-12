from Sistema import Sistema

sistema = Sistema()

while True:
    print("1. Cadastrar Aluno")
    print("2. Listar Alunos")
    print("3. Cadastrar tarefa")
    print("0. Sair")

    opcao = input("Escolha uma opção")

    if opcao == "1":
        nome = input("digite o nome do aluno")
        sistema.cadastrarAluno(nome)

    elif opcao == "2":
        sistema.listarAlunos()
    elif opcao =="3":
        idAluno = int(input("ID do Aluno: "))
        descricao = input("Descrição da Tarefa: ")
        sistema.cadastrarTarefa(idAluno, descricao)
        
    elif opcao == "0":
        break
    else:
        print("Opção invalida")
