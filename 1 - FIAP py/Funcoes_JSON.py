import json
import os

def chamarMenu():
    opcao=int(input("Digite: "
                      "<1> para registrar ativo"
                      "<2> para exibir ativos armazenados: "
                      "<3> para filtrar"))    
    return opcao

def lerArquivo(arquivo):
    if os.path.exists(arquivo):
        with open(arquivo,"r") as arq_json:
            dicionario = json.load(arq_json)
    else:
        dicionario = {}
    return dicionario
                
def gravarArquivo(dicionario,arquivo):
    with open(arquivo,"w") as arq_json:
        json.dump(dicionario,arq_json)

def registrar(dicionario, arquivo):
    resp = "S"
    while resp == "S":
        dicionario[input("Digite o número patrimonial: ")] = [
            input("Digite a data da última atualização: "),
            input("Digite a descrição: "),
            input("Digite o departamento: ")]
        resp = input("Digite <S> para continuar.").upper()
        gravarArquivo(dicionario, arquivo)
    return "JSON gravado"
    
    
def exibir(arquivo):
    dicionario = lerArquivo(arquivo)
    for chave, dado in dicionario.items():
        print("Data: ",dado[0])
        print("Descrição",dado[1])
        print("Departamento",dado[2])
        
def filtraPor(dicionario, key, por):
    dados_filtrados = []
    for chave, dado in dicionario.items():
        if chave == key:
            dados_filtrados = dado
        else:
            pass   
        
    if len(dados_filtrados) > 0:    
        if por == "DEPARTAMENTO":
            return dados_filtrados[2]
        elif por == "DATA":
            return dados_filtrados[0]

        elif por == "DESCRICAO":
            return dado[1]
        else:
            return "ERRO 021 - Categoria não existe"
    elif len(dados_filtrados) == 0:
        return "Patrimonio não existe"       