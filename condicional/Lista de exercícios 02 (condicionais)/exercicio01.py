#informe um número inteiro possitivo de 0 até 10

n= int(input('Digite um número de 0 a 10:'))

#mostrar por extenso o nome do número. do contrário, mostrar a mensagem 'número invalido'

if n == 0:
    extenso= 'Zero'
elif n == 1:
    extenso= 'Um'
elif n == 2:
    extenso= 'Dois'
elif n == 3:
    extenso= 'Três'
elif n == 4:
    extenso= 'Quatro'
elif n == 5:
    extenso= 'Cinco'
elif n == 6:
    extenso= 'Seis'
elif n == 7:
    extenso= 'Sete'
elif n == 8:
    extenso= 'Oito'
elif n == 9:
    extenso= 'Nove'
elif n == 10:
    extenso= 'Dez'
elif n > 10:
    extenso= 'Número inválido'

print (extenso)
