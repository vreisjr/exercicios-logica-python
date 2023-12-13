# informar um número possitivo, ou negativo
n= float(input('Informe um número possitivo ou negativo:'))

# Se for possitivo, multiplicar por 2, se for negativo, triplicar

if n >= 0:
    n_final= n * 2

else:
    n_final= n * 3

print('O resultado foi:', n_final)
