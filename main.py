from Produtos import cadastrar_produto, realizar_venda, relatorio_produto
lista = []
def main():
    while True:
        print("\n=== CADASTRO DE PRODUTO ===")
        nome = input("Produto: ")
        preco = float(input("Preço Unitário: "))
        quantidade = int(input("Quantidade: "))
        produto = cadastrar_produto(nome, preco, quantidade)
        lista.append(produto)

        continuar = input("Cadastrar outro produto? [s/n]: ")
        if continuar == 'n':
            break
    
    for produto in lista:
        print(f"\n=== VENDA - {produto['nome']} ===")
        while True:
            qtd = int(input("Quantidade vendida: "))
            if realizar_venda(produto, qtd):
                break
            
    for produto in lista:
        relatorio_produto(produto)
    
if __name__ == "__main__":
    main()