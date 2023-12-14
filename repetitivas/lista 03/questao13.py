# fazer 50 entradas de dados contendo: altura e sexo ('f' ou 'm'). fazer que op programa calcule: a maior e a menor altura do grupo; média de altura das mulheres e o número de homens

menor_altura= 99999999999999999999
maior_altura= -1
altura_f= 0
n_homens= 0
n_mulheres= 0

for i in range (5):
    sexo= input('Informe o sexo (f ou m):')
    altura= float(input('Informe a altura:'))

    if sexo == 'f':
        n_mulheres= n_mulheres + 1
        altura_f= altura_f + altura
        media_altura_f= altura_f / n_mulheres
    
    if sexo == 'm':
        n_homens= n_homens + 1

    if altura > maior_altura:
        maior_altura= altura
    
    if altura < menor_altura:
        menor_altura= altura


print ('A maior altura é', maior_altura, ', e amenor é:', menor_altura)   
print ('A média da altura das mulheres é:', media_altura_f)
print ('o número de homens é:', n_homens)
