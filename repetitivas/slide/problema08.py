#elaborar um programa que receba valores alatórios, e encerrar quando receber um número com o valor igual a 999. Mostrar: 1 - a quantidade de números digitados; 2 - a soma dos valores digitados; 3 - a média dos números pares digitados 

qtd_n= 0
qtd_par= 0
soma_par= 0
soma_n=0 

numero= int(input('Informe um número:'))

while numero != 999:
    qtd_n= qtd_n + 1
    soma_n= soma_n +numero
    numero= int(input('Informe um número:'))

    if numero % 2 == 0:
        qtd_par= qtd_par + 1
        soma_par= soma_par + numero
    
media_par= soma_par / qtd_par
        
print ('A qauntidade de números digitada foi de:', qtd_n)
print ('A soma dos números digitados foi de:', soma_n)
print ('A média dos números digitados foi de:', media_par)