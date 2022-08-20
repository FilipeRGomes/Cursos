# ------------------------------------------------------------------------------------------------------------
# Reduce
"""

Não é mais uma função integrada (bulit-in) a partir do Py3+



"Utilize a função reduce() somente quando precisar dela, e m todo caso 99% das vezes um loop for é mais legivel." - Guido van Rossum


# Imageine uma coleção de dados

dados = [a1, a2, ..., an]

def funca(x, y):
    return x * y


Assim como map e filter:
reduce(funcao, dados)



Execução

    Passo 1: res1 = f(a1,a2) # Aplica os dois primeiros valores na função
    # Aplica o resultado anterior mais o terceiro elemento
    passo 2: res2 = f(res1, a3)
    .
    .
    .
    passo n: resn = f(resm, an) # m = n-1



Alternativamente:
    funcao(funcao(funcao(funcao(a1,a2),a3),...),an)

"""
# ------------------------------------------------------------------------------------------------------------

"""
from functools import reduce

dados = [2, 3, 4, 5, 7, 11, 13, 17, 19, 23, 29]


def multi(x, y): return x * y


res = reduce(multi, dados)
print(res)

# usando loop

res_2 = 1

for n in dados:
    res_2 = res_2 * n

print(res_2)
"""
# ------------------------------------------------------------------------------------------------------------
# All
"""
True se todos os elementos do iteravel são verdadeiros ou ainda se o iteravel esta vazio
"""
# ------------------------------------------------------------------------------------------------------------
"""
# print(all([1, 2, 3]))
# print(all([0, 1, 2, 3]))
# print(all([]))

nomes = ['Carlos', 'Cassiano', 'Camila', 'Carla']


print(all([nome[0] == 'C' for nome in nomes]))

print(all([letra for letra in 'eiof' if letra in 'klz']))  # Exemplo bad
print(all(numero for numero in [4, 2, 10, 6, 8]
      if numero % 2 == 1))  # Exemplo bad
# OBS: um iteravel vazio é true
"""


# ------------------------------------------------------------------------------------------------------------
# Any
"""
True se qualquer elemento for verdadeiro, se estiver vazio retorna False
"""
# ------------------------------------------------------------------------------------------------------------
"""
print(any([1, 2, 3]))
print(any([0, False, {}, (), []]))
nomes = ['Carlos', 'Cassiano', 'Camila', 'Carla', 'Vanessa']
print(any([nome[0] == 'C' for nome in nomes]))
print(any([numero for numero in [4, 2, 10, 6, 8, 9] if numero % 2 == 0]))
"""


# ------------------------------------------------------------------------------------------------------------
# Generators
"""

Diferença Visual

- List Comprehension : []
- Generator : () -> Usa menos recurso de memoria



"""
# ------------------------------------------------------------------------------------------------------------
# Usando Generators


"""
nomes = ['Carlos', 'Cassiano', 'Camila', 'Carla', 'Vanessa']
# print(any(nome[0] == 'C' for nome in nomes))

print('----------------')
print(getsizeof('geek'))
print(getsizeof(10*'geek'))

print('----------------')
print(getsizeof(1))
print(getsizeof(99999999999999))

print('----------------')
print(getsizeof(True))
print(getsizeof(False))
"""

# Gerando Lista
"""
list_comp = getsizeof([x * 10 for x in range(1000)])

# set
set_comp = getsizeof({x * 10 for x in range(1000)})

# dict
dict_comp = getsizeof({x: x * 10 for x in range(1000)})

# Generator

gen = getsizeof(x * 10 for x in range(1000))

print('List Comp: ', list_comp, 'bytes')
print('Set Comp: ', set_comp, 'bytes')
print('Dict Comp: ', dict_comp, 'bytes')
print('gen Comp: ', gen, 'bytes')
"""
"""
# Iterando com generator
# Retorna a quantidade de bytes em memoria do elemento passado como parametro
from sys import getsizeof
gen = (x * 10 for x in range(100))
print(gen)
print('gen Comp: ', getsizeof(gen), 'bytes')

for num in gen:
    print(num)
"""

