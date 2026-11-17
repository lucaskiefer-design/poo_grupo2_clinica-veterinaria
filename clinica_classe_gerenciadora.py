class Clinica:
    def __init__(self, nome, endereco):
        self.__animais = []
        self.nome = nome
        self.endereco = endereco

    # Getter e Setter de nome
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valor):
        if valor.strip() == "":
            raise ValueError("O nome da clínica não pode ser vazio.")
        self.__nome = valor

    # Getter e Setter de endereço
    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, valor):
        if valor.strip() == "":
            raise ValueError("O endereço não pode ser vazio.")
        self.__endereco = valor

    def __str__(self):
        return f"{self.nome} ({self.endereco})"

    def adicionar_animal(self, animal):
        self.__animais.append(animal)

    def listar_animais(self):
        return self.__animais

    def buscar_por_nome(self, nome):
        for animal in self.__animais:
            if animal.nome.lower() == nome.lower():
                return animal
        return None
