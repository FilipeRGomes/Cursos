import primeiro

def funcao_2():
    primeiro.funcao_1()
    
if __name__ == '__main__':
    funcao_2()
    print('Segundo.py sendo executado como principal')
else:
    print(f'Segundo.py Importado {__name__}')