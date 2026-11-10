## CLÍNICA

class Clinica:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco

    def __str__(self):
        return f"{self.nome} ({self.endereco})"

clinica01 = Clinica("Clínica do Jorge", "Rua 25 de julho, Vila Nova, Jaraguá do Sul")

