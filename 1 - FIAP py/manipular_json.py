from Funcoes_JSON import *


inventario = lerArquivo("inventario.json")
opcao = chamarMenu()
while opcao>0 and opcao<3:
    if opcao==1:
        print(registrar(inventario, "inventario.json"))
    elif opcao==2:
        exibir("inventario.json")
    opcao = chamarMenu()