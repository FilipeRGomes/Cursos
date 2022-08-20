"""
Documentando funções com Docstring


"""

def diz_oi():
    """Função simples que diz oi"""
    return "oi"


def exponencial(numero, potencia=2):
    """_summary_
        Função que retorna o numero "elevado" a "potencia" desejada ou ao quadrado por padrão
    Args:
        numero (real): Numero que desejamos elevar ao exponencial;
        potencia (int, optional): Potencia que querermos gerar. Padrão 2.

    Returns:
        real: "Numero" elevado a "potencia" desejada
    """
    return numero ** potencia

#Acessando a documentação
# print(diz_oi.__doc__)  #Propriedade Do
# help(diz_oi)

