#Receber duas entradas de altura e sexo de uma pessoa

altura= float(input('Informe a altura:'))
sexo= str(input('Informe o sexo (F ou M):'))

if sexo == 'F':
    peso_ideal= (62.1 * altura) - 44.7

elif sexo == 'M':
    peso_ideal= (72.7 * altura) - 58

print ('O peso ideal é:', peso_ideal)