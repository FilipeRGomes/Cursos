############################################################################################################################################
# ------------------------------------------------------------------------------------------------------------------------------------------
#  Modulo random
"""
Random -> possue diversas funções para geração de numeros pseudoaleatorios
- Modulos são outros arquivos python.
Exs:
-
"""
# ------------------------------------------------------------------------------------------------------------------------------------------

#OBS: Duas formas de utilizar modulo ou a função deste
"""
#forma 1 - Importando todo o modulo  (tudo fica em memoria - não recomendavel)
import random
print(random.random()) # NomeDoModulo.NomeDaFuncao()
# Não confunda o pacote random com a função random()
"""
"""
#forma 2- Importa so as funções/atributos/metodos especificados (mais recomendado para evitar o disperdicio de memoria )
from random import random
print(random()) # NomeDoModulo.NomeDaFuncao()
"""
"""
# uniform() -> gera numero pseudoaleatorio com base em um intervalo

from random import uniform

for i in range(10):
    print(uniform(3, 7)) #Nunca gera o 7
"""
"""
# randint()-> Gera valores pseudoaleatorios INTEIROS

# gerador de apostas para a megasena
from random import randint

for i in range(0,6):
    print(randint(1, 61), end=', ')
"""
"""
# choice() -> Mostra um valor aleatorio dentro de um iteravel
from random import choice
jogadas = ['pedra', 'papel', 'tesoura']
print(choice(jogadas))
print(choice('Teste com Strings'))
"""
"""
# shuffle() -> Embaralha dados
from random import shuffle

cartas = ['K', 'Q', 'J', 'A', '1', '2', '3']
print(cartas)
shuffle(cartas)
print(cartas)
"""

############################################################################################################################################
# ------------------------------------------------------------------------------------------------------------------------------------------
#  Modulos Build-In
"""
Random -> possue diversas funções para geração de numeros pseudoaleatorios
- Modulos são outros arquivos python.
Exs:
-
"""
# ------------------------------------------------------------------------------------------------------------------------------------------
"""
# Usando alias (apelidos)
import random as rdm

print(rdm.random())
""""""

from random import randint as rdi, random as rdm

print(rdi(5, 99))

print(rdm())
"""
"""
# Muitas funções
#from random import random, randint, shuffle, choice # Não recomendado
from random import (
    random,
    randint,
    shuffle,
    choice
) #Recomendado
"""
"""
############################################################################################################################################
# ------------------------------------------------------------------------------------------------------------------------------------------
#  Modulos Customizados
"""
 
"""
# ------------------------------------------------------------------------------------------------------------------------------------------

from Funcoes import soma

print(soma(1, 3))
"""

############################################################################################################################################
# ------------------------------------------------------------------------------------------------------------------------------------------
#  Modulos Externos
"""
- Para instalar modulos externos usamos o pip - Python Installer Package
- Encontre, Instale, Publique modulos em python  pypip.org
"""
# ------------------------------------------------------------------------------------------------------------------------------------------


############################################################################################################################################
# ------------------------------------------------------------------------------------------------------------------------------------------
#  Pacote
"""
- Modulo: É apenas um arquivo python que pode ter diversas funções 
- Pacote é um conjunto de modulos 

Syntax:
- Pacote inteiro
    - Estando na mesma pasta
        Importando: from nome_pacote import modulo_1, ... modulo_n
        Usando: modulo_1.funcao_1()
    - Em subpasta
        Importando: from nome_pasta.nome_pacote import modulo_1, ... modulo_n
        Usando: modulo_1.funcao_1()
- Somente uma função
    - Estando na mesma pasta
            Importando: from nome_pacote.modulo import funcao_1, ... funcao_n
            Usando: funcao_1()
    - Em subpasta
        Importando: from nome_pasta.nome_pacote.modulo import funcao_1, ... funcao_n
        Usando: funcao_1()
        
OBS:
- Nas versões 2.x do python um pacote pyton deveria conter dentro dele um arquivo chamado __init__.py
- nas versões 3.x não é obrigatorio mas é utilizado para manter compatibilidade

"""
# ------------------------------------------------------------------------------------------------------------------------------------------

############################################################################################################################################
# ------------------------------------------------------------------------------------------------------------------------------------------
#  Dunder Name e Dunder Main
"""
- Dunder -> Doble Under
- Dunder Name -> __name__
- Dunder Main -> __main__

# Na limguagem C temos:
int main(){
    //processo
}
# Em java 
public static void main(string[] args){
    //processo
}

#Em Python executamos um modulo Python diretamente na linha de comando, internamente o Python atribuira a variavel __name__ o valor __main__ indicando que este modulo de execução principal.



"""
# ------------------------------------------------------------------------------------------------------------------------------------------
"""
# EX1
def soma_impares(numeros):
    soma = 0
    for numero in numeros:
        if numero % 2 != 0:
            soma += numero
    return numero



if __name__ == '__main__':
    lista = [1, 2, 3, 4, 5, 6, 7]
    print(soma_impares(lista))
    tupla = (1, 2, 3, 4, 5, 6, 7)
    print(soma_impares(tupla))
"""
#EX2 
# Arquivos primeiro.py e segundo.py
import primeiro
import segundo
