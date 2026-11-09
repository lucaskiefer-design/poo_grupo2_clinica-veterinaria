## CACHORRO

from animal import Animal

class Cachorro:
    def __init__(self, nome, sexo, idade, peso, nome_dono, raca):
        super().__init__(nome, sexo, idade, peso, nome_dono)
        self.raca = raca

cachorro01 = Cachorro("", "Fêmea", 12, 9, "Vinícius Über", "Golden Retriever")