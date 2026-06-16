from datetime import datetime
from cadastro import cadastro


def salvaProdutos(produtos):
    data_atual = datetime.now()

    try:
        with open('produtos.txt', 'r', encoding='utf8') as arquivo:
            linhas = arquivo.readlines()
            
            produtos_antigos = linhas[4:]
            
    except FileNotFoundError:
        produtos_antigos = []
        

    with open('produtos.txt', 'w', encoding='utf8') as arquivo:
        arquivo.write(f"Relatório de Produtos Cadastrados - {data_atual.strftime('%d/%m/%Y %H:%M:%S')}\n\n")
        arquivo.write(f"SKU ------------------ Produto ------------------ UN ------------------ Preço ------------------ Custo\n\n")
    
        arquivo.writelines(produtos_antigos)
    
    with open('produtos.txt', 'a', encoding='utf8') as arquivo:
        for produto in produtos:
            arquivo.write(f"{produto[0]} ------------------ {produto[1]} ------------------ {produto[2]} ------------------ R${produto[3]} ------------------ R${produto[4]}\n")
   
    return arquivo
   
def listaProdutos():
                
    produtos = []
        
    with open('produtos.txt', 'r', encoding='utf8') as arquivo:
        next(arquivo)
        next(arquivo)
        next(arquivo)
        next(arquivo)
        
        for linha in arquivo:
            data = linha.strip().split(' ------------------ ')
            print(linha)
            produtos.append(
                [data[0], data[1], data[2] , float(data[3].replace("R$", "")), float(data[4].replace("R$", ""))]
            )
            
    return produtos