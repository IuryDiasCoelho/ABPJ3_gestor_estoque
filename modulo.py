print("Bem vindo ao seu gestor de estoque")

def menu():
    print("\n--- MENU DE OPÇÕES ---")
    print("1- Cadastrar produto")
    print("2- Atualizar estoque")
    print("3- Registrar venda ")
    print("4- Estoque disponivel")
    print("5- Valor em caixa")
    print("6- Sair\n")

def cadastrar():
    protudo = input('digite o nome do produto: ')
    quantidade = int(input('digite a quantidade: '))
    valor = (input('digite o valor: '))
    valor_limpo = float(valor.replace(',', '.'))
    estoque[protudo] = quantidade
    financeiro[protudo] = valor_limpo

def venda():
    venda_produto = input('digite o nome do produto: ')

    if venda in estoque:
        try:
            print(estoque[venda_produto], "unidades")
            quantidade = int(input('digite a quantidade a ser vendida: '))

            if quantidade <= 0:
                print("A quantidade deve ser maior que zero.")
            elif quantidade > estoque[venda_produto]:
                print("Quantidade maior do que o estoque disponível.")
            else:
                estoque[venda_produto] -= quantidade
                print("vendendo ", quantidade, " unidades de ", venda_produto)
                print("registrando venda...")
                print("Estoque Atualizado\n", list(estoque.items()))
                return quantidade , venda_produto
        except ValueError:
            print("Digite uma quantidade válida (número inteiro).")
    else:
        print("Produto não encontrado no estoque.")


def valor_em_caixa(venda_produto, quantidade):
    soma=financeiro[venda_produto]*quantidade
    print(soma)
    print("valor em caixa...")

estoque={}
financeiro={}
while True:
    menu()
    usuario=input('digite a ação que quer realizar: ').lower()
    match usuario:
        case "cadastrar produto" | "1":
            cadastrar()
            print("cadastrando produto...")

        case "atualizar estoque" | "2":
            print(list(estoque.items()))
            print(list(financeiro.items()))
            cadastrar()
            print(list(estoque.items()))
            print(list(financeiro.items()))
            print("atualizando estoque...")

        case "registrar venda" | "3":
            venda()

        case "estoque disponivel" | "4":
            print("Buscando estoque disponivel...")
            print(estoque)
            print(financeiro)

        case "valor em caixa" | "5":


            print("valor em caixa...")

        case "sair" | "6":
            print("saindo...")
            break
        case _:
            print("\nDigite novamente o comando")

