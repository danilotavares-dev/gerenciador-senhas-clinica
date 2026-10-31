import tkinter as tk
from tkinter import messagebox

class TelaCadastroEspecialidades(tk.Frame):
    def __init__(self, parent, controller, gerenciador):
        super().__init__(parent)
        self.gerenciador = gerenciador

        tk.Label(self, text="Cadastro de Especialidades", font=("Arial", 16)).pack(pady=10)

        tk.Label(self, text="Código (Ex: C1):").pack()
        self.entry_codigo = tk.Entry(self)
        self.entry_codigo.pack(pady=5)

        tk.Label(self, text="Nome da Especialidade:").pack()
        self.entry_nome = tk.Entry(self)
        self.entry_nome.pack(pady=5)

        tk.Button(self, text="Salvar Cadastro", command=self.executar_cadastro).pack(pady=15)
        tk.Button(self, text="Voltar ao Menu", command=lambda: controller.mostrar_tela("TelaMenuPrincipal")).pack()

    def executar_cadastro(self):
        codigo = self.entry_codigo.get().strip()
        nome = self.entry_nome.get().strip()

        if not codigo or not nome:
            messagebox.showwarning("Aviso", "Preencha todos os campos!")
            return

        sucesso, mensagem = self.gerenciador.cadastrar_especialidade(codigo, nome)

        if sucesso:
            messagebox.showinfo("Sucesso", mensagem)
            self.entry_codigo.delete(0, tk.END)
            self.entry_nome.delete(0, tk.END)
        else:
            messagebox.showerror("Erro", mensagem)