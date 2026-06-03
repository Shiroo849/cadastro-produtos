


def cadastrar_produto(nome, preco, quantidade_inicial):
    produto = {
        "nome": nome,
        "preco": float(preco),
        "quantidade_inicial": int(quantidade_inicial),
        "quantidade_vendida": 0,
        "quantidade_atual": int(quantidade_inicial)
    }
    return produto

def realizar_venda(produto, quantidade_vendida):
    quantidade_vendida = int(quantidade_vendida)

    if quantidade_vendida <=0:
        print("Quantidade deve ser maior que 0")
        return False
    
    if quantidade_vendida > produto["quantidade_atual"]:
        print(f"Estoque insuficiente! Disponível: {produto['quantidade_atual']}")
        return False
    
    produto["quantidade_vendida"] += quantidade_vendida
    produto["quantidade_atual"] -= quantidade_vendida
    return True

def relatorio_produto(produto):
    valor_total = produto['preco'] * produto["quantidade_vendida"]
    print("=" * 40)
    print("\n=== RELATÓRIO ===".center(40))
    print("=" * 40)
    print(f"Produto: {produto['nome']}")
    print(f"Preço Unitário: R$ {produto['preco']:.2f}")
    print("=" * 40)
    print("\n=== Vendas ===")
    print("=" * 40)
    print(f"Quantidade Vendida: {produto['quantidade_vendida']}")
    print(f"Quantidade Inicial: {produto['quantidade_inicial']}")
    print(f"Quantidade Atual: {produto['quantidade_atual']}")
    print("-" * 40)
    print(f"\nValor total vendido: R$ {valor_total:.2f}")
    print("=" * 40)

