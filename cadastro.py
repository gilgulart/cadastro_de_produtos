import random

def cadastro():
    quantidade = int(input('Quantos produtos deseja cadastrar? '))
    
    produtos = []

    for i in range(quantidade):
        sku = random.randint(1000, 9999)
        nome_produto = str(input(f'digite o nome do produto {i+1}: '))
        unidades = int(input(f'quanto você tem em estoque? '))
        custo = float(input(f'digite o custo unitário do produto {i+1}: '))
        print()

        produtos.append([ sku, nome_produto, unidades , custo])
    
    return produtos



    