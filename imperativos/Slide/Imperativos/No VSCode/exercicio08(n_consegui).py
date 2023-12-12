#Digitar a quantidade de candidatos masculinos, femininos e ausentes de um concurso público

qtd_masc= int(input('Digite o número de candidatos masculinos:'))
qtd_fem= int(input('Digite o número de candidatos femininos:'))
qtd_aus= int(input('Digite o número de candidatos ausentes:'))

#calcular o percentual de homens presentes em relação aos inscritos, e o percentual de ausentes em relação ao total dos inscritos

inscr= qtd_masc + qtd_fem + qtd_aus
por_masc= inscr / (qtd_masc * 100)
por_aus= inscr /  (qtd_aus * 100)

print ('São', por_masc, 'candidatos masculinos, e', por_aus, 'candidatos ausentes')
