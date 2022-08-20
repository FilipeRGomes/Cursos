"""

#Listas 


"""

#------------------------------------------------------------------------------------------------------------------------------------------
#   Listas
"""

Representação: []
Representam Vetores/Matrizes, são DINÂMICOS* e podem receber QUALQUER tipo de dado.

*Dinâmico: Não possiu tamanho fixo 
"""
#------------------------------------------------------------------------------------------------------------------------------------------
# 1
"""
lista_1 = [7, 9, 14, 1, 2, 3, 4, 5, 10]
lista_2 = ["a", "s", "d", "f"]
lista_4 = []
lista_5 = list(range(1, 11))
lista_6 = list("Palavra Decodificada")
valor = "a"

if valor in lista_6:
    print(f"Encontrei o {valor}")
else:
    print("Não encontrei ")

# 2 Ordenar
lista_1.sort()
lista_6.sort()
print(lista_1)
print(lista_6)

# 3 Contar
print(lista_6.count("a"))

# 4 Incluir valor no fim da lista
print(lista_1)
lista_1.append(42)  # so aceita um elemento
print(lista_1)

lista_1.append([22, 23, 89])  # so aceita um elemento
print(lista_1)


lista_1.extend([27, 28, 29])  # coloca cada elemento separado na lista
print(lista_1)

# 5 Insere valores em qualquer posição da lista
lista_1.insert(2, "novo valor")
print(lista_1)

# 6 Unir listas
lista_composta = lista_5 + lista_6
print(lista_composta)
"""

"""
# 7 Copia
lista_copiada = lista_2
print(lista_copiada)

# 8 Remove o ultimo valor
print(lista_5)
print(lista_5.pop())  # Remove da lista e retorna
print(lista_5)

# 9 Remove valor pelo indice
print(lista_5)
print(lista_5.pop(2))  # Remove da lista e retorna
print(lista_5)

# 10 Limpa a lista

# print(lista_5)
# lista_5.clear()  # a
# print(lista_5)

# 11 Converter string em lista

curso = "curso top de python"
print(curso)  # Separa pelo espaço Argumento: pode reeber outro separador
por_palavra = curso.split()
print(por_palavra)

# 12 Converter lista em string
palavra_lista = ["curso", "top", "de", "python"]
# print(curso) # Separa pelo espaço Argumento: pode reeber outro separador
palavra_string = " ".join(palavra_lista)
print(palavra_string)
"""

"""
# 13 for each
for elemento in lista_1:
    print(elemento)


# 14 while
carrinho = []
produto = ""

while produto != "SAIR":
    produto = input("Adicione um produto no carrinho ou digite sair: ").upper()
    if produto != "SAIR":
        carrinho.append(produto)

for produto in carrinho:
    print(produto)
"""

"""
#15 
cor_1 = "verde"
cor_2 = "amarelo"
cor_3 = "azul"
cores = [cor_1, cor_2, cor_3]
print(cores)

for indice, cor in enumerate(cores):
    print(indice, cor)
"""
"""
#16 retorna indice
numeros = list(range(1,50)) + list(range(3,33))
print(numeros)

#print(numeros.index(3))
#print(numeros.index(3, 5)) #numeros.index(valor_de_busca, indice_inicial)
#print(numeros.index(3, 5, 50)) #numeros.index(valor_de_busca, indice_inicial, indice_final)
"""


"""#17 Slice em listas
#lista[inicio:fim:passo]
#print(numeros[1:len(numeros):2])
"""

"""
#18 Invertendo Listas
nomes = ["nome 1", "nome 2"]
print(nomes)
nomes[0], nomes[1] = nomes[1], nomes[0]
print(nomes)
nomes.reverse()
print(nomes)
"""
"""
# 19 Busca valores: maximo, minimo, tamanho 

# Sendo inteiros/reais

numeros = list(range(1,50)) + list(range(3,33))
print("Soma: ", sum(numeros)) # Soma todos
print("Maximo: ", max(numeros)) # Maximo todos
print("Minimo: ", min(numeros)) # Soma todos
print("Tamanho: ", len(numeros)) # Tamanho (qualquer objeto na lista)

tupla = tuple(numeros)
print("Tupla: ", tupla) # Tamanho (qualquer objeto na lista)
"""

