import modulo



print("Bem vindo ao seu gestor de estoque")

while True:
    modulo.menu()
    usuario=input('digite a ação que quer realizar: ').lower()
    match usuario:
        case "cadastrar produto" | "1":
            modulo.cadastrar()
            print("cadastrando produto...")

        case "atualizar estoque" | "2":
            modulo.estoque_disponivel()
            modulo.cadastrar()
            modulo.estoque_disponivel()
            print("atualizando estoque...")

        case "registrar venda" | "3":

            modulo.venda()

        case "estoque disponivel" | "4":
            modulo.estoque_disponivel()

        case "valor em caixa" | "5":
            print(f"valor em caixa: {modulo.caixa:.2f} R$")

        case "sair" | "6":
            print("saindo...")
            break

        case _:
            print("\nDigite novamente o comando")

