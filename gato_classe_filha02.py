## GATO

# Classe filha -- Gato

# Importa a classe base Animal
from animal_classe_base import Animal


class Gato(Animal):

    # Método construtor
    def __init__(self, nome, sexo, idade, peso, nome_dono, cor):
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
            f"Sexo: {self.sexo} | "
            f"Cor: {self.cor} | "
            f"Idade: {self.idade} anos | "
            f"Peso: {self.peso} kg | "
            f"Tutor: {self.nome_dono}"
        )

    # Polimorfismo
    def emitir_som(self):
        return "Miau Miau!"

    # Método próprio
    def arranhar(self):
        return f"{self.nome} está a afiar as garras!"


# Instância
gato01 = Gato(
    "Bob",
    "Macho",
    8,
    6,
    "Yara Borges",
    "Laranja"
)

# Testes dos métodos da classe
print(gato01)
print(gato01.emitir_som())
print(gato01.arranhar())