#Classe Gerenciadora -- Clínica

class Clinica:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco

    # Atributos privados
    __nome = ""
    __endereco = ""

    # Getter e Setter de nome
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valor):
        # Validação para impedir nome vazio
        if valor.strip() == "":
            raise ValueError("O nome da clínica não pode ser vazio.")
        self.__nome = valor

    # Getter e Setter de endereço
    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, valor):
        # Validação para impedir endereço vazio
        if valor.strip() == "":
            raise ValueError("O endereço não pode ser vazio.")
        self.__endereco = valor

    # Método str
    def __str__(self):
        return f"{self.nome} ({self.endereco})"


clinica01 = Clinica(
    "Clínica do Jorge",
    "Rua 25 de Julho, Vila Nova, Jaraguá do Sul"
<<<<<<< HEAD
)
=======
)
# Exibe os dados da clínica utilizando
# o método especial __str__()
print(clinica01)
>>>>>>> 91f6ebb (Implementação dos comentários)
