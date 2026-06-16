from relatorioCadastro import listaProdutos

produtos = listaProdutos()

# venda_total = 0

def relatorioEstoque(produtos):
    estoque_total = 0
    
    with open('estoque.txt', 'w') as arquivo:
        arquivo.write(f"SKU ------------------ Produto ------------------ Quantidade\n\n")
        
    for produto in produtos:
        estoque_total += int(produto[2])
        valor_em_estoque = int(produto[2]) * int(produto[4])
        
        with open('estoque.txt', 'a') as arquivo:
            arquivo.write(f"{produto[0]} ------------------ {produto[1]} ------------------ {produto[2]}\n")
            
    
    with open('estoque.txt', 'a') as arquivo:
        arquivo.write(f"estoque total: {estoque_total}")
    
    with open('estoque.txt', 'a') as arquivo:
        arquivo.write(f"SKU ------------------ Produto ------------------ Quantidade ------------------ Custo Unitário ------------------ Valor em Estoque\n\n")
        
        
relatorioEstoque(produtos)
    
