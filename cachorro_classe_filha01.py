## CACHORRO

from animal_classe_base import Animal

#Classe Filha
class Cachorro:
    def __init__(self, nome, sexo, idade, peso, nome_dono, raca):
        super().__init__(nome, sexo, idade, peso, nome_dono)
        self.raca = raca

#   Método def str(características das classes)
    def __str__(self):
        return f"{self.nome} (tutor: {self.nome_dono})"

    def emitir_som(self):
        return "Au Au!!"

cachorro01 = Cachorro("", "Fêmea", 12, 9, "Vinícius Über", "Golden Retriever")