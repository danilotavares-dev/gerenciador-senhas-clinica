import tkinter as tk
from tkinter import messagebox

class TelaTempoEspera(tk.Frame):
    def __init__(self, parent, controller, gerenciador):
        super().__init__(parent)
        self.gerenciador = gerenciador

        tk.Label(self, text="Tempo Estimado de Espera", font=("Arial", 16, "bold")).pack(pady=10)

        tk.Label(self, text="Código da Especialidade (Ex: C1):").pack()
        self.entry_codigo = tk.Entry(self)
        self.entry_codigo.pack(pady=5)

        tk.Label(self, text="Sua Senha (Ex: C1-N001):").pack()
        self.entry_senha = tk.Entry(self)
        self.entry_senha.pack(pady=5)

        tk.Button(self, text="Consultar Tempo", command=self.consultar).pack(pady=10)

        self.lbl_resultado = tk.Label(self, text="", font=("Arial", 14), fg="blue")
        self.lbl_resultado.pack(pady=10)

        tk.Button(self, text="Voltar ao Menu", command=lambda: controller.mostrar_tela("TelaMenuPrincipal")).pack()

    def consultar(self):
        codigo = self.entry_codigo.get().strip()
        senha = self.entry_senha.get().strip()

        if not codigo or not senha:
            messagebox.showwarning("Aviso", "Preencha todos os campos.")
            return

        sucesso, mensagem, tempo = self.gerenciador.calcular_tempo_espera(codigo, senha)
        
        if sucesso:
            self.lbl_resultado.config(text=mensagem)
        else:
            self.lbl_resultado.config(text="")
            messagebox.showerror("Erro", mensagem)