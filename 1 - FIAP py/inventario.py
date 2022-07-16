from os import sep
from funcoes import *


inventario={}
opcao=chamarMenu()
while opcao>0 and opcao<4:
    if opcao==1:
        registrar(inventario)
    elif opcao==2:
        persistir(inventario)
    elif opcao==3:
        resultado = exibir()
        print(resultado)
        for linha in resultado:
            #print(linha[2:-1])
            '''
            separacao=linha[linha.find(";")+1:-1]
            data=separacao[0:separacao.find(";")]
            separacao = separacao[separacao.find(";")+1:-1]
            descricao=separacao[0:separacao.find(";")]
            departamento=linha[linha.rfind(";")+1:-1]
            print("Data.........: ", data)
            print("Descrição....: ", descricao)
            print("Departamento.: ", departamento)
            '''
            '''
            separacao = linha[linha.find(";")+1:-1]#retina numero patrimonial e quebra de linha no final
            print("separacao 1: ",separacao)
            data = separacao[0:separacao.find(";")]
            separacao = separacao[separacao.find(";")+1:]#retira data
            print("separacao 2: ",separacao)
            descricao = separacao[0:separacao.find(";")]
            departamento = separacao[separacao.rfind(";")+1:]
            print("Data: ",data)
            print("Descrição: ", descricao)
            print("Departamento: ", departamento)
            '''
            lista = linha.split(";")
            print("Data: ",lista[0])
            print("Descrição: ", lista[2])
            print("Departamento: ", lista[3])
    opcao = chamarMenu()