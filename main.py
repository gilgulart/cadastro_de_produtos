import os
import webbrowser
from cadastro import cadastro
from relatorioCadastro import listaProdutos, salvaProdutos
from relatorioEstoque import relatorioEstoque

while True:
    def menu():
        print(f"{"=" * 20} MENU {"=" * 20} ")
        print(f"1 - Cadastrar Produtos")
        print(f"2 - Listar produtos")
        print(f"3 - Gerar Relatório de Estoque")
        print(f"4 - Remover SKU")
        print(f"5 - Sair")
    
    menu()
    option = int(input(">>> "))
    os.system('cls')
    
    if option not in [1,2,3,4,5]:
        menu()
        option = int(input(">>> "))

    if option == 1:
        
        try:
            produtos = listaProdutos()
            novo_produto = cadastro()
            produtos.extend(novo_produto)  
            
            salvaProdutos(produtos)
            
        except:
            produtos = cadastro()
            salvaProdutos(produtos)
        
        print('Produto Cadastrado!')
        
    if option == 2:
        listaProdutos()
        webbrowser.open('produtos.txt')
        
    if option == 3:
        produtos = listaProdutos()
        relatorioEstoque(produtos)
        webbrowser.open('estoque.txt')
    
    if option == 4:
        produtos = listaProdutos()
        sku = str(input('Digite o sku que deseja remover: '))
        
        for produto in produtos:
            if produto[0] == sku:
                produtos.remove(produto)
                salvaProdutos(produtos)
                print("Produto removido!")
                webbrowser.open('produtos.txt')
                    
                    
            else:
                sku = str(input('Digite um sku válido: '))
        
    if option == 5:
        break
    