"""
#20 Desempacotamento
numeros = list(range(1,50)) + list(range(3,33))
print("Numeros: ", numeros) # 
numero_1, numero_2, numero_3 = numeros[0:3]

print("Numero 1: ", numero_1, "Numero 2: ", numero_2, "Numero 3: ", numero_3) # 
"""
"""
#21 Copiando listas (Shallow Copy e Deep Copy)
numeros = list(range(1,50)) + list(range(3,33))
print("Numeros: ", numeros) # 


#Deep Copy: copia uma lista para a outra de maneira independente
nova_deep = numeros.copy()
#print("Nova: ", nova_deep) # 
nova_deep.append(4)
#print("Numeros: ", numeros) # 
#print("Nova: ", nova_deep) # 

#Shallow Copy: Copia e gera vinculo entre as duas listas
nova_shallow = numeros
print("Nova: ", nova_shallow) # 
nova_shallow.append(4)
print("Numeros: ", numeros) # As duas listas foram atualizadas 
print("Nova: ", nova_shallow) # 
"""



#------------------------------------------------------------------------------------------------------------------------------------------
#   Tuplas
"""
Grande similaridade com listas

diferenças:
Representação: ()
São IMUTAVEIS toda a operação em tuplas gera uma nova tupla

"""
#------------------------------------------------------------------------------------------------------------------------------------------
"""
#1 Cuidado - São representadas por parenteses mas veja:

tupla_1 = (6, 5, 7, 4) # isso é uma tupla
print(tupla_1)
print(type(tupla_1))

tupla_2 = 6, 5, 7, 4 # isso também é uma tupla
print(tupla_2)
print(type(tupla_2))

# 2 Cuidado - São definidas pelo uso de "," e não de "()"
tupla_3 = (6) # isso não é uma tupla
print(tupla_3)
print(type(tupla_3))

tupla_4 = (6,) # isso é uma tupla
print(tupla_4)
print(type(tupla_4))

# 3 Pode ser usado range
tupla = tuple(range(0,10))


# 4 Desempacotamento de Tupla
dados = ("FURG", "EAUTO", "2016")
escola, curso, ano = dados
print(escola)
print(curso)
print(ano)

# 5 Adição e remoção de itens
# NÃO EXISTEM AS TUPLAS SÃO IMUTAVEIS

# 6 Também funcionam com tuplas
numeros = tuple(range(1,50)) + tuple(range(3,33)) # Concatenas duas tuplas em outra
print("Soma: ", sum(numeros)) # Soma todos
print("Maximo: ", max(numeros)) # Maximo todos
print("Minimo: ", min(numeros)) # Soma todos
print("Tamanho: ", len(numeros)) # Tamanho (qualquer objeto na lista)
print("Tupla: ", numeros) # T

numeros = numeros + tuple(range(10,60,4)) # Tuplas são imutaveis mas podem ser editadas
print("Tupla: ", numeros) # T

#
numeros = tuple(range(1,50)) + tuple(range(3,33)) # Concatenas duas tuplas em outra

# 7 Verifica se o objeto esta na tupla
print(6 in numeros)

# 8 Conta elementos
print(numeros.count(10)) 
"""
"""
# 9 Dicas 
#- Devemos usar tuplas SEMPRE que não precisarmos modificar os dados contidos na coleção
#- Tuplas são mais rapidas do que listas 
#- São mais seguras
meses = ("janeiro", "fevereiro", "marco", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro")
#print(meses[5])

# 10 Iteração com while
i = 0 
while i < len(meses):
    print(meses[i])
    i += 1

# 11 Verificar indice e existir
print(meses.index("fevereiro"))


# 11 Slicing
#tupla[inicio, fim, passo]
print(meses[2:])


#12 Copiando Tupla
tupla_1 = (5, 9, 4, 6, 14, 21, 2)

#So existe Shallow Copy
nova_shallow = tupla_1
print("Nova: ", nova_shallow) # 
print("Numeros: ", tupla_1) # As duas listas foram atualizadas 
"""

#------------------------------------------------------------------------------------------------------------------------------------------
#   Dicionarios
"""
Em outras linguagens são conhecidos com mapas, pois são coleções do tipo chave/valor

Representação: {"chave": "valor"}
OBS:
    - Chave e valor podem ser de qualquer tipo
    - Podemos misturar tipos de dados
    
Onde usar:

- Exemplo do Carrinho de Compras:
    - Produto 1:
        -Nome
        -quantidade
        -preço
    - Produto 2:
        -Nome
        -quantidade
        -preço    
     
"""
#------------------------------------------------------------------------------------------------------------------------------------------


