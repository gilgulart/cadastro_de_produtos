from relatorioCadastro import listaProdutos

def relatorioEstoque(produtos):
    estoque_total = 0
    custo_total_estoque = 0
    
    with open('estoque.txt', 'w' , encoding='utf8') as arquivo:
        arquivo.write(f"SKU ------------------ Produto ------------------ Un ------------------ Custo ------------------ Valor em estoque\n\n")
        
    
    for produto in produtos:
        estoque_total += int(produto[2])
        valor_em_estoque = int(produto[2]) * int(produto[3])
        custo_total_estoque += valor_em_estoque
            
        with open('estoque.txt', 'a') as arquivo:
            arquivo.write(f"{produto[0]} ------------------ {produto[1]} ------------------ {produto[2]} ------------------ R${produto[3]} ------------------ R${valor_em_estoque} \n")
            
    
    with open('estoque.txt', 'a', encoding='utf8') as arquivo:
        arquivo.write(f"\nEstoque total: {estoque_total} Un ------------------ R${custo_total_estoque}")
    
        
        
    
