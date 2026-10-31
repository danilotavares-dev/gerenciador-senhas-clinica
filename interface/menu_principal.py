import tkinter as tk

class TelaMenuPrincipal(tk.Frame):
    def __init__(self, parent, controller, gerenciador):
        super().__init__(parent)
        
        titulo = tk.Label(self, text="Menu Principal", font=("Arial", 18, "bold"))
        titulo.pack(pady=20)

        # Botão 1: Cadastro
        tk.Button(
            self, 
            text="1. Cadastro de Especialidades", 
            command=lambda: controller.mostrar_tela("TelaCadastroEspecialidades"),
            width=30
        ).pack(pady=5)

        # Botão 2: Emissão de Senhas
        tk.Button(
            self, 
            text="2. Emissão de Senhas", 
            command=lambda: controller.mostrar_tela("TelaEmissaoSenhas"),
            width=30
        ).pack(pady=5)

        # Botão 3: Gerenciamento das Filas (Chamar próximo)
        tk.Button(
            self, 
            text="3. Gerenciamento das Filas", 
            command=lambda: controller.mostrar_tela("TelaGerenciamentoFilas"),
            width=30
        ).pack(pady=5)

        # Botão 4: Painel de Atendimento (Ecrã de espera)
        tk.Button(
            self, 
            text="4. Painel de Atendimento", 
            command=lambda: controller.mostrar_tela("TelaPainelAtendimento"),
            width=30
        ).pack(pady=5)

        # Botão 5: Tempo Estimado
        tk.Button(
            self, 
            text="5. Tempo Estimado de Espera", 
            command=lambda: controller.mostrar_tela("TelaTempoEspera"),
            width=30
        ).pack(pady=5)