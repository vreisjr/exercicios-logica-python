#Informar um número

numero= float(input('Informe um número:'))

#verificar se ele é multiplo de 3 e 7. Se sim, mostrar a menssagem 'é múltiplo de 3 e 7'; se não, mostrar 'não é múltiplo de 3 e 7'

if numero == (numero % 3) == 0 and (numero % 7) == 0:
    print ('O número é múltiplo de 3 e 7')
else:
    print ('O número não é múltiplo de 3 e 7')