"""
#1 Forma mais comun para criar dicionarios 
paises = {"br": "Brasil", "eua": "Estados Unidos", "py": "Paraguai"}
print(paises)
print(type(paises))

#2 Forma menos comun

paises_2 = dict(br="brasil", eua="Estados Unidos", py="Paraguai")
print(paises_2)
print(type(paises_2))
"""
"""
# 3 Acessando elementos via chave
paises = {"br": "Brasil", "eua": "Estados Unidos", "py": "Paraguai"}
#print(paises["br"])
#print(paises["py"])
#print(paises["ru"]) # chave que não existe -> KeyError

# 4 Acessando elementos via get (RECOMENDADO)
print(paises.get("br"))
#pais = paises.get("ru") #Não gera erro retorna None (Tipo sem tipo)
pais = paises.get("ru", "Não Encontrado")
print(pais) 

#if pais:
#    print("Encontrei")
#    
#else:
#    print("Não econtrei") 

# 5 Verifica se existe o valor
print("br" in paises)
print("eua" in paises)
print("ru" in paises)


#7 Tuplas são interessantes para representação de chaves pois são imutaveis

localidades= {
    (35.6895, 39.6917): "Escritorio Tokio",
    (40.7128, 74.0060): "Escritorio NY",
    (37.7749, 1222.4194): "Escritorio SP"
}

print(localidades)
print(type(localidades))

"""
"""
# 8 Adicionar elementos no dicionario 
#forma 1 - Mais comun
receita = {"janeiro": 100, "fevereiro":120, "marco":300}
print(receita)
receita["abril"] = 380
print(receita)

# forma 2
novo = {"maio":560}
receita.update(novo)
print(receita)

# 9 Alteando valores existentes

#forma 1 - Mais comun
receita["abril"] = 150
print(receita)

# forma 2
receita.update({"maio":780})
print(receita)
#Conclusão 1: A forma de adicionar novos elementos ou atualizar é a mesma
#Conclusão 2: Não aceita chaves repetidas
"""
"""
# 10 Removendo dados
#forma 1 - Mais Comun
receita = {"janeiro": 100, "fevereiro":120, "marco":300}
print(receita.pop("marco")) # se não encontrar retorna KeyError
print(receita) # 

#forma 2 
del receita["fevereiro"] # se não encontrar retorna KeyError | Não retorna o valor removido
print(receita) # 
"""

"""
# 11 Exemplo do carrinho

# Usando lista
carrinho_list = []
produto_1 = ["PS4", 1, 2300.00]
produto_2 = ["GoW 4 ", 1, 150.00]
carrinho_list.append(produto_1)
carrinho_list.append(produto_2)
#print(carrinho_list[0][0])

print(carrinho_list)
#Para acessar as informações temos que saber o indice de cada uma delas

# Usando lista
produto_1 = ["PS4", 1, 2300.00]
produto_2 = ["GoW 4 ", 1, 150.00]
carrinho_tupla = (produto_1, produto_2)

#print(carrinho_tupla[0][0])
print(carrinho_tupla)
#Para acessar as informações temos que saber o indice de cada uma delas

# Usando Dicionario
carrinho_dict = []
produto_1_d = {"nome":"PS4","quantidade": 1,"preco": 2300.00}
produto_2_d = {"nome":"GoW 4 ","quantidade": 1,"preco": 150.00}
carrinho_dict.extend([produto_1_d, produto_2_d])
print(carrinho_dict[0]["nome"])
print(carrinho_dict)
"""

# 12 Metodos com Dicionarios

"""
dicionario = {"a":1, "b":2, "c":3}
print(dicionario) 

# Limpar dicionario
#dicionario.clear()
#print(dicionario) 

# Copiando dicionarios
#DeepCopy 
novo = dicionario.copy()
novo["d"] = 4
print("original: ",dicionario) 
print("novo: ",novo) 

#ShallowCopy 
novo_s = dicionario
novo_s["d"] = 4
print("original: ",dicionario) 
print("novo: ",novo_s) 
"""
"""
# 14 Forma não usual de criação
outro = {}.fromkeys("a", "b")
usuario ={}.fromkeys(["nome", "pontos", "email", "profile"], "desconhecido") # fromkeys recebe cada valor iteravel com uma chave e o valor
print("Usuario: ",usuario) 

veja = {}.fromkeys("TESTE", "VALOR")
print("Veja: ",veja) 
"""
#------------------------------------------------------------------------------------------------------------------------------------------
#   Mapas
"""
São Dicionarios
"""
#------------------------------------------------------------------------------------------------------------------------------------------


