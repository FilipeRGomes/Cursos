# ------------------------------------------------------------------------------------------------------------------------------------------
#  Leitura de Arquivos
"""

- open(nome_arquivo, modo) -> Função build-in que abre um arquivo | 
    - Forma mais simples open(nome_arquivo) 
    - Retorna um TextIOWrapper 
    
- modos:
    - r -> Somente leitura | default
    - w -> Escrita | Sobrepoe se existir
    - x -> Abre para a escrita somente se o arquivo não existir
    - a -> Abre para a escrita e adiciona no final
-     
#OBS: Por padrão abre o arquivo para leitura, se não existir retorna FileNotFoundError
- read() -> le todo conteudo do arquivo


OBS:
- Quando um arquivo é abert com open() é criada uma conexao
entre o arquivo e o programa chamada de (streaming) ao finalizar
o trabalho com o arquivo devemos fechar a coneção 

- Passos para trabalhar com o arquivo
1 - Abre
2 - Processa
3 - Fecha

Exs:
-
"""
# ------------------------------------------------------------------------------------------------------------------------------------------
"""
arquivo = open('texto.txt')
#print(arquivo)
#print(type(arquivo))

#Ler o conteudo do arquivo
ret = arquivo.read()
print(ret) # O python utiliza um recurso para trabalhar com arquivos chamado cursor, esse funciona como o cursor quando estamos escrevendo
print(type(ret))
#print(arquivo.read())
# Separa por linha
ret_l = ret.split('\n')
print(ret_l)
"""

# ------------------------------------------------------------------------------------------------------------------------------------------
#  Seek e Cursors
"""

- seek() -> Move o cursor no arquivo
Exs:

arquivo.read(max_carac)
-
"""
# ------------------------------------------------------------------------------------------------------------------------------------------
from genericpath import isfile
from operator import is_
from posixpath import split


arquivo = open('texto.txt')
#ret = arquivo.read()
"""
print(ret) # O python utiliza um recurso para trabalhar com arquivos chamado cursor, esse funciona como o cursor quando estamos escrevendo
print('$$$------------------------------------$$$')
print(arquivo.read())

# Movimentando o cursor
arquivo.seek(0)
print(arquivo.read())

# Movimentando o cursor
arquivo.seek(20)
print(arquivo.read()) # 
"""
"""
#Le linha por linha
print(arquivo.readline())
#print(arquivo.readline())
#print(arquivo.readline())
#print(type(arquivo.readline()))
print(arquivo.readline().split(' '))

"""
"""
#Ja converte para lista
print(arquivo.readlines())
print("Fechou: ", arquivo.closed)

arquivo.close()
print("Fechou: ", arquivo.closed)
"""

# ------------------------------------------------------------------------------------------------------------------------------------------
#  Bloco With
"""

- seek() -> Move o cursor no arquivo
Exs:

arquivo.read(max_carac)
-
"""
# ------------------------------------------------------------------------------------------------------------------------------------------
"""
with open('texto.txt') as arquivo:
    print(arquivo.readlines())
    print("Fechou: ", arquivo.closed)
    

print("Fechou: ", arquivo.closed)

"""


# ------------------------------------------------------------------------------------------------------------------------------------------
#  Escrita

"""# se não existe cria se existe sobrepoe conteudo
with open('texto.txt', 'w') as arquivo:
    arquivo.write('Escrever em arquivos é muito facil\n')
    

print("Fechou: ", arquivo.closed)

with open('texto.txt', 'w') as arquivo:
    arquivo.write('Escrever em arquivos é muito facil\n'*1000)
"""
"""
with open('texto.txt', 'w') as arquivo:
    while True:
        fruta = input('Fruta ou Sair: ').upper()
        if fruta != 'SAIR':
            arquivo.write(fruta + '\n')
        else:
            break

"""        
# ------------------------------------------------------------------------------------------------------------------------------------------
#  Abre se não existir

"""
with open('texto.txt', 'x') as arquivo:
    arquivo.write('Escrever em arquivos é muito facil\n'*1000)

"""
"""
# Escreve no final
with open('texto.txt', 'a') as arquivo:
    while True:
        fruta = input('Fruta ou Sair: ').upper()
        if fruta != 'SAIR':
            #Para escrever no inico
            #arquivo.seek(0) #So adiciona no final
            arquivo.write(fruta + '\n')
        else:
            break
"""

