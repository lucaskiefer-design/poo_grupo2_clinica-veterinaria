9## --- MAIN ---
"""Programa Principal - Menu Interativo Simplificado."""

from clinica_classe_gerenciadora import Clinica
from cachorro_classe_filha01 import Cachorro
from gato_classe_filha02 import Gato


def main():
    clinica = Clinica(
        "Pet Feliz",
        "Rua 25 de Julho, Jaraguá do Sul"
    )

    while True:
        print("\n--- CLÍNICA VETERINÁRIA ---")
        print("1. Cadastrar | 2. Listar | 3. Buscar | 4. Som | 5. Sair")
        opcao = input("Opção: ").strip()

        if opcao == "1":
            try:
                tipo = input("Tipo (1-Cachorro / 2-Gato): ").strip()
                nome = input("Nome: ").strip()
                sexo = input("Sexo: ").strip()
                idade = int(input("Idade: "))
                peso = float(input("Peso: "))
                dono = input("Dono: ").strip()

                if tipo == "1":
                    raca = input("Raça: ").strip()
                    clinica.adicionar_animal(
                        Cachorro(nome, sexo, idade, peso, dono, raca)
                    )

                elif tipo == "2":
                    cor = input("Cor do pelo: ").strip()
                    clinica.adicionar_animal(
                        Gato(nome, sexo, idade, peso, dono, cor)
                    )

                else:
                    print("Tipo inválido.")
                    continue

                print("Cadastrado com sucesso!")

            except ValueError as erro:
                print(f"Erro: {erro}")

        elif opcao == "2":
            print("\n--- Lista de Animais ---")
            animais = clinica.listar_animais()

            if not animais:
                print("Nenhum animal cadastrado.")
            else:
                for animal in animais:
                    print(animal)

        elif opcao == "3":
            nome = input("Nome para buscar: ").strip()
            animal = clinica.buscar_por_nome(nome)

            if animal:
                print(animal)
            else:
                print("Não encontrado.")

        elif opcao == "4":
            print("\n--- Teste de Polimorfismo ---")

            for animal in clinica.listar_animais():
                print(f"{animal.nome}: {animal.emitir_som()}")

        elif opcao == "5":
            print("Saindo...")
            break

        else:
            print("Opção inválida.")