receita = {"janeiro": 100, "fevereiro":120, "marco":300}
"""
for chave in receita:
    print(chave)


for chave in receita:
    print(receita[chave])    
    

for chave in receita:
    print(f"{chave}: {receita[chave]}")        
    
print(receita.keys()) # metodo recomendado
print(receita.values()) # metodo recomendado

# Desempacotamento de variaveis

for chave, valor in receita.items():
    print(f"{chave}: {valor}")        

# 2 Também funcionam com tuplas
print("Soma: ", sum(receita.values())) # Soma todos
print("Maximo: ", max(receita.values())) # Maximo todos
print("Minimo: ", min(receita.values())) # Soma todos
print("Tamanho: ", len(receita)) # Tamanho (qualquer objeto na lista)
"""
#------------------------------------------------------------------------------------------------------------------------------------------
#   Conjuntos
"""
Teoria de conjuntos da matematica

No Python são sets

- Não possuem valor duplicado
- Não possuem valores ordenados
- Elementos ão são acessados via inde, conjuntos não são indexados

São bons para se utilizar quando precisamos armazenar elementos sem se importar com a ordem deles, chaves, valores e itens duplicados

Diferença entre Conjunto (Set) e Dicionarios
    - Um dicionario tem chave e valor o Conjunto tem apenas valor
    

"""
#------------------------------------------------------------------------------------------------------------------------------------------
"""
#1 Criando Conjunto

s = set({1, 2, 3, 2, 9}) # valores ja existentes serão ignorados SEM gerar erro 
print(s)
print(type(s))
"""
"""
#2  Criando Conjunto mais comum
s = {1, 2, 3, 2, 9} # valores ja existentes serão ignorados SEM gerar erro 
print(s)
print(type(s))

conjunto_string = set("Geek University") # É possivel converter outros tipos para set
print(conjunto_string)


print(3 in s)
print("e" in conjunto_string)
"""

#s = set({0, 2, 3, 2, 9,True, "a"}) # Aceita todos os tipos de dados 
#print(s)
"""
# 3 Uso de Sets
#Visitantes de um museu, escreveram manualmente as cidades no formulario

cidades = ["Belo Horizonte", "São Paulo", "Pelotas", "São Paulo","Cuiaba", "Belo Horizonte"]

print(len(cidades))
print(set(cidades))
print(len(set(cidades)))
"""
"""
# 4 Adicionando elementos no conjunto

conjunto = {1, 2, 5}
conjunto.add(4)
conjunto.add(4) # Não gera erro mas ignora
print(conjunto)

# 5 Removendo elementos no conjunto
#forma 1
conjunto.remove(4) # O argumento é o valor a ser removido | se o valor não existir -> KeyError
print(conjunto)

#forma 2
conjunto.discard(2) # O argumento é o valor a ser removido | se o valor não existir NÃO retorna erro
print(conjunto)
"""

"""
# 6 Copiando Conjunto

conjunto = {1, 2, 5}
#Deep Copy
conjunto_novo = conjunto.copy()
conjunto_novo.add(4)
print("Original: ", conjunto)
print("Deep: ", conjunto_novo)

#Shallow Copy
conjunto_shallow = conjunto
conjunto_shallow.add(8)
print("Original: ", conjunto)
print("Deep: ", conjunto_shallow)
"""
"""
estudantes_python = {"Pedro", "Joao", "Marcos", "Julia", "Filipe", "Guilherme"}
estudantes_java = {"vitor", "Julia","Joao"}


#Alguns alunos que estudam python estudam java

# 1 UNIÃO- Gerar conjunto com nome dos estudantes unicos
#forma 1
unicos_1 = estudantes_java.union(estudantes_python) # Mais recomendado
print(unicos_1)
#unicos_1 = estudantes_python.union(estudantes_java) # igual a linha de cima

unicos_2 = estudantes_python | estudantes_java
print(unicos_2)
"""
"""
#2 Intersecção - Pertencem aos dois conjuntos
#Forma 1
ambos_1 = estudantes_python.intersection(estudantes_java)
print(ambos_1)

ambos_2 = estudantes_python & estudantes_java
print(ambos_2)


# 3 - Estudantes somente em um curso

so_python = estudantes_python.difference(estudantes_java)
so_java = estudantes_java.difference(estudantes_python)
print(so_python)
print(so_java)

"""
"""
s = {1, 5, 9, 15, 999}
# 4 Também funcionam com set
print("Soma: ", sum(s)) # Soma todos
print("Maximo: ", max(s)) # Maximo todos
print("Minimo: ", min(s)) # Soma todos
print("Tamanho: ", len(s)) # Tamanho (qualquer objeto na lista)
"""

