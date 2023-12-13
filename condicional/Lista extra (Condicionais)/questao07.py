#inserir um número

numero= float(input('Digite um número:'))

#se for par, somar com 5; se for ímpar, somar com 8

resultado= numero % 2

if resultado == 0:
    print ('o número', numero, 'é par, logo, soma com 5, que dá:', numero + 5)

else:
    print ('o número', numero, 'é ímpar, logo, soma com 8, que dá:', numero + 8)