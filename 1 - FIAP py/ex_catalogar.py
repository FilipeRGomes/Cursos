from ast import Return
from Funcoes_JSON import *

inventario = lerArquivo("inventario.json")
opcao = chamarMenu()


    
while opcao>0 and opcao<4:
    if opcao==1:
        print(registrar(inventario, "inventario.json"))
    elif opcao==2:
        exibir("inventario.json")
    elif opcao==3:
        print(filtraPor(inventario, input("Digite o Numero de patrimonio:  ").upper(), input("Digite a informação desejada:  ").upper()))
    opcao = chamarMenu()