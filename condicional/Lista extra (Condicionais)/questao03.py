# informar um número

numero= float(input('Informe um número:'))

#Informar se é ímpar ou par

resultado= numero % 2
if resultado == 0:
    print (numero, 'é um número par')

else:
    print (numero, 'é um número ímpar')