# ------------------------------------------------------------------------------------------------------------
# Sorted
"""

- Ao contrario do sort() pode ser usado com QUALQUER iteravel
- Não altera o iteravel original gera uma lista nova

"""
# ------------------------------------------------------------------------------------------------------------
"""
# Lista
numeros = [4, 22, 2, 8, 11, 66, 44]
print(numeros)
print(sorted(numeros))
# Tu´pla
numeros_t = [4, 22, 2, 8, 11, 66, 44]
print(numeros_t)
print(sorted(numeros_t))
# Outros parametros
print(sorted(numeros_t, reverse=True))
"""

"""

usuarios = [
    {'username': 'Samuel', 'tweets': [
        'TESTE-TESTE-TESTE-', 'TESTE-TESTE-TESTE-TESTE-']},
    {'username': 'Carla', 'tweets': [
        'TESTE-TESTE-TESTE-']},
    {'username': 'Jeff', 'tweets': []},
    {'username': 'bob123', 'tweets': []},
    {'username': 'Doggo', 'tweets': [
        'TESTE-TESTE-', 'TESTE-TESTE-TESTE-']},
    {'username': 'gal', 'tweets': []}
]
print(usuarios)
print('----------------')
# Ordena pelo nome de usuario
print(sorted(usuarios, key=lambda usuario: usuario['username']))
print('----------------')
# Ordena pelo numero de tweets
print(sorted(usuarios, key=lambda usuario: len(usuario['tweets'])))
print('----------------')
"""
"""
musicas = [
    {'titulo': 'Thunderstrucj', 'tocou': 3},
    {'titulo': 'FF', 'tocou': 99},
    {'titulo': 'GG', 'tocou': 2},
    {'titulo': 'HH', 'tocou': 4},
    {'titulo': 'jj', 'tocou': 32}
]

print("As mais tocadas", sorted(
    musicas, key=lambda musicas: musicas['tocou'], reverse=True))
"""

# ------------------------------------------------------------------------------------------------------------
# Min e Max
"""

- Ao contrario do sort() pode ser usado com QUALQUER iteravel
- Não altera o iteravel original gera uma lista nova

"""
# ------------------------------------------------------------------------------------------------------------

"""
lista = [1, 2, 6, 99, 658, 78, 44, 129]
print(min(lista))
print(max(lista))
print('----------------')

tupla = (1, 2, 6, 99, 658, 78, 44, 129)
print(min(tupla))
print(max(tupla))
print('----------------')

conjunto = {1, 2, 6, 99, 658, 78, 44, 129}
print(min(conjunto))
print(max(conjunto))
print('----------------')

dicionario = {'a': 1, 'b': 2, 'c': 6, 'd': 99,
              'e': 658, 'f': 78, 'g': 44, 'g': 129}
print(min(dicionario.values()))
print(max(dicionario.values()))
print('----------------')
"""

# programa que recebe dados do usuario e verifica o maior
"""
val_2, val_1 = input('Informe o segundo valor: '),  input(
    'Informe o primeiro valor: ')

print("O maior valor é: ", max(val_2, val_1))
print("O maior valor é: ", min(val_2, val_1))
"""
"""
print(max('a', 'ab', 'abc'))
print(min('a', 'ab', 'abc'))

print(max(3.14, 3.18))
print(min(3.14, 3.18))

print(max('Filipe Gomes'))
print(min('Filipe Gomes'))
"""
"""
nomes = ['Arya', 'Samson', 'Dora', 'Tim', 'Ollivander']
print(nomes)
print("Original max: ", max(nomes))
print("Original min: ", min(nomes))

print("Maior nome: ", max(nomes, key=lambda nome: len(nome)))
print("Menor nome: ", min(nomes, key=lambda nome: len(nome)))
"""


from cgi import print_arguments
musicas = [
    {'titulo': 'Thunderstrucj', 'tocou': 3},
    {'titulo': 'FF', 'tocou': 99},
    {'titulo': 'GG', 'tocou': 2},
    {'titulo': 'HH', 'tocou': 4},
    {'titulo': 'jj', 'tocou': 32}
]
# print(musicas)
# print("Original max: ", max(musicas))
# print("Original min: ", min(musicas))
"""
print("Mais tocada: ", max(musicas, key=lambda musica: musica['tocou']))
print("Menos tocada: ", min(musicas, key=lambda musica: musica['tocou']))

# Desafio nome da musica mais e menos tocada

print("Mais tocada por nome: ", max(
    musicas, key=lambda musica: musica['tocou'])['titulo'])
print("Menos tocada por nome: ", min(
    musicas, key=lambda musica: musica['tocou'])['titulo'])
"""
# Desafio nome da musica mais e menos tocada sem lambda
"""
max = 0
min = 999999
for musica in musicas:
    if musica['tocou'] > max:
        max = musica['tocou']
        mais_tocada = musica

print(mais_tocada['titulo'])

for musica in musicas:
    if musica['tocou'] < min:
        min = musica['tocou']
        menos_tocada = musica

print(menos_tocada['titulo'])
"""


