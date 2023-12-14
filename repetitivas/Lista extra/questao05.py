soma_idade= 0

n_pessoa= int (input('Quantas pessoas estão no grupo:'))
for i in range (n_pessoa):
    idade= int(input('Informe a idade:'))
    soma_idade= soma_idade + idade

media_idade= soma_idade / n_pessoa

if media_idade >= 60:
    print ('A idade média é de', media_idade, ',portanto, a turma é considerada idosa')

if media_idade < 60 and media_idade >= 26:
    print ('A idade média é de', media_idade, ',portanto, a turma é considerada adulta')

if media_idade <= 25:
    print ('A idade média é de', media_idade, ',portanto, a turma é considerada jovem')