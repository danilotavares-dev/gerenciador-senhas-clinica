from collections import deque

class Especialidade: 
    def __init__(self, codigo: str, nome: str):
        self.codigo = codigo
        self.nome = nome
        self.fila_normal = deque()
        self.fila_prioritaria = []
        self.contador = 0

class Senha:
    def __init__(self, identificador: str, tipo: str, prioridade: int = 99):
        self.identificador = identificador
        self.tipo = tipo
        self.prioridade = prioridade

    def __lt__(self, other):
        return self.prioridade < other.prioridade