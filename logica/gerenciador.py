from logica.modelos import Especialidade, Senha
import heapq

class GerenciadorFilas:
    def __init__(self):
        self.especialidades_cadastradas = []
        self.ultima_senha_chamada = None
        self.ultima_especialidade_chamada = ""

    def cadastrar_especialidade(self, esp_codigo: str, esp_nome: str):
        if len(self.especialidades_cadastradas) >= 3:
            return False, "ERRO: Quantidade de especialidades excedida."

        for esp in self.especialidades_cadastradas:
            if esp.codigo == esp_codigo or esp.nome == esp_nome:
                return False, f"ERRO: Especialidade {esp_nome} já cadastrada."

        especialidade_nova = Especialidade(esp_codigo, esp_nome)
        self.especialidades_cadastradas.append(especialidade_nova)
        
        return True, f"SUCESSO: especialidade {esp_nome} cadastrada."

    def emitir_senha(self, codigo_especialidade: str, tipo: str, categoria_prioridade: int = 99):
        esp_alvo = None

        for esp in self.especialidades_cadastradas:
            if esp.codigo == codigo_especialidade:
                esp_alvo = esp
                break
                
        if not esp_alvo:
            return False, "ERRO: Especialidade não encontrada.", None

        esp_alvo.contador += 1
        identificador = f"{esp_alvo.codigo}-{tipo}{esp_alvo.contador:03d}"

        nova_senha = Senha(identificador, tipo, categoria_prioridade)

        if tipo == "N":
            esp_alvo.fila_normal.append(nova_senha)
        elif tipo == "P":
            heapq.heappush(esp_alvo.fila_prioritaria, nova_senha)
        else:
            return False, "ERRO: Tipo de atendimento inválido.", None

        return True, f"Senha {identificador} gerada com sucesso!", identificador

    def chamar_proximo(self, codigo_especialidade: str):
        esp_alvo = None

        for esp in self.especialidades_cadastradas:
            if esp.codigo == codigo_especialidade:
                esp_alvo = esp
                break
                
        if not esp_alvo:
            return False, "ERRO: Especialidade não encontrada.", None

        if esp_alvo.fila_prioritaria:
            senha_chamada = heapq.heappop(esp_alvo.fila_prioritaria)
            return True, f"Próximo paciente: {senha_chamada.identificador}", senha_chamada

        elif esp_alvo.fila_normal:
            senha_chamada = esp_alvo.fila_normal.popleft()
            return True, f"Próximo paciente: {senha_chamada.identificador}", senha_chamada

        else:
            return False, "A fila desta especialidade está vazia.", None

    def calcular_tempo_espera(self, codigo_especialidade: str, identificador_senha: str):
        esp_alvo = None
        
        for esp in self.especialidades_cadastradas:
            if esp.codigo == codigo_especialidade:
                esp_alvo = esp
                break
                
        if not esp_alvo:
            return False, "ERRO: Especialidade não encontrada.", 0

        pacientes_a_frente = 0
        encontrado = False

        fila_prioridade_ordenada = sorted(esp_alvo.fila_prioritaria)
        for i, senha in enumerate(fila_prioridade_ordenada):
            if senha.identificador == identificador_senha:
                pacientes_a_frente = i
                encontrado = True
                break

        if not encontrado:
            for i, senha in enumerate(esp_alvo.fila_normal):
                if senha.identificador == identificador_senha:
                    pacientes_a_frente = len(esp_alvo.fila_prioritaria) + i
                    encontrado = True
                    break

        if not encontrado:
            return False, "ERRO: Senha não encontrada ou já atendida.", 0

        tempo_estimado = pacientes_a_frente * 30
        return True, f"Tempo estimado de espera: {tempo_estimado} minutos.", tempo_estimado