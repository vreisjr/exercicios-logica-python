#fazer várias entradas de números, até digitar o número 0. somar os 10 números subsequentes desse números e tirar a média

n= int(input('Insira um número:'))
while n != 0:
    soma=0
    for i in range (n+1,n+11):
        soma= soma + i
    n_media= soma / 10
    print('A soma dos 10 numeros subsequentes é:',soma,', e a média desses números é:',n_media)
    n= int(input('Insira um número:'))