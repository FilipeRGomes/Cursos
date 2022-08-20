###########################################################################################################################################
# ------------------------------------------------------------------------------------------------------------------------------------------
#  Try,Except, Else, Finally
"""
- Quando tratar erros??
    - Toda entrada do usuario deve ser tratada

Exs:
-
"""
# ------------------------------------------------------------------------------------------------------------------------------------------
"""
# EX1
num = 0

try:
    num = int(input('Informe um numero: '))

except ValueError as value:
    
    print('valor incorreto!')

else:
    print(f'Você digitou {num}') # Só é executado se não ocorrer o erro
    
"""
"""
# EX2
num = 0

try:
    num = int(input('Informe um numero: '))

except ValueError as value:
    
    print('valor incorreto!')

else:
    print(f'Você digitou {num}') # Só é executado se não ocorrer o erro

finally:
    # Geralmente é usado para realizar rotinas de finalização
    #ex: fechar conexão com DB, fechar arquivos, zerar variaveis....
    print('Sempre executa o finally independente se houve excessão ou não')
"""

"""
# EX3
def dividir(a, b):
    try:
        return int(a) / int(b)
    except ValueError as errVal:
        return f'O vaor precisar ser numerico | Erro: {errVal}'
    
    except NameError as errName:
        return f'Valor não declarado | Erro: {errName}'
    
    except ZeroDivisionError as errZero:
        return f'Não é possivel realizar divisão por 0| Erro: {errZero}'
    # Tratamento Generico
    except:
        return f'Erro Inesperado'
    

print(dividir(input('digite o pirmeiro valor: '), input('digite o segundo valor: ')))
"""

"""
# EX4
def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, NameError, ZeroDivisionError) as err:
        return f'Erro Inesperado | Erro: {err}'
    
    # Tratamento Generico
    except:
        return f'Erro Inesperado'
    

print(dividir(input('digite o pirmeiro valor: '), input('digite o segundo valor: ')))
"""