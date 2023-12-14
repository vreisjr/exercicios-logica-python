#inserir 20 números inteiros, e apresentar a: média dos ímpares, maior número par e a diferença do maior menos o menor número

soma_impar= 0
conta_impar= 0 
maior_par= 0 
numero= int(input('Informe um número:'))
maior_n= 0
menor_n= 0 

for i in range (4):
    if numero % 2 != 0:
        soma_impar= soma_impar + numero
        conta_impar= conta_impar + 1

    elif numero > maior_par:
            maior_par= numero

    if numero > maior_n:
        maior_n= numero
    if numero < menor_n:
        menor_n= numero

    numero= int(input('Informe um número:'))

dife= maior_n - menor_n
media_impar= soma_impar / conta_impar

print (media_impar)
print (maior_par)
print (dife)