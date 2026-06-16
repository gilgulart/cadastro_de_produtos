# from relatorioCadastro import salvaProdutos

def cadastro():
    quantidade = int(input('Quantos produtos deseja cadastrar? '))

    produtos = []

    for i in range(quantidade):
        sku = f"{i + 1 :04d}"
        nome_produto = str(input(f'digite o nome do produto {i+1}: '))
        preco_venda = float(input(f'digite o preço do produto {i+1}: '))
        preco_compra = float(input(f'digite o custo do produto {i+1}: '))
        print()

        produtos.append([ sku, nome_produto, preco_venda, preco_compra])
    
    return produtos



    