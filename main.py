import os
import webbrowser
from relatorioCadastro import listaProdutos, salvaProdutos
from cadastro import cadastro

while True:
    print(f"{"=" * 50} MENU {"=" * 50} ")
    print(f"1 - Cadastrar Produtos")
    print(f"2 - Listar produtos")
    print(f"3 - Gerar Relatório Financeiro")
    print(f"4 - Sair")

    option = int(input(">>> "))
    os.system('cls')

    if option == 1:
        produtos = cadastro()
        salvaProdutos(produtos)
    if option == 2:
        listaProdutos()
        webbrowser.open('produtos.txt')
    if option == 3:
        break
    if option == 4:
        break