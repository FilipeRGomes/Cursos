"""

#Listas 
Representação: []
Representam Vetores/Matrizes, são DINÂMICOS* e podem receber QUALQUER tipo de dado.

*Dinâmico: Não possiu tamanho fixo 


"""
# Listas

# 1
lista_1 = [7, 9, 14, 1, 2, 3, 4, 5, 10]
lista_2 = ["a", "s", "d", "f"]
lista_4 = []
lista_5 = list(range(1, 11))
lista_6 = list("Palavra Decodificada")
valor = "a"
"""
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

cor_1 = "verde"
cor_2 = "amarelo"
cor_3 = "azul"
cores = [cor_1, cor_2, cor_3]
print(cores)
