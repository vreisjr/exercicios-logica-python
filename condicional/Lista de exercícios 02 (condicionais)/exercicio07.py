#apresentar um número de 5 dígitos

numero= str(input('Informe um número de 5 dígitos:'))

#dizer se esse número é um palíndromo

n_invert= numero [::-1]

if numero == n_invert:
    print ('É um palíndromo')
else:
    print ('Não é um palíndromo')
