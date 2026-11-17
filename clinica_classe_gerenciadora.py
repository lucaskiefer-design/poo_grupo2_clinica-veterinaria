class Clinica:
    def __init__(self, nome, endereco):
        self.__nome = ""
        self.__endereco = ""

        self.nome = nome
        self.endereco = endereco

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valor):
        if valor.strip() == "":
            raise ValueError("O nome da clínica não pode ser vazio.")
        self.__nome = valor

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


clinica01 = Clinica(
    "Clínica do Jorge",
    "Rua 25 de Julho, Vila Nova, Jaraguá do Sul"
)

print(clinica01)