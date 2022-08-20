topicos = [
    {'secao': '1', 'tempo': 16, 'status': True},  # a
    {'secao': '2', 'tempo': 76, 'status': True},  # a
    {'secao': '3', 'tempo': 101, 'status': True},  # a
    {'secao': '4', 'tempo': 95, 'status': True},  # a
    {'secao': '5', 'tempo': 45, 'status': True},  # a
    {'secao': '6', 'tempo': 94, 'status': True},  # a
    {'secao': '7', 'tempo': 433, 'status': True},  # a
    {'secao': '8', 'tempo': 255, 'status': True},  # a
    {'secao': '9', 'tempo': 86, 'status': True},  # a
    {'secao': '10', 'tempo': 314, 'status': True},  # a
    {'secao': '11', 'tempo': 169, 'status': False},  # a
    {'secao': '12', 'tempo': 160, 'status': False},  # a
    {'secao': '13', 'tempo': 300, 'status': False},  # a
    {'secao': '14', 'tempo': 108, 'status': False},  # a
    {'secao': '15', 'tempo': 118, 'status': False},  # a
    {'secao': '16', 'tempo': 284, 'status': False},  # a
    {'secao': '17', 'tempo': 185, 'status': False},  # a
    {'secao': '18', 'tempo': 107, 'status': False},  # a
    {'secao': '19', 'tempo': 98, 'status': False},  # a
    {'secao': '20', 'tempo': 186, 'status': False},  # a
    {'secao': '21', 'tempo': 9, 'status': False},  # a
    {'secao': '22', 'tempo': 59, 'status': False},  # a
    {'secao': '23', 'tempo': 135, 'status': False},  # a
    {'secao': '24', 'tempo': 73, 'status': False},  # a
    {'secao': '25', 'tempo': 50, 'status': False},  # a
    {'secao': '26', 'tempo': 60, 'status': False},  # a
    {'secao': '27', 'tempo': 96, 'status': False}  # a
]


def calcula_progresso(topicos):
    total = 0
    total_feito = 0
    for secao in topicos:
        total += secao['tempo']
        if secao['status']:
            total_feito += secao['tempo']
    percentual_feito = round(100*total_feito/total, 2)
    return total, total_feito, percentual_feito


total, feito, percentual = calcula_progresso(topicos)
print(f"Tempo total de curso: {total} minutos | {round(total/60, 2)} horas \n Tempo de curso feito: {feito} minutos | {round(feito/60, 2)} horas \n Representando: {round(100*feito/total, 2)} %")
print('---------------')
# Em construção


def altera_status(secao_alterar, curso, novo_status=True):
    #print(secao_alterar, curso)
    #filter(lambda sec: sec['secao'] == str(secao_alterar), curso)
    for topico in curso:
        if topico['secao'] == str(secao_alterar):
            topico['status'] = novo_status
    return curso


topicos = altera_status(11, topicos)
total, feito, percentual = calcula_progresso(topicos)
print(f"Tempo total de curso: {total} minutos | {round(total/60, 2)} horas \n Tempo de curso feito: {feito} minutos | {round(feito/60, 2)} horas \n Representando: {round(100*feito/total, 2)} %")
