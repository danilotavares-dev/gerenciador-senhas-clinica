import tkinter as tk
from tkinter import messagebox

class TelaEmissaoSenhas(tk.Frame):
    def __init__(self, parent, controller, gerenciador):
        super().__init__(parent)
        self.gerenciador = gerenciador

        tk.Label(self, text="Emissão de Senhas", font=("Arial", 16, "bold")).pack(pady=10)

        tk.Label(self, text="Código da Especialidade (Ex: C1):").pack()
        self.entry_codigo = tk.Entry(self)
        self.entry_codigo.pack(pady=5)

        tk.Label(self, text="Tipo de Atendimento:").pack()
        self.var_tipo = tk.StringVar(value="N")
        tk.Radiobutton(self, text="Normal (N)", variable=self.var_tipo, value="N").pack()
        tk.Radiobutton(self, text="Prioritário (P)", variable=self.var_tipo, value="P").pack()

        tk.Label(self, text="Categoria de Prioridade (1 a 6) - Apenas se 'P':").pack()
        self.entry_prioridade = tk.Entry(self)
        self.entry_prioridade.pack(pady=5)

        tk.Button(self, text="Gerar Senha", command=self.gerar_senha).pack(pady=10)
        
        self.lbl_senha_gerada = tk.Label(self, text="", font=("Arial", 14, "bold"), fg="blue")
        self.lbl_senha_gerada.pack(pady=10)

        tk.Button(self, text="Voltar ao Menu", command=lambda: controller.mostrar_tela("TelaMenuPrincipal")).pack()

    def gerar_senha(self):
        codigo = self.entry_codigo.get().strip()
        tipo = self.var_tipo.get()
        prioridade_str = self.entry_prioridade.get().strip()

        if not codigo:
            messagebox.showwarning("Aviso", "Informe o código da especialidade.")
            return

        prioridade = 99
        if tipo == "P":
            if not prioridade_str.isdigit() or not (1 <= int(prioridade_str) <= 6):
                messagebox.showwarning("Aviso", "Para atendimento prioritário, informe uma categoria de 1 a 6.")
                return
            prioridade = int(prioridade_str)

        sucesso, mensagem, senha = self.gerenciador.emitir_senha(codigo, tipo, prioridade)

        if sucesso:
            self.lbl_senha_gerada.config(text=f"SENHA GERADA: {senha}")
            messagebox.showinfo("Sucesso", mensagem)
        else:
            messagebox.showerror("Erro", mensagem)