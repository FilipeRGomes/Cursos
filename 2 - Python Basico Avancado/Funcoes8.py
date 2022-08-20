#------------------------------------------------------------------------------------------------------------------------------------------
#   Seção 8 Funções
"""

"""
#------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------
#   Definindo Funções
"""
- Trechos de codigos que executam funções especificas
- Pode ou não receber e retornar argumentos
- Principio DRY - Don't Repeat Yourself
- exemplos:
    -print()
    -min()
    -len()
    -max()
    -count()
    
OBS: Se escrever uma função que executa diversas tarefas, refatorar em funções menores
"""
#------------------------------------------------------------------------------------------------------------------------------------------
#1 Exemplo uso de funções

"""
cores = ["verde", "amarelo", "azul", "branco"]

curso = "Programação em Python: Essencial"

#Funções integradas "built-in"
#print(cores)
cores.append("roxo")
#print(cores)

#curso.append("verde") # Erro de tipo de entrada
"""
# 2 Criando Funções

"""
def nome_da_função(opcional:parametros):
    bloco_da_funcao
   
Para definir a função usamos a palavra reservada "def"    
"""
"""
# Definindo primeira função
def diz_oi():
    print("Oi!")


#diz_oi()

# ex 2 
def canta_parabens():
    print("Parabens pra você")
    print("Nessa data querida")
    print("Muitas Felicidades")
    print("Viva o Aniversariante")
    
#canta_parabens()


#Podemos criar variaveis do tipo de uma função e executar a função pela variavel | Não é comum e nem usual
canta = canta_parabens
canta()
"""
# 3 Funções com Retorno
# Usa a palavra reservada "return" para retornar o valor
# Não é necessario armazenar o retorno em uma variavel, pode ser passado diretamento para outras funções/...
# return finaliza a função
# uma função pode ter mais de um return
#
"""
ret = numeros = [1, 2, 3]

numeros.pop()
ret_pr = print(numeros) 
print(f"Retorno de Pop: {ret}")
print(f"Retorno de Print: {ret_pr}") # Não tem retorno por isso "None"
"""
"""
# ex 2
def quadrado_de_7_fake():
    print(7*7)

def quadrado_de_7():
    return 7*7
    
ret = quadrado_de_7() # None
print(ret)
print(f"Quadrado: {quadrado_de_7()}")

def diz_oi():
    return "Oi "

alguem = "Pedro"
print(diz_oi() + alguem)

"""
# ex 3 Diferentes retornos
"""
def nova_funcao():
    variavel = False
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return "b"

print(nova_funcao())
"""
"""
# ex 4 Retornando Multiplas Variaveis
def outra_funcao():
    return 1, 2, 4

num_1, num_2, num_3 = outra_funcao()

print(f"Numero 1: {num_1} | Numero 2: {num_2} | Numero 3: {num_3} | ")
"""
"""
#ex 5 Joga moeda

from random import random

def joga_moeda():
    valor = random()
    if valor > 0.5:
        return "cara"
    return "Coroa"

print(joga_moeda())

# Erros comuns ao usar retorno

def eh_impar():
    numero = 5
    if numero % 2 != 0:
        return True
    #errado coloca else aqui
    return False

"""

# 4 Funções com parametros
"""
def quadrado(numero):   #Função com parametro obrigatório
    #return numero * numero
    return numero ** 2

#print(quadrado(7))
#print(quadrado(4))
#print(quadrado(5))
#print(quadrado()) #TypeError

def canta_parabens(aniversariante):
    print("Parabens pra você")
    print("Nessa data querida")
    print("Muitas Felicidades")
    print(f"Viva o/a {aniversariante}")
    
canta_parabens("Marcos")
"""

# 5 Funções podem ter n parametros separados por ","
"""
def soma(a, b):
    return a + b

def multiplica(a, b):
    return a * b

def outra(a, b, msg):
    return (a + b)* msg


print(soma(5,7))
print(multiplica(5,7))
print(outra(3,2,"geek-"))
"""

# 6 Nomeando Parametros
"""
def nome_completo(nome, sobrenome):
    return f'Seu nome completo é {nome} {sobrenome}'


print(nome_completo("Filipe", "Gomes"))

# Parametros x Argumentos
# Parametros: São variaveis declaradas na definição da funçao
# Argumentos: Dados passados durante a execução de uma função
# A ordem importa

# 7 Argumentos Nomeados
nome = "Filipe"
sobrenome = "Gomes"
print(nome_completo(sobrenome = sobrenome,nome = nome))



def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total += num
        # return total # Errado
    return total # tem que ir aqui

numeros = [1, 2, 5, 9, 14, 16]

print(soma_impares(numeros))
"""

"""
# 8 Fuções com Parâmetros Padrão (Default Paramter)

# Ex Passagem de parametro obrigatória
def quadrado(numero):
    return numero ** 2

# Ex Valor Padrão
def exponencial(numero, potencia = 2):
    return numero ** potencia


print(exponencial(2,3))
print(exponencial(3,2))
print(exponencial(3))
print(exponencial(3,9))

# Outros exemplos
def mostrar_informacoes(nome = "Geek", instrutor = False):
    if nome == "Geek" and instrutor:
        return "Bem Vindo instrutor geek"
    elif nome == "Geek":
        return "Pensei que era o instrutor"
    return f"Ola {nome}"


print(mostrar_informacoes())
print(mostrar_informacoes(instrutor = True))
print(mostrar_informacoes(True))
print(mostrar_informacoes("Ozzi"))

# Porque usar parametros default:
# Evita erros com mparâmetros
# Gera Flexibilidade
# Exemplos mais legiveis de codigo
# Pode receber qualquer tipo de dados incluindo outras funções 

"""

def soma (num_1,num_2):
    return num_1 + num_2

def mat (num_1, num_2, fun = soma):
    return fun(num_1, num_2)

def subtrai (num_1,num_2):
    return num_1 - num_2

"""
print(mat(5, 6))

print(mat(5, 6,subtrai))
"""


# Escopo

#Cuidado com variaveis globais e locais
#Ver documentação de escopo da função (global, local, nonlocal)