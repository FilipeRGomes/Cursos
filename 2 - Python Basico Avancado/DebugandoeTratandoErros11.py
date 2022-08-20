##########################################################################################################################
# ------------------------------------------------------------------------------------------------------------------------
# Erros mais comuns / Exceptions
"""
SyntaxError -> Erro de sintax do python
NamedError -> Função/metodo não criado
TypeError -> Ocorro quando uma função/operação/ação é aplicada a um tipo errado
IndexError -> Ocorre quando tentamos acessar um elemento em um indice invalido
ValueError -> Ocorre quando uma função/operação built-in recebe um argumento do tipo correto mas com valor invalido
KeyError -> Tentativa de acesso a uma chave que não existe no dicionario
AttributeError -> Variavel não tem atributo/função
IndentationError -> Erro de indentação do codigo


"""
# ------------------------------------------------------------------------------------------------------------------------
"""
#ex NamedError
printf('printF errado')  # NamedError - objeto não criado
print(geek)

"""

"""
# ex syntax error

# EX1
def funcao:
    return 1
    
# EX2
return    
"""
"""
#EX TypeError -> Ocorro quando uma função/operação/ação é aplicada a um tipo errado
print(len(5))
print('geek'+ [])
"""
"""
# IndexError -> Ocorre quando tentamos acessar um elemento em um indice invalido
lista = ['geek']
print(lista[1])
"""

"""
# ValueError -> Ocorre quando uma função/operação built-in recebe um argumento do tipo correto mas com valor invalido
print(int('G'))
"""
"""
# KeyError -> Tentativa de acesso a uma chave que não existe no dicionario
dicionario = {}
print(dicionario['geek'])
"""

"""
# AttributeError -> Variavel não tem atributo/função
tupla = (1, 2, 5)
tupla.sort()
print(tupla)
"""
##########################################################################################################################
# ------------------------------------------------------------------------------------------------------------------------
# Raise -> Levantando os proprios erros
"""

Syntax:

raise TipoDoErro('Mensagem')

OBS: Raise não é uma função é uma palavra reservada
OBS: Raise FINALIZA a função
"""
# ------------------------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------------------------------##########################################################################################################################
"""
EX 1
def colore(texto, cor):
    if type(texto) is not str:
        raise TypeError('O texto precisa ser string')

    if type(cor) is not str:
        raise TypeError('A cor precisa ser string')

    print(f'texto {texto} - cor: {cor}')


colore('geek', 4)
"""
"""
# EX 2


def colore(texto, cor):
    cores = ('verde', 'amarelo', 'azul', 'branco')
    if type(texto) is not str:
        raise TypeError('O texto precisa ser string')

    if type(cor) is not str:
        raise TypeError('A cor precisa ser string')

    if cor not in cores:
        raise ValueError(f'A {cor} precisa ser uma entre {cores}')

    print(f'texto {texto} - cor: {cor}')


colore('geek', 'preto')
"""
##########################################################################################################################
# ------------------------------------------------------------------------------------------------------------------------
# Try/Except
"""
o bloco Try/Except é usado para tratar erros


Syntax:

#Forma mais simples

try:
    //execução problematica
except:
    //se problema faz o que esta aqui


"""
# ------------------------------------------------------------------------------------------------------------------------
"""
#EX 1
try:
    geek()
except:
    print('Deu BO')
"""
"""
# EX 2
try:
    len(5)
except:
    print('Deu BO s')
"""

"""
# EX 3 Tratando erro especifico
try:
    geek()
except NameError:
    print('Deu BO')
    """
"""
# EX 3 Tratando erro especifico
try:
    len(5)
except TypeError:
    print('Deu BO')
"""
"""
try:
    geek()
except NameError as err:
    print(f'A aplicação gerou o erro: {err}')

"""
"""
try:
    # len(5)
    # geek()
    print('geek'[5])
except TypeError as err_1:
    print(f'Deu o BO: {err_1}')
except NameError as err:
    print(f'A aplicação gerou o erro: {err}')

except:
    print('Erro Diferente')
"""


def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None


dic = {'nome': 'geek'}

print(pega_valor(dic, 'nome'))
