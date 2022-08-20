#------------------------------------------------------------------------------------------------------------------------------------------
#   List Comprehensions
"""
- Utilizando List Comprehension nos podemos gerar novas listas com dados processados a partir de outro iteravel


Sintaxe:

[dado for dado in interavel]

Exs:
-

O que é *kargs?

O parâmetro *args usado em uma função cloca os valores extras informados como uma tupla


"""
#------------------------------------------------------------------------------------------------------------------------------------------
"""
#1 Exemplo 
numeros = [1, 2, 3, 5, 7, 9]

#res = [numero * 10 for numero in numeros]
#res = [numero / 10 for numero in numeros]

def funcao(valor):
    return valor * valor


res = [funcao(numero) for numero in numeros]
print(res)

# Detalhando:
# for numero in numeros -> para cada um dos numeros em "numeros"
# multiplica por 1  gera uma nova lista 
# """
"""
# 2 List Comprehensions x loop
numeros = [1, 2, 3, 5, 7, 9]
numeros_dobrados = []

for numero  in numeros:
    numero_dobrado = numero * 2
    numeros_dobrados.append(numero_dobrado)

print(numero_dobrado)
print([numero *2 for numero in numeros])
"""
"""

# 3 Outro Exemplo
# EX1

nome = "geek university"
print([letra.upper() for letra in nome])

# EX2
amigos = ['Vanessa', 'Filipe', 'julia', 'pedro']
print([amigo.title() for amigo in amigos])


# EX3
print([numero*3 for numero in range(1,10)])

# EX4 
print([bool(valor) for valor in [0, [], '', True, 1, 3.14]])

# EX5 
print([str(numero) for numero in [1, 2, 3, 4, 5]])
"""

# Parte 2

# Podemos adicionar estrutura condicionais logicas as list Comprehension

# EX1
#numeros = list(range(1,20))
"""
print(numeros)
pares = [numero for numero in numeros if numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 != 0]
print(pares)
print(impares)
"""
"""
# EX1 Refatorando

pares = [numero for numero in numeros if not numero % 2]
impares = [numero for numero in numeros if numero % 2]
print(pares)
print(impares)

# EX2 
res = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]
print(res)
"""

#------------------------------------------------------------------------------------------------------------------------------------------
#   Listas Aninhadas (Nested Lists)
"""
- Algumas linguagens possuem arrays:
    - Unidimensional (Array/ Vetores)
    - Multidimensional (Matrizes)

- Em Python temos Listas

Sintaxe:

Exs:
-
"""
#------------------------------------------------------------------------------------------------------------------------------------------
"""
# EX1
listas = [[1,2,3],[4,5,6],[7,8,9]] # Representação de matriz com listas aninhadas
print(listas)
print(type(listas))

#Acessando dados
print(listas[0][1])
print(listas[2][1])
"""
"""
# Iterando com loop listas aninhadas

for lista in listas:
    for num in lista:
        print(num)

# List Comprehension

[[print(valor) for valor in lista] for lista in listas]

"""
"""
#EX2 - Matriz 3x3
tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]
print(tabuleiro)

#EX3 - Gerando jogadas no jogo da velha
velha = [['X' if numero % 2 == 0 else 'O' for numero in range(1, 4)] for valor in range(1, 4)]
print(velha)
"""

#------------------------------------------------------------------------------------------------------------------------------------------
#   Dictionary Comprehension
"""
-
-

Sintaxe:
{chave:valor for valor in iteravel}

Exs:
-
"""
#------------------------------------------------------------------------------------------------------------------------------------------
"""
# EX1 
numeros = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}

quadrado = {chave:valor ** 2 for chave, valor in numeros.items()}
print(quadrado)
"""
"""
# EX2
numeros = [1, 2, 3, 4, 5]
quadrado = {valor: valor ** 2 for valor in numeros}
print(quadrado)
"""
"""
# EX3 
chaves = 'abcde'
valores = [1, 2, 3, 4, 5]
mistura = {chaves[i]:valores[i] for i in range(0, len(chaves))}
print(mistura)
"""
"""
# EX4
numeros= [1, 2, 3, 4, 5]
res = {num: ('par' if num % 2 == 0 else 'impar') for num in numeros}
print(res)
"""
#------------------------------------------------------------------------------------------------------------------------------------------
#   Set Comprehension
"""
-
-

Sintaxe:
{chave:valor for valor in iteravel}

Exs:
-
"""
#------------------------------------------------------------------------------------------------------------------------------------------
"""
# EX1
numeros = {num for num in range(1, 7)}
print(numeros)
"""

"""
# EX2
numeros_2 = {x ** 2  for x in range(1, 7)}
print(numeros_2)

"""

"""
# Desafio: Alterar a estrutura acima para gerar um dicionario ao inves de um set
dicionario = {x:x ** 2  for x in range(1, 7)}
print(dicionario)
"""
"""
# EX 3
letras = {letra for letra in 'Geek University'}
print(letras)
"""

