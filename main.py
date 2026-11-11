## --- MAIN ---
"""Programa Principal - Menu Interativo Simplificado."""

from clinica_classe_gerenciadora import Clinica       #Classe Gerenciadora
from animal_classe_base import Animal         #Classe Base
from cachorro_classe_filha01 import Cachorro     #Classe Filha
from gato_classe_filha02 import Gato             #Classe Filha

def main():
    clinica = Clinica("Pet Feliz")

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
                    clinica.adicionar_animal(Cachorro(nome, sexo, idade, peso, dono, raca))
                elif tipo == "2":
                    cor = input("Cor do pelo: ").strip()
                    clinica.adicionar_animal(Gato(nome, sexo, idade, peso, dono, cor))
                print("Cadastrado com sucesso!")
            except ValueError as erro:
                print(f"Erro: {erro}")

        elif opcao == "2":
            print("\n--- Lista de Animais ---")
            animais = clinica.listar_animais()
            if not animais:
                print("Nenhum animal cadastrado.")
            for a in animais:
                print(a)

        elif opcao == "3":
            nome = input("Nome para buscar: ").strip()
            animal = clinica.buscar_por_nome(nome)
            print(animal if animal else "Não encontrado.")

        elif opcao == "4":
            print("\n--- Teste de Polimorfismo ---")
            for a in clinica.listar_animais():
                print(f"{a.nome}: {a.emitir_som()}")

        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()