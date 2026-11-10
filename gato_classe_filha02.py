## GATO

from animal_classe_base import Animal

#Classe Filha
class Gato(Animal):
    def __init__(self, nome, sexo, idade, peso, nome_dono, cor):
        super().__init__(nome, sexo, idade, peso, nome_dono)
        self.cor = cor  # Atributo próprio
        self.cor = cor

    def __str__(self):
        return f"{self.nome} (tutor: {self.nome_dono})"

    def emitir_som(self):
        return "Miau Miau!"

    def arranhar(self):
        return f"{self.nome} está a afiar as garras!"

    # Método sobrescrito
    def emitir_som(self):
        return "Miau Miau!"

    def __str__(self):
        return f"[Gato] {super().__str__()} | Cor: {self.cor}"
gato01 = Gato("Bob", "Macho", 8, 6, "Yara Borges", "Laranja")




