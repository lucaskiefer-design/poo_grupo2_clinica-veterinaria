## GATO

from animal_classe_base import Animal

class Gato:
    def __init__(self, nome, sexo, idade, peso, nome_dono, cor):
        super().__init__(nome, sexo, idade, peso, nome_dono)
        self.cor = cor

    def __str__(self):
        return f"{self.nome} (tutor: {self.nome_dono})"

    def emitir_som(self):
        return "Miau Miau!"

gato01 = Gato("Bob", "Macho", 8, 6, "Yara Borges", "Laranja")