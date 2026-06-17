import os
import webbrowser
from cadastro import cadastro
from relatorioCadastro import listaProdutos, salvaProdutos
from relatorios import relatorioEstoque

while True:
    def menu():
        print(f"{"=" * 20} MENU {"=" * 20} ")
        print(f"1 - Cadastrar Produtos")
        print(f"2 - Listar produtos")
        print(f"3 - Gerar Relatório de Estoque")
        print(f"4 - Sair")
    
    menu()
    option = int(input(">>> "))
    os.system('cls')
    
    if option not in [1,2,3,4]:
        menu()
        option = int(input(">>> "))

    if option == 1:
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
        break