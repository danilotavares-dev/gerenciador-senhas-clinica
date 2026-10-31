import tkinter as tk

class TelaPainelAtendimento(tk.Frame):
    def __init__(self, parent, controller, gerenciador):
        super().__init__(parent)
        self.gerenciador = gerenciador

        tk.Label(self, text="Painel de Atendimento", font=("Arial", 20, "bold")).pack(pady=20)

        self.lbl_senha = tk.Label(self, text="Nenhuma senha chamada", font=("Arial", 26, "bold"), fg="red")
        self.lbl_senha.pack(pady=10)

        self.lbl_detalhes = tk.Label(self, text="", font=("Arial", 14))
        self.lbl_detalhes.pack(pady=10)

        tk.Button(self, text="Atualizar Painel", command=self.atualizar_painel).pack(pady=10)
        tk.Button(self, text="Voltar ao Menu", command=lambda: controller.mostrar_tela("TelaMenuPrincipal")).pack()

    def atualizar_painel(self):
        senha = self.gerenciador.ultima_senha_chamada
        esp_codigo = self.gerenciador.ultima_especialidade_chamada

        if senha and esp_codigo:
            self.lbl_senha.config(text=f"SENHA: {senha.identificador}")
            
            # Encontra a especialidade para contar os pacientes restantes
            esp_alvo = None
            for e in self.gerenciador.especialidades_cadastradas:
                if e.codigo == esp_codigo:
                    esp_alvo = e
                    break
            
            if esp_alvo:
                qtd = len(esp_alvo.fila_normal) + len(esp_alvo.fila_prioritaria)
                tipo_str = "Prioritário" if senha.tipo == "P" else "Normal"
                self.lbl_detalhes.config(text=f"Especialidade: {esp_alvo.nome}\nAtendimento: {tipo_str}\nAguardando na fila: {qtd}")
        else:
            self.lbl_senha.config(text="Aguardando chamadas...")
            self.lbl_detalhes.config(text="")