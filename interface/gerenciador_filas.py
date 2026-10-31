import tkinter as tk
from tkinter import messagebox

class TelaGerenciamentoFilas(tk.Frame):
    def __init__(self, parent, controller, gerenciador):
        super().__init__(parent)
        self.gerenciador = gerenciador

        tk.Label(self, text="Gerenciamento de Filas", font=("Arial", 16, "bold")).pack(pady=10)

        tk.Label(self, text="Código da Especialidade (Ex: C1):").pack()
        self.entry_codigo = tk.Entry(self)
        self.entry_codigo.pack(pady=5)

        tk.Button(self, text="Chamar Próximo Paciente", command=self.chamar).pack(pady=10)

        self.lbl_chamado = tk.Label(self, text="", font=("Arial", 14, "bold"), fg="green")
        self.lbl_chamado.pack(pady=10)

        tk.Button(self, text="Voltar ao Menu", command=lambda: controller.mostrar_tela("TelaMenuPrincipal")).pack()

    def chamar(self):
        codigo = self.entry_codigo.get().strip()
        if not codigo:
            messagebox.showwarning("Aviso", "Informe a especialidade.")
            return

        sucesso, mensagem, senha_obj = self.gerenciador.chamar_proximo(codigo)
        
        if sucesso:
            self.lbl_chamado.config(text=mensagem)
            # Regista a chamada para o Painel de Atendimento (Tela 5)
            self.gerenciador.ultima_senha_chamada = senha_obj
            self.gerenciador.ultima_especialidade_chamada = codigo
        else:
            self.lbl_chamado.config(text="")
            messagebox.showinfo("Fila", mensagem)