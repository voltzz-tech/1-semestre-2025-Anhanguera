import tkinter as tk
from Sistema import Sistema
from tkinter import messagebox

class Interface:
    def __init__(self):
        self.sistema = Sistema()

        self.janela = tk.Tk()
        self.janela.title("Sistema 2° Semestre")
        self.janela.geometry("450x400")

        tk.Label(self.janela, text="Nome do Aluno").pack()
        self.nomeEntry = tk.Entry(self.janela, width=40)
        self.nomeEntry.pack()

        tk.Button(self.janela, text="Cadastrar Aluno", command=self.cadastrarAluno).pack()
        tk.Button(self.janela, text="Listar Alunos", command=self.listarAlunos).pack()

        self.lista = tk.Listbox(self.janela)
        self.lista.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)


        self.janela.mainloop()

    def cadastrarAluno(self):
        nome = self.nomeEntry.get()

        if nome.strip():
            try:
                self.sistema.cadastrarAluno(nome)
                messagebox.showinfo("Sucesso","Aluno cadastrado com sucesso")
                self.listarAlunos()
            except ValueError as e:
                messagebox.showerror("Erro",str(e))

        else:
            messagebox.showerror("Erro", "Nome não pode ser vazio")

    def listarAlunos(self):
        self.lista.delete(0, tk.END)
        alunos = self.sistema.listarAlunos()

        if not alunos:
            self.lista.insert(tk.END, "Nenhum aluno encontrado")
        for aluno in alunos:
            self.lista.insert(tk.END, str(aluno))

if __name__=="__main__":
    Interface()
