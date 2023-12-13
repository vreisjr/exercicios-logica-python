# Informar o nome, sexo e estado civil de uma pessoa

nome= input('Informe o nome:')
sexo= input('Informe o Sexo (F ou M):')
est_civil= input('Informe o Estado Civil:')

# caso seja sexo F e estado civil seja "Casada", solicitar e imprimir o tempo de casada

if sexo == 'f' and est_civil == 'casada':
    print (input('Informe tempo de casada (anos):'))

else:
    print ('Ok')