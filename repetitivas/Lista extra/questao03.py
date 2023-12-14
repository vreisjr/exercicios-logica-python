
numeros_pares= 0
n1= int(input('Informe o primeiro número:'))
n2= int(input('Informe o segundo número:'))

if n1 < n2:
    for i in range (n1, n2 + 1):
        resto= i % 2
        if resto == 0:
            numeros_pares= numeros_pares + 1
    print ('São', numeros_pares, 'números pares de', n1, 'até', n2)


if n2 < n1:
    for i in range (n2, n1 + 1):
        resto= i % 2
        if resto == 0:
            numeros_pares= numeros_pares + 1
    print ('São', numeros_pares, 'números pares de', n1, 'até', n2)
