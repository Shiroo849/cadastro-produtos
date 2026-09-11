# Sistema de Controle de Estoque e Vendas

Sistema simples em Python, via terminal, para cadastro de produtos, controle de vendas e geração de relatórios.

## Funcionalidades
- Cadastrar produto: nome, preço unitário e quantidade inicial em estoque
- Realizar venda: baixa automática no estoque, com validação de quantidade disponível
- Relatório: exibe dados de cada produto (estoque inicial, vendido, atual e valor total vendido)

## Estrutura do projeto
````text
├── Produtos.py     # Regras de negócio (cadastro, venda e relatório)
└── main.py         # Menu interativo (interface com o usuário)
````

## Exemplos de uso
````text
=== MENU ===
[1] Cadastrar produto
[2] Realizar venda
[3] Relatório
[0] Sair
Opção: 1

Produto: Caneta
Preço Unitário: R$ 2.50
Quantidade inicial: 100
✔ Produto 'Caneta' cadastrado com sucesso!
````

## Melhorias Futuras
````text
 - Persistência de dados em arquivo (JSON/CSV) para não perder o cadastro ao fechar o programa
 - Edição e exclusão de produtos
 - Busca de produto por nome
 - Relatório consolidado de todos os produtos (total geral de vendas)
 - Testes automatizados
````
