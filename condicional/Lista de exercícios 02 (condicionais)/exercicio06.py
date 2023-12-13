#Digite a idade de uma pessoa

idade= int(input('Informe a Idade:'))

#informar a classificação da idade, se for menor de idade, inferior a 21; se for maior, superior ou igual a 21; se for superior ou igual a 65, idoso

if idade >= 65:
    print ('Pessoa idosa')
elif idade >= 21:
    print ('Pessoa maior de idade')
else:
    print ('Pessoa menor de idade')
