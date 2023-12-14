#Informar um número inteiro
numero= int(input('Informe um número inteiro:'))

#exibir a soma dos números até o número que foi inserido

soma= 0
for n in range (1, numero+1):
    soma= soma + n
print ('a soma de 1 até', numero, 'é:', soma)
