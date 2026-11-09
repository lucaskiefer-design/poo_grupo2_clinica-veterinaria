## GATO

from animal import Animal

class Gato:
    def __init__(self, nome, sexo, idade, peso, nome_dono, cor):
        super().__init__(nome, sexo, idade, peso, nome_dono)
        self.cor = cor

gato01 = Gato("Bob", "Macho", 8, 6, "Yara Borges", "Laranja")