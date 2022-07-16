from os import sep
from funcoes import *

with open("economic-indicators.csv","r") as boston:
    #Monta Estrutura de dados
    dados = {}
    ano = []
    id_coluna = 0
    #Cria chaves do dicionario
    linhas = boston.readlines()
    primeira_linha = linhas[0]
    #print("Primeira linha",primeira_linha,"\n")
    for coluna in primeira_linha.split(","):
        dados[coluna] = []
        aux = []
        for linha in linhas[1:]:
            aux.append(linha.split(",")[id_coluna].rstrip())
        id_coluna += 1
        dados[coluna] = aux   
        #print(coluna, ":",dados[coluna])
        #print("\n","----------------------------------------------------","\n")
        
        
def SomaColuna(dados,key):
    total = 0
    print(dados[key])
    for valor in dados[key]:
        #if valor != "None":
        print(valor)
        total += int(valor)
    return total

def Maior(dados, key):
    maiorValor = max(dados[key])
    idMaiorValor = dados[key].index(maiorValor)
    #print ("Valor",maiorValor)
    #print ("Index",idMaiorValor)
    return maiorValor, idMaiorValor

#Verifica ano com maior numero de passageiros
def NumeroPassageiros(dados,key):
   valor, id =  Maior(dados,key)
   ano = dados["Year"][id]
   mes = dados["Month"][id]
   return ano, mes


def SomaColunaFiltrada(dados, key, ano):
    soma = 0
    for linha in dados["Year"]:
        #print("linha", linha, type(linha))
        #print("ano", ano, type(ano))
        if int(linha) == ano:
            id = dados["Year"].index(linha)
            soma = soma + int(dados[key][id])
    print(soma)
            
def MaiorPreco(dados, key, ano):
    maior_preco = 0
    lista_precos = []
    for linha in dados["Year"]:
        if int(linha) == ano:
            id = dados["Year"].index(linha)
            print("Linha", linha, "preço",dados[key][id],"id",id)
            #lista_precos.append(dados[key][id])
    print(lista_precos)      

#print(SomaColuna(dados,"logan_intl_flights"))
#Maior(dados,"logan_intl_flights")
#print(NumeroPassageiros(dados,"logan_passengers"))
#SomaColunaFiltrada(dados, "logan_passengers", 2019)
MaiorPreco(dados,"med_housing_price",2018)