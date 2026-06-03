from Produtos import cadastrar_produto, realizar_venda, relatorio_produto

lista = []

def menu_cadastrar():
    nome = input("Produto: ")
    preco = float(input("Preço Unitário: R$ "))
    quantidade = int(input("Quantidade inicial: "))
    produto = cadastrar_produto(nome, preco, quantidade)
    lista.append(produto)
    print(f"✔ Produto '{nome}' cadastrado com sucesso!")

def menu_vender():
    if not lista:
        print("⚠ Nenhum produto cadastrado.")
        return

    print("\n=== PRODUTOS DISPONÍVEIS ===")
    for i, p in enumerate(lista):
        print(f"[{i + 1}] {p['nome']} — Estoque: {p['quantidade_atual']}")

    try:
        idx = int(input("Escolha o número do produto: ")) - 1
        if idx < 0 or idx >= len(lista):
            print("⚠ Opção inválida.")
            return
    except ValueError:
        print("⚠ Digite um número válido.")
        return

    while True:
        try:
            qtd = int(input("Quantidade vendida: "))
        except ValueError:
            print("⚠ Digite um número válido.")
            continue

        if realizar_venda(lista[idx], qtd):
            print("✔ Venda realizada com sucesso!")
            break

def menu_relatorio():
    if not lista:
        print("⚠ Nenhum produto cadastrado.")
        return

    for produto in lista:
        relatorio_produto(produto)

def main():
    while True:
        print("\n=== MENU ===")
        print("[1] Cadastrar produto")
        print("[2] Realizar venda")
        print("[3] Relatório")
        print("[0] Sair")

        opcao = input("Opção: ")

        if opcao == "1":
            menu_cadastrar()
        elif opcao == "2":
            menu_vender()
        elif opcao == "3":
            menu_relatorio()
        elif opcao == "0":
            print("Até logo!")
            break
        else:
            print("⚠ Opção inválida.")

if __name__ == "__main__":
    main()
