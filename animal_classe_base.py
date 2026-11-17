## ANIMAL

# Classe Base -- Animal
class Animal:
    def __init__(self, nome, sexo, especie, idade, peso, nome_dono):
        self.nome = nome
        self.sexo = sexo
        self.especie = especie
        self.idade = idade
        self.peso = peso
        self.nome_dono = nome_dono

    # Getter e Setter de nome
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valor):
        if valor.strip() == "":
            raise ValueError("O nome não pode ser vazio.")
        self.__nome = valor

    # Getter e Setter de sexo
    @property
    def sexo(self):
        return self.__sexo

    @sexo.setter
    def sexo(self, valor):
        self.__sexo = valor

    # Getter e Setter de espécie
    @property
    def especie(self):
        return self.__especie

    @especie.setter
    def especie(self, valor):
        self.__especie = valor

    # Getter e Setter de idade
    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, valor):
        if valor < 0:
            raise ValueError("A idade não pode ser negativa.")
        self.__idade = valor

    # Getter e Setter de peso
    @property
    def peso(self):
        return self.__peso

    @peso.setter
    def peso(self, valor):
        if valor <= 0:
            raise ValueError("O peso deve ser maior que zero.")
        self.__peso = valor

    # Getter e Setter de nome do dono
    @property
    def nome_dono(self):
        return self.__nome_dono

    @nome_dono.setter
    def nome_dono(self, valor):
        self.__nome_dono = valor

    # Método str
    def __str__(self):
        return (
            f"Nome: {self.nome} | "
            f"Espécie: {self.especie} | "
            f"Sexo: {self.sexo} | "
            f"Idade: {self.idade} anos | "
            f"Peso: {self.peso} kg | "
            f"Dono: {self.nome_dono}"
        )

    def emitir_som(self):
        pass
