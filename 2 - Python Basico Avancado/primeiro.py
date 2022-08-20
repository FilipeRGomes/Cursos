from unicodedata import name


def funcao_1():
    print('geek university - Primeiro.py')
    
if __name__ == '__main__':
    funcao_1()
    print('Primeiro sendo executado como principal')
else:
    print(f'primeiro importado {__name__}')