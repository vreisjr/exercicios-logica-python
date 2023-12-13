#Informe a idade

idade= int(input('Informe a idade:'))

#classificar a classe eleitoral:

if idade <= 65 and idade >= 18:
    print ('Eleitor obrigatório')
elif idade < 16:
    print ('Não eleitor')
else:
    print ('Eleitor Facultativo')
