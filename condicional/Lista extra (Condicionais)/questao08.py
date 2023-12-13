#Inserir três valores inteiros diferentes

n1= int(input('Digite o primero número:'))
n2= int(input('Digite o segundo número:'))
n3= int(input('Digite o terceiro número:'))

#e mostrar eles de forma decrescente

if n1 > n2 > n3:
    print ('a ordem decrescente é:', n1, n2, n3)

elif n1 > n3 > n2:
    print ('a ordem decrescente é:', n1, n3, n2)

elif n2 > n1 > n3:
    print ('a ordem decrescente é:', n2, n1, n3)

elif n2 > n3 > n1:
    print ('a ordem decrescente é:', n2, n3, n1)

elif n3 > n1 > n2:
    print ('a ordem decrescente é:', n3, n1, n2)

elif n3 > n2 > n1:
    print ('a ordem decrescente é:', n3, n2, n1)