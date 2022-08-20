###########################################################################################################################################
# ------------------------------------------------------------------------------------------------------------------------------------------
#  Debuggando com PDB
"""

- PDB: Python Debugger
- Quando tratar erros??
    - Toda entrada do usuario deve ser tratada

Exs:
-
"""
# ------------------------------------------------------------------------------------------------------------------------------------------
"""
# Usar o print para debuggar é uma pratica ruim existem formas mais proficionais 
def dividir(a, b):
    print(f'a= {a} | b= {b}')
    try:
        return int(a) / int(b)
    except (ValueError, NameError, ZeroDivisionError) as err:
        return f'Erro Inesperado | Erro: {err}'
    
    # Tratamento Generico
    except:
        return f'Erro Inesperado'
    

print(dividir(input('digite o pirmeiro valor: '), input('digite o segundo valor: ')))
"""

"""
#EX com VSCODE
def dividir(a, b):
    print(f'a= {a} | b= {b}')
    try:
        return int(a) / int(b)
    except (ValueError, NameError, ZeroDivisionError) as err:
        return f'Erro Inesperado | Erro: {err}'
    
    # Tratamento Generico
    except:
        return f'Erro Inesperado'
    

print(dividir(4, 0))
"""


#EX com PDB
# Precisamos importar o PDB* e usar a função set_trace()
# Comando Basicos PDB
"""
l -> Lista ponto atual do codigo
n -> Proxima Linha
p -> Imprime variavel
c -> Continua execução / finaliza debugging 
"""
"""
import pdb
nome = 'Angelina'
sobrenome = 'Jolie'
pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação Python '
final = nome_completo + ' faz o curso ' + curso
print(final)
"""
"""
#* A partir do Python 3.7 não precisa importar o PDB pois este foi incorporado e virou breakpoint()

nome = 'Angelina'
sobrenome = 'Jolie'
breakpoint()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação Python '
final = nome_completo + ' faz o curso ' + curso
print(final)
"""