"""
loop for


    for item in iteravel:
        # execução

    iteraveis
        -String
        -Lista
        -range

# 4 Enumerate
    (0, 'g')
    (1, 'e')
    (2, 'e')
    (3, 'k')


    for i, v in enumerate(nome):
        print(nome[i])

    for index, letra in enumerate(nome):
        print(letra)

    # _ -> Server para desconsiderar a variavel
    for _, letra in enumerate(nome):
        print(letra)


"""

"""
# exemplo for 1
nome = "geek"
lista = [1, 2, 3, 4, 5]
numeros = range(1, 10)


# 1
for letra in nome:
    print(letra)

# 2
for numero in lista:
    print(numero)

# 3
for numero in numeros:
    print(numero)

# 4 Enumerate
# for i, v in enumerate(nome):
for valor in enumerate(nome):
    print(valor)


# 5
qtd = int(input("repetições do loop"))
for n in range(1, qtd+1):
    print(f"imprimindo {n}")

# Ranges

# Ranges são usados para criar sequencias numericas não aleatorias

#sequencia = range(valor_de_parada)
#sequencia = range(valor_inicial, valor_de_parada)
#sequencia = range(valor_inicial, valor_de_parada, passo)
# sequencia = range(valor_inicial, valor_de_parada, -passo) #inversa

sequencia = range(12, 0, -1)


for num in sequencia:
    print(f"imprimindo {num}")
"""
"""
# While

# 1
numero = 1
while numero < 10:
    # print(numero)
    numero += 1

# 2
resposta = ''
while resposta != "SIM":
    resposta = input("digite sua resposta:  ").upper()
"""
"""
# Breaks - Saindo de loops comb Break
# O break é usado para sair de um loop de maneira projetada
for num in range(11):
    if num == 6:
        break
    else:
        print(f"{num}")
"""
resposta = ''
while True:
    if resposta == "SAIR":
        break
    else:
        resposta = input("Digite sair para parar:").upper()