#------------------------------------------------------------------------------------------------------------------------------------------
#   Modulo Collection Counter
"""
Collections -> High-Performace Container DateTypes

Counter -> Recebe um iteravel como parametro e cria um objeto do tipo Collections similar a um dicionario, sendo chave o elemento da lista passada e o valor a quantidade
"""
#------------------------------------------------------------------------------------------------------------------------------------------

from collections import Counter
import queue
"""
#1 Usando counter
lista = [1, 1, 1, 2, 3, 5, 5, 5, 99, 33, 66] 
res = Counter(lista) # Poderia ser qualquer objeto | Counter({1: 3, 5: 3, 2: 1, 3: 1, 99: 1, 33: 1, 66: 1})
print(res)
print(type(res))


# 2 
#print(Counter("Filipe Gomes"))

# 3 - Encontrando Palavras mais comuns
texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

palavras = texto.split()
#print(palavras)
res = Counter(palavras)
#print(res)
print(res.most_common(5))
"""
#------------------------------------------------------------------------------------------------------------------------------------------
#   Modulo Collection Dict
"""
Collections -> High-Performace Container DateTypes

Dict -> São dicionarios 
lambda -> Funções sem nome, podendo ou não receber parametros de entrada e retornar valores
"""
#------------------------------------------------------------------------------------------------------------------------------------------
"""
from collections import defaultdict
dicionario = {"Curso":"Python", "Instituicao": "Geek"}
#print(dicionario)
#print(dicionario["as"]) #KeyError

# 1 Valor Default | se a chave não existir cria e atribui o valor default

dicionario_2 = defaultdict(lambda: 0)
dicionario_2["Curso"] = "Python"
print(dicionario_2)

print(dicionario_2["outro"])
print(dicionario_2)
"""
#------------------------------------------------------------------------------------------------------------------------------------------
#   Modulo Collection OrderedDict
"""
Collections -> High-Performace Container DateTypes

Em dicionario normal a ordem não é garantida
"""
#------------------------------------------------------------------------------------------------------------------------------------------
"""
from collections import OrderedDict

dicionario = OrderedDict({"a":1, "b":2, "c":3,"d":4})
for chave, valor in dicionario.items():
    print(f"Chave: {chave} | Valor: {valor}")

dicionario_1 = {"a":1, "b":2}
dicionario_2 = {"b":2, "a":1}

print(dicionario_1 == dicionario_2) # True dicionarios comuns, não importa a ordem

o_dicionario_1 = OrderedDict({"a":1, "b":2})
o_dicionario_2 = OrderedDict({"b":2, "a":1})

print(o_dicionario_1 == o_dicionario_2) # False OrderedDict, a ordem importa
"""

#------------------------------------------------------------------------------------------------------------------------------------------
#   Modulo Collection NamedTuple
"""
Collections -> High-Performace Container DateTypes

Tupla diferenciada -> especificamos nome e parametro

"""
#------------------------------------------------------------------------------------------------------------------------------------------
"""
from collections import namedtuple
#1 forma 1 declaração
cachorro = namedtuple("cachorro","idade raca nome")

#Forma 2 declaração
cachorro_1 = namedtuple("cachorro","idade, raca, nome")


#Forma 3 declaração
cachorro_2 = namedtuple("cachorro",["idade", "raca", "nome"])
ray = cachorro_2(idade="2", raca="chowchow", nome="Ray")

# 2 Acessando as variaveis
#Forma 1
print(ray)
print(ray[0]) # idade
print(ray[1]) # raça
print(ray[2]) # nome
print("#---------------------------------------#")
#forma 2
print(ray.idade) # idade
print(ray.raca) # raça
print(ray.nome) # nome
"""


#------------------------------------------------------------------------------------------------------------------------------------------
#   Modulo Collection Deque
"""
Collections -> High-Performace Container DateTypes

Deque -> Lista de auta performace
"""
#------------------------------------------------------------------------------------------------------------------------------------------
"""
from collections import deque

deq = deque("Filipe")
print(deq)

#1  Adicionando elementos
deq.append(" G")
print(deq)

deq.appendleft("Nome:")
print(deq)

# Removendo elementos
print(deq.pop())
print(deq)
print(deq.popleft())
print(deq)
"""