"""# Escreve no final
with open('texto.txt', 'a+') as arquivo:
    while True:
        fruta = input('Fruta ou Sair: ').upper()
        if fruta != 'SAIR':
            #Para escrever no inico
            #arquivo.seek(0) #So adiciona no final
            arquivo.write(fruta + '\n')
        else:
            break
"""
"""
# Handson Inicio
with open('texto.txt', 'r+') as arquivo:
    while True:
        fruta = input('Fruta ou Sair: ').upper()
        if fruta != 'SAIR':
            #Para escrever no inico
            temp = arquivo.read()
            arquivo.seek(0)
            arquivo.write(fruta + '\n'+ temp)
        else:
            break
            
"""
# ------------------------------------------------------------------------------------------------------------------------------------------
#  StringIO
"""

- Para ler um arquivo é necessario ter permição
- O string IO é usado para criar arquivos em memoria 
"""
# ------------------------------------------------------------------------------------------------------------------------------------------
"""
from io import StringIO

mensagem = 'String normal'
#Criar arquivo em memoria

arquivo = StringIO(mensagem)
#Posso fazer tudo que faria com um arquivo
print(arquivo.read())
arquivo.seek(0)
arquivo.write(arquivo.read())
"""

# ------------------------------------------------------------------------------------------------------------------------------------------
#  Sistema de arquivos e navegação
"""

-  Para manipular os arquivos precisamos usar o modulo OS
"""
# ------------------------------------------------------------------------------------------------------------------------------------------

import os

# Get CurrentWorkDirectory (cwd)
print(os.getcwd())
"""
# Mudar de diretorio
os.chdir('..')
print(os.getcwd())
"""
"""
print(os.path.isabs('C:\\Users\\filipe.rita.gomesDocuments\\99 - Temporario\\2 - Python Basico ao Avançado'))
"""

#Identificando o so
print(os.name)

#Mais detalhes
#print(os.uname_result()) # Não rola window

"""
import sys
print(sys.platform)"""

''
"""
# Mudando caminho
print(os.getcwd())
res = os.path.join(os.getcwd(), 'dir1', 'dir2')


os.chdir(res)
print(os.getcwd())
"""

#print(os.path.isabs('C:\\Users\\filipe.rita.gomesDocuments\\99 - Temporario\\2 - Python Basico ao Avançado'))
#print(os.listdir('dir1\\dir2'))
"""
# Com mais detalhes
with os.scandir('dir1') as scan:
    scan_diretorio = list(scan)
# scan.close() # É necessario fechar o scandir

print('Nome: ',scan_diretorio[0].name) #Nome
print('Inode: ',scan_diretorio[0].inode()) #Nome
print('Is Dir:',scan_diretorio[0].is_dir()) #Nome
print('Is File: ',scan_diretorio[0].is_file()) #Nome
print('Path: ',scan_diretorio[0].path) #Nome
print('Stat: ',scan_diretorio[0].stat()) #Nome
#É necessario fechar o scandir
"""
# ------------------------------------------------------------------------------------------------------------------------------------------
#  Sistema de arquivos manipulação
"""

-  Para manipular os arquivos precisamos usar o modulo OS
"""
# ------------------------------------------------------------------------------------------------------------------------------------------
import os

"""
#Verificando se o diretorio/arquivo existe
print(os.path.exists('texto.txt'))
print(os.path.exists('te.txt'))
print(os.path.exists('dir1'))
      
print(os.path.exists('dir1\\dir2'))
"""

#Criando arquivo 

#Não recomendadas
"""
#forma 1
open('novo_arquivo.txt', 'w').close()

#forma 2
open('novo_arquivo.txt', 'a').close()
#Forma 3 
with open('novo_arquivo.txt', 'a') as arquivo:
    pass
"""
"""
#Recomendada para criar arquivos, não funciona no windows
os.mknod('teste.txt')
os.mknod('dir1\\dir2\\university.txt')
"""
"""
#Recomendada para criar diretorios cria um de cada vez
os.mkdir('teste')
os.mkdir('dir1\\dir2\\university')
"""
"""
#Criando multiplos diretorios
os.makedirs('dir3\\dir2\\university')
"""
"""
#Renomeando
os.rename('dir3', 'univ') # se não existir file notfound error
"""

#Deletando
#OBS: Cuidado com os comando de delete pois não vai para a lixeira,são excluidos permanentemente 
#os.remove('texto.txt') # Arquivos | se não existir file notfound error
#os.rmdir('univ/dir2')
# Se ja estiver aberto PermissionError

"""
#Limpando pasta | Funciona muito bem se as subpastas estiverem vazias
diretorio = 'dir1\dir2'
for arquivo in os.scandir(diretorio):
    print(f'- {arquivo.name}')
    if arquivo.is_file():
        os.remove(arquivo.path)
    if not arquivo.is_file():
        os.rmdir(arquivo.path)
"""

# os.removedirs() # Remove todos os diretorios da arvore SE estiverem vazios


#Pacote send2trash

# ------------------------------------------------------------------------------------------------------------------------------------------
#  Trabalhando com arquivos e diretorios temporarios
"""

-  Para manipular os arquivos precisamos usar o modulo OS
"""
# ------------------------------------------------------------------------------------------------------------------------------------------

import tempfile

with tempfile.TemporaryDirectory() as tmp:
    print(f'Criei um diretorio temporario em: {tmp}')
    with open(os.path.join(tmp, 'arquivo_temporario.txt'), 'w') as arquivo:
        arquivo.write('Trabalhando com arquivos temporarios \n')
    input('Sgura')