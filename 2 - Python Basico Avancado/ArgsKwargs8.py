#------------------------------------------------------------------------------------------------------------------------------------------
#   Args
"""
- O *args é um parâmetro, como outro qualquer, isso significa que pode  receber qualquer nome MAS DEVE MANTER * no inicio

Exs:
- *X, *Numero

Por convenção foi definido *args

O que é *args?

O parâmetro *args usado em uma função cloca os valores extras informados como uma tupla


"""
#------------------------------------------------------------------------------------------------------------------------------------------
"""
# não é legal
def soma_todos_numeros(num_1, num_2, num_3):
    return num_1 + num_2 + num_3

print(soma_todos_numeros(2, 5, 7))
"""
# 1 Usando args

from ast import Num, arg

"""
def soma_todos_numeros(*args):
    total = 0
    for numero in args:
        total += numero
    return total
"""

"""
def soma_todos_numeros(*args):
    return sum(args)

print(soma_todos_numeros(2, 5, 7))
print(soma_todos_numeros(1))
print(soma_todos_numeros(4, 5, 7, 12, 9))

"""
"""
def verifica_info(*args):
    if "Geek" in args and "University" in args:
        return "Bem vindo geek"
    return "Não te conheço"

print(verifica_info())
print(verifica_info(True))
print(verifica_info(1))
print(verifica_info("Geek","University"))
print(verifica_info("Geek"))
"""
"""
def soma_todos_numeros(*args):
    return sum(args)


numeros = [1, 3, 5, 9]

#print(soma_todos_numeros(numeros)) #TypeError

#Desempacotamento
print(soma_todos_numeros(*numeros)) #* Informa ao python que estamos passando uma coleção e ele sabe que precisa desempacotar antes de usar
"""

#------------------------------------------------------------------------------------------------------------------------------------------
#   Kwargs
"""
- O **kwargs é um parâmetro, como outro qualquer, mas diferente do *args que coloca os valores em uma tupla, o *kwargs exige que utilizemos parametros nomeados


Exs:
- *X, *Numero

Por convenção foi definido *kwargs

O que é *kargs?

O parâmetro *args usado em uma função cloca os valores extras informados como uma tupla


"""
#------------------------------------------------------------------------------------------------------------------------------------------

"""
# ex 1
def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f"A cor favorita de {pessoa.title()} é {cor}")

cores_favoritas(marcos="verde",filipe="amarelo",fernanda="azul")
"""
"""
def cumprimento_especial(**kwargs):
    if "geek" in kwargs and kwargs["geek"] == "Python":
        return "Pythonico"
    elif "geek" in kwargs:
            return f"{kwargs['geek']} Geek"
    return "Não te conheço"

print(cumprimento_especial())
dicionario = {"Geek": "Python"}
print(cumprimento_especial(geek="Python"))
print(cumprimento_especial(geek="OI"))
print(cumprimento_especial(geek="Espcial"))
"""

# Ordem dos parametros na função 
"""
def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f"{nome} tem {idade} anos")
    print(args)
    if solteiro:
        print("solteiro")
    else:
        print("Casado")
    print(kwargs)
    
    
minha_funcao(8, "Julia")
minha_funcao(18, "Felicity", 4, 5, 6, solteiro=True)
minha_funcao(33, "Filipe", eu="não", voce="vai")
"""
"""
# Entenda porque da ordem

# Parametros na ordem correta
def mostra_info(a, b, *args, instrutor="geek", **kwargs):
    return[a, b, args, instrutor, kwargs]

# Parametros na ordem incorreta
#def mostra_info(a, b, instrutor="geek", *args, **kwargs):
#    return[a, b, args, instrutor, kwargs]


print(mostra_info(1, 2, 3, sobrenome="GeekUn", cargo="instrutor"))
"""

#Desempacotar Kwargs
"""
def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} - {kwargs['sobrenome']}"

nomes = {"nome":"Felcicity", "sobrenome":"jones"}

print(mostra_nomes(**nomes))
"""
"""
def soma_multiplos_numeros(a, b, c):
    print(a + b + c)
    
lista = [1, 3, 5]
soma_multiplos_numeros(*lista) # * Desempacora lista, tupla ou conjunto

dicionario = {"a":1, "b":2, "c":3}
soma_multiplos_numeros(**dicionario) # ** Desempacota dicionario

"""