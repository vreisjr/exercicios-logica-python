#informar 50 números digitados via teclado, valores aleatórios

soma= 0
for n in range (5):
    numero= float(input('Informe um número:'))
    soma= soma + numero

media= soma / 5
print ('soma=', soma, 'media=', media)
