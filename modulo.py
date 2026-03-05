estoque={}
financeiro={}
caixa=0

def menu():
    print("\n--- MENU DE OPÇÕES ---")
    print("1- Cadastrar produto")
    print("2- Atualizar estoque")
    print("3- Registrar venda ")
    print("4- Estoque disponivel")
    print("5- Valor em caixa")
    print("6- Sair\n")

def estoque_disponivel():
    print("\nBuscando estoque disponivel...")
    for produto, qtd in estoque.items():
        valor = financeiro[produto]
        print(f"{produto} - {qtd} unidades - R${valor}\n")

def cadastrar():
    produto = input('digite o nome do produto: ')
    quantidade = int(input('digite a quantidade: '))
    valor = (input('digite o valor: '))
    valor_limpo = float(valor.replace(',', '.'))
    estoque[produto] = quantidade
    financeiro[produto] = valor_limpo

def venda():
    global caixa
    estoque_disponivel()
    venda_produto = input('digite o nome do produto: ')
    if venda_produto in estoque:
        try:
            print(estoque[venda_produto], "unidades")
            quantidade = int(input('digite a quantidade a ser vendida: '))
            if quantidade <= 0:
                print("A quantidade deve ser maior que zero.")
            elif quantidade > estoque[venda_produto]:
                print("Quantidade maior do que o estoque disponível.")
            else:
                estoque[venda_produto] -= quantidade
                soma = financeiro[venda_produto] * quantidade
                caixa += soma
                print("vendendo ", quantidade, " unidades de ", venda_produto)
                print("registrando venda...")
                print("Estoque Atualizado")
                estoque_disponivel()
        except ValueError:
            print("Digite uma quantidade válida (número inteiro).")
    else:
        print("Produto não encontrado no estoque.")