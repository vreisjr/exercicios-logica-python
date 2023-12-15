nome_aluno= input('Informe o nome do aluno:')

nome_junto= (nome_aluno.replace(' ',''))
nome_minsc= (nome_junto.lower())
silva= (nome_minsc.find('silva'))

if silva > -1:
    print ('Esse nome contém "Silva"')

else:
    print ('Esse nome não tem "Silva"')

#Programa quebra quando digita nome "Silvana", ou "Luís da Silva"