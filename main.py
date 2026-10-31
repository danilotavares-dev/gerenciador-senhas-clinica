import tkinter as tk
from logica.gerenciador import GerenciadorFilas
from interface.menu_principal import TelaMenuPrincipal
from interface.cadastro_especialidades import TelaCadastroEspecialidades
from interface.emissao_senhas import TelaEmissaoSenhas
from interface.painel_atendimento import TelaPainelAtendimento
from interface.tempo_espera import TelaTempoEspera
from interface.gerenciador_filas import TelaGerenciamentoFilas

class AppClinica(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Gerenciamento de Senhas")
        self.geometry("600x400")

        self.gerenciador = GerenciadorFilas()

        self.telas = {}

        container = tk.Frame(self)
        container.pack(fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        for TelaClass in (
            TelaMenuPrincipal, 
            TelaCadastroEspecialidades, 
            TelaEmissaoSenhas, 
            TelaGerenciamentoFilas, 
            TelaPainelAtendimento, 
            TelaTempoEspera
        ):
            nome_tela = TelaClass.__name__
            frame = TelaClass(parent=container, controller=self, gerenciador=self.gerenciador)
            self.telas[nome_tela] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.mostrar_tela("TelaMenuPrincipal")

    def mostrar_tela(self, nome_tela):
        frame = self.telas[nome_tela]
        frame.tkraise()

if __name__ == "__main__":
    app = AppClinica()
    app.mainloop()