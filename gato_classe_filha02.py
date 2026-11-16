## GATO

from animal_classe_base import Animal

# Classe Filha
class Gato(Animal):
    def __init__(self, nome, sexo, idade, peso, nome_dono, cor):
        super().__init__(nome, sexo, idade, peso, nome_dono)
        self.cor = cor  # Atributo próprio
        super().__init__(nome, sexo, "Gato", idade, peso, nome_dono)
        self.cor = cor

    # Atributo privado
    __cor = ""

    # Getter e Setter
    @property
    def cor(self):
        return self.__cor

    @cor.setter
    def cor(self, valor):
        if valor.strip() == "":
            raise ValueError("A cor não pode ser vazia.")
        self.__cor = valor

    # Método str
    def __str__(self):
        return (
            f"Nome: {self.nome} | "
            f"Cor: {self.cor} | "
            f"Tutor: {self.nome_dono}"
        )

    # Polimorfismo
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




gato01 = Gato(
    "Bob",
    "Macho",
    8,
    6,
    "Yara Borges",
    "Laranja"
)