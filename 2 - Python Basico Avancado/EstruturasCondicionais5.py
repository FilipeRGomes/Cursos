"""
if

elif

else


"""
idade = "6"


if idade.isnumeric():

    if int(idade) < 18:
        print("Menor de idade")
    elif int(idade) > 60:
        print("idoso")
    elif int(idade) >= 18 or idade <= 60:
        print("Adulto")
else:
    print("Erro - not num")
