# informar um número inteiro, e mostar a tabuada até 10

numero= int(input('Informe um número:'))
for n in range (1,11):
    print(str(numero)+'x'+str(n)+'=', numero * n)