# ------------------------------------------------------------------------------------------------------------
# Reversed
"""
- Não confundir com reverse
- reverse() -> Somente para listas
- reversed() -> Qualquer tipo de dado

"""
# ------------------------------------------------------------------------------------------------------------

"""
lista = [1, 2, 3, 4, 5, 6, 7, 8, ]

res = reversed(lista)
print(res)
#
lista_nova = list(res)  # Salva em memoria
print(lista_nova)
print(tuple(reversed(lista)))
print(set(reversed(lista)))  # Não guarda ordem
print('-', lista_nova)
lista_nova += " FEITO"
print('-', lista_nova)

# for letra in reversed('Palindromo fica top'):
#    print(letra, end='')

print(''.join(list(reversed('Palindromo fica top'))))
print()
"""

# ------------------------------------------------------------------------------------------------------------
# Len, Abs, Sum , Round
"""

# Len -> Tamanho de um iteravel

# Abs -> Retorna o valor real

# sum -> Soma valores de um iteravel sum(iteravel, valo_adicionado_final)

# Round -> Arredonda round(numero, casas_decimais)
"""
# ------------------------------------------------------------------------------------------------------------
"""

# Len -> Tamanho de um iteravel

print(len('Geek UNiversity'))
print(len([1, 2, 3, 5, 6]))
print(len({1, 2, 3, 5, 6}))
print(len({'a': 1, 'b': 2, 'c': 3, 'd': 5, 'e': 6}))
print(len(range(10)))
# print(len())


# Por baixo
# Dunder len
print('Geek UNiversity'.__len__())
"""

# ABS -> Retorna o valor real
"""
print(abs(1))
print(abs(2))
print(abs(-3.1415))
"""
"""
# Sum

print(sum([1, 2, 3, 4, 5]))
print(sum((1, 2, 3, 4, 5), 5))
print(sum({1, 2, 3, 4, 5}, 5))
print(sum({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}.values(), 5))

# Round
print(round(10.2))
print(round(10.5))
print(round(10.7))
print(round(10.554, 2))
print(round(10.555, 2))
print(round(10.556, 2))
"""

# ------------------------------------------------------------------------------------------------------------
# Zip
"""
zip() -> Cria um iteravel (zip-object) que agrega elemento de cada um dos iteraveis passados como entrada em pares
"""
# ------------------------------------------------------------------------------------------------------------

#
"""
lista_1 = [1, 2, 3]
lista_2 = [4, 5, 6]

zipado = zip(lista_1, lista_2)
print(zipado)
print(type(zipado))
lista_zipada = list(zipado)  # Persistencia dos dados
print(lista_zipada)
print(tuple(lista_zipada))
print(set(lista_zipada))
print(dict(lista_zipada))


lista_3 = [1, 2, 3, 4, 5, 6]
# Ignora os elementos restantes da lista maior
zipado_2 = zip(lista_1, lista_2, lista_3)
print(list(zipado_2))
"""
"""
tupla = 1, 2, 3
lista = [4, 5, 6]
dicionario = {'a': 7, 'b': 8, 'c': 9}

zt = list(zip(tupla, lista, dicionario, dicionario.values()))
print(zt)
"""

prova_1 = [80, 91, 78]
prova_2 = [98, 89, 53]
alunos = ['maria', 'pedro', 'carla']

# ---------------------------------------------------------------------------------------------------
#####################################################################################################
# Sacada muito top
final = {dado[0]: max(dado[1], dado[2])
         for dado in zip(alunos, prova_1, prova_2)}


# Com map
final_2 = dict(zip(alunos, map(lambda nota: max(nota), zip(prova_1, prova_2))))
print(final_2)
