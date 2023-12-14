maior_idade= 0
conta_mulher= 0
conta= 0
idade= int(input('Informe a idade:'))

while idade != -1:
    sexo= input('Informe o sexo:')
    olhos= input ('Informe a cor dos olhos:')
    conta= conta + 1

    if maior_idade < idade:
        maior_idade= idade
    
    if sexo == 'f' and olhos == 'verde' and idade >= 18 and idade <= 35:
        conta_mulher= conta_mulher + 1
    
    idade= int(input('Informe a idade:'))

perc_mulher= conta_mulher / conta

print (maior_idade)
print (perc_mulher)
