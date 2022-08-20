#------------------------------------------------------------------------------------------------------------------------------------------
#  10 - Expressões Lambdas e  Funções integradas
"""
- La
-


Exs:
-
"""
#------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------
#  Lambdas
"""
- Funções anonimas ou sem nome
-
- Função em python:
def soma(a, b):
    return a + b


Exs:
-
"""
#------------------------------------------------------------------------------------------------------------------------------------------
"""
# EX1 Função em python
def funcao(x):
    return 3 * x + 1

print(funcao(4))

# EX1 lambda
calc = lambda x: 3 * x + 1

# Usando
print(calc(4))
"""
"""
# Podemos ter expressões lambda com multiplas entradas
nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title() 
print(nome_completo('angelina', 'jolie'))
print(nome_completo('  fElIcItY', ' jones  '))
"""
"""
amar = lambda : 'Como não amar python'

uma = lambda x: 3 * x + 1
#duas = lambda x1, x2, x3, ...: <expressão>
# """
"""
# Outros Exemplos

# EX2 
autores = ['Isaac Asimov', 'Ray Bradbury', 'Robert Heilein', 'Artur C. Clarc', 'Frank Herbert', ' Orson Scott Card', 'Douglas Adams', 'M. G. Wells', ' Leigh Bracket']
print(autores)

# Ordenar pelo sobrenome 
autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())
print(autores)
"""


# Função quadratica| f(x) = a * x ** 2 + b * x + c
def geradora_quadratica(a, b, c=0):
    """_summary_
    Função quadratica
    Args:
        a (real): Coeficiente de x**2
        b (real): coeficiente de x
        c (float, optional): Offset. Defaults to 0.

    Returns:
        real : f(x)
    """
    return lambda x: a * x ** 2 + b * x + c
"""
teste = geradora_quadratica(2, 3, -5)
print(teste(0))
print(teste(1))
print(teste(2))

print(geradora_quadratica(2, 3, -5)(14))
"""

#------------------------------------------------------------------------------------------------------------------------------------------
#  Map
"""
- Com map fazemos o mapeamento de valores para função
-

Exs:
-
"""
#------------------------------------------------------------------------------------------------------------------------------------------

import math


def area(raio):
    """_summary_
    Calcula a area do circulo com base no 'raio'
    Args:
        raio (real): Raio do Circulo

    Returns:
        Real: Retorna a area do circulo
    """
    return math.pi * (raio ** 2)

"""
#print(area(2))


raios = [3, 3, 0.5, 9, 44, 10]
areas = []
#  forma comum 
for r in raios:
    areas.append(area(r))

print(areas)

# Forma 2
areas_map = map(area, raios) # Map recebe dois parametros: 1º Função - 2º iteravel | Retorna um Map object
print(type(areas_map))
print(list(areas_map))

# Forma 3 - Map com lambda
print(list(map( lambda r : math.pi * (r ** 2), raios)))
# OBS: Apos usar a função map depois da primeira utilização do resultado ele limpa
      
"""
"""
# EX

cidades = [('Berlin', 29), ('Cairo', 36), ('Buenos Aires', 19), ('Los Angeles', 26), ('Tokio', 27), ('Nova York', 29)]
print(cidades)

# Converter celcius para farenheit

c_para_f = lambda dado: (dado[0], (9/5) * dado[1] + 32)
print(list(map(c_para_f, cidades))) # A função do argumento do map recebe um parametro
"""

#------------------------------------------------------------------------------------------------------------------------------------------
#  Filter
"""
- Filtra uma coleção de valores
-

Exs:
-
"""
#------------------------------------------------------------------------------------------------------------------------------------------
"""
valores = 1, 2, 3, 4, 5, 6

media = sum(valores)/len(valores)
print(media)
"""
"""
import statistics


# Filtrar valor acima da media

# dados de um sensor
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]
media = statistics.mean(dados)

# Assim como a função map a filter recebe dois parametros, uma função e um iteravel

res = filter(lambda x: x > media, dados)
var = res
print(list(var))
print(media)
print(list(var))
"""

"""
# EX 2 
paises = ['','Argentina','','Brasil','Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']
print(paises)
res = filter(None, paises) # Mais simples
#res = filter(lambda pais: len(pais) > 0, paises)
print(list(res))
"""

# Diferença Map x Filter: Map retorna um objeto mapeando a função para cada objeto | Retorna apenas os valores que retornam true da função passada como parametro


"""
# Exemplo
usuarios = [
    {"username":"Samuel", "tweets":["eu adoro bolo","eu adoro pizza"]},
    {"username":"Carlos", "tweets":["amo meu gato"]},
    {"username":"Jeff", "tweets":[]},
    {"username":"Bob123", "tweets":[]},
    {"username":"Doggo", "tweets":["Gosto de cachorro","Vou sair hoje"]},
    {"username":"gal", "tweets":[]}    
]
#print(usuarios)
# Filtrar usuarios inativos no tt
#forma 1
#inativos = list(filter(lambda u: len(u["tweets"]) == 0, usuarios))

#forma 2 
inativos = list(filter(lambda u: not u["tweets"], usuarios))

print(inativos)
"""
# Combinando filter e map

nomes = ['vanessa', 'ana', 'maria']

# Devemos criar uma lista com "Sua instrutora é" desde qe 


