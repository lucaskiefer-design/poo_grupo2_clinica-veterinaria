## CACHORRO

# Classe filha -- Cachorro

# Importa a classe base Animal
from animal_classe_base import Animal


class Cachorro(Animal):

    # Método construtor
    def __init__(self, nome, sexo, idade, peso, nome_dono, raca):
        super().__init__(nome, sexo, "Cachorro", idade, peso, nome_dono)
        self.raca = raca

    # Atributo privado
    __raca = ""

    # Getter e Setter com validação
    @property
    def raca(self):
        return self.__raca

    @raca.setter
    def raca(self, valor):
        if valor.strip() == "":
            raise ValueError("A raça não pode ser vazia.")
        self.__raca = valor

    # Método str
    def __str__(self):
        return (
            f"Nome: {self.nome} | "
            f"Sexo: {self.sexo} | "
            f"Raça: {self.raca} | "
            f"Idade: {self.idade} anos | "
            f"Peso: {self.peso} kg | "
            f"Tutor: {self.nome_dono}"
        )

    # Polimorfismo
    def emitir_som(self):
        return "Au Au